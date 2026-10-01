#!/usr/bin/env python3
"""Narrate a lesson article section by section (macOS).

Reads lessons/<slug>.html, speaks the intro and each <h2> section with the
Kokoro neural voice (via uv; falls back to the macOS `say` voice), joins them into one audio file (so playback continues with
the phone screen locked), and adds a "Listen" button to every section that
starts playback at that section.

    python3 <teach skill>/scripts/narrate-lesson.py lessons/0001-idempotency-and-deduplication.html

Writes lessons/audio/<slug>.mp3 and updates the HTML in place: total listening and
reading time under the title, a listen button with its length per section, and a
bottom player whose scroll progress bar shows percent read and time left. Safe to re-run; --keep-audio
refreshes the page without regenerating the audio.
macOS only. Requires `ffmpeg`, plus `uv` and `espeak-ng` for Kokoro; without
them it uses the macOS `say` voice. The lesson must be an <article> with a
<p class="standfirst"> and <h2> section headings. NARRATION_ENGINE=say|kokoro
NARRATION_VOICE, and NARRATION_CACHE (default /Volumes/T9/Dev/.cache) override the defaults.
"""
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path

PREFERRED_VOICES = ["Ava (Premium)", "Zoe (Premium)", "Ava (Enhanced)", "Zoe (Enhanced)", "Samantha"]
RATE = "185"  # words per minute, for the macOS `say` fallback
KOKORO_VOICE = "af_heart"
READING_WPM = 230
KOKORO_SPEED = 1.0
# Keep the model and packages on the external drive, not in the home directory.
DEFAULT_CACHE = "/Volumes/T9/Dev/.cache"
KOKORO_DEPS = [
    "--with", "kokoro>=0.9.4", "--with", "transformers>=4.45", "--with", "soundfile",
    "--with", "en-core-web-sm@https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl",
]
SKIP_TAGS = {"title", "style", "script", "footer", "button", "audio"}
CODE_NOTE = "The page shows the code for this step."


def pick_voice():
    if os.environ.get("NARRATION_VOICE"):
        return os.environ["NARRATION_VOICE"]
    installed = subprocess.run(["say", "-v", "?"], capture_output=True, text=True).stdout
    for voice in PREFERRED_VOICES:
        if re.search(rf"^{re.escape(voice)}\s", installed, re.M):
            return voice
    return "Samantha"


class SectionText(HTMLParser):
    """Collect spoken text per section: the intro, then one per <h2>."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.sections = [[]]
        self.skip = 0
        self.in_pre = False

    def handle_starttag(self, tag, attrs):
        if tag in SKIP_TAGS:
            self.skip += 1
        elif tag == "pre":
            self.in_pre = True
            self.sections[-1].append(f" {CODE_NOTE} ")
        elif tag == "h2" and not self.skip:
            if any(t.strip() for t in self.sections[-1]):
                self.sections.append([])
        if tag in {"p", "li", "h1", "h2", "blockquote"}:
            self.sections[-1].append("\n")

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS:
            self.skip = max(0, self.skip - 1)
        elif tag == "pre":
            self.in_pre = False
        if tag in {"h1", "h2"}:
            self.sections[-1].append(". ")
        if tag in {"p", "li", "blockquote"}:
            self.sections[-1].append("\n")

    def handle_data(self, data):
        if not self.skip and not self.in_pre:
            self.sections[-1].append(data)


def section_texts(page):
    body = re.sub(r'<p class="(?:kicker|lesson-length)">.*?</p>', "", page, flags=re.S)
    body = re.sub(rf"{PLAYER_START}.*?{PLAYER_END}", "", body, flags=re.S)
    parser = SectionText()
    parser.feed(body)
    texts = []
    for parts in parser.sections:
        text = re.sub(r"[ \t]+", " ", "".join(parts))
        text = re.sub(r"\n\s*", "\n", text).strip()
        if text:
            texts.append(text)
    return texts


def duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True,
    ).stdout
    return float(out.strip())


def synth_say(texts, tmp):
    voice = pick_voice()
    paths = []
    for i, text in enumerate(texts):
        txt, aiff = Path(tmp, f"{i}.txt"), Path(tmp, f"{i}.aiff")
        txt.write_text(text + " [[slnc 900]]")
        subprocess.run(["say", "-v", voice, "-r", RATE, "-o", str(aiff), "-f", str(txt)], check=True)
        paths.append(aiff)
    return paths, f"say:{voice}"


def synth_kokoro(texts, tmp):
    voice = os.environ.get("NARRATION_VOICE", KOKORO_VOICE)
    job = Path(tmp, "job.json")
    job.write_text(json.dumps({"voice": voice, "speed": KOKORO_SPEED, "texts": texts, "outdir": tmp}))
    helper = Path(__file__).with_name("kokoro_tts.py")
    cache = Path(os.environ.get("NARRATION_CACHE") or (DEFAULT_CACHE if Path(DEFAULT_CACHE).parent.is_dir() else Path.home() / ".cache"))
    env = {**os.environ, "UV_CACHE_DIR": str(cache / "uv"), "HF_HOME": str(cache / "huggingface")}
    subprocess.run(["uv", "run", "--quiet", "--python", "3.11", *KOKORO_DEPS, "python", str(helper), str(job)],
                   check=True, env=env)
    return [Path(tmp, f"{i}.wav") for i in range(len(texts))], f"kokoro:{voice}"


def narrate(texts, out_path):
    engine = os.environ.get("NARRATION_ENGINE") or ("kokoro" if shutil.which("uv") else "say")
    with tempfile.TemporaryDirectory() as tmp:
        if engine == "kokoro":
            try:
                parts, voice = synth_kokoro(texts, tmp)
            except (subprocess.CalledProcessError, OSError) as err:
                if not shutil.which("say"):
                    raise
                print(f"Kokoro failed ({err}); falling back to the macOS voice.", file=sys.stderr)
                parts, voice = synth_say(texts, tmp)
        else:
            parts, voice = synth_say(texts, tmp)
        starts, clock = [], 0.0
        for part in parts:
            starts.append(round(clock, 2))
            clock += duration(part)
        listing = Path(tmp, "list.txt")
        listing.write_text("".join(f"file '{p}'\n" for p in parts))
        out_path.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(listing),
             "-ac", "1", "-c:a", "libmp3lame", "-b:a", "48k", str(out_path)],
            check=True,
        )
    return starts, round(clock, 2), voice


PLAYER_START = "<!-- narration:start -->"
PLAYER_END = "<!-- narration:end -->"


def minutes(seconds):
    return f"{max(1, round(seconds / 60))} min"


def inject(page, audio_src, starts, total, words):
    page = re.sub(r'\s*<button class="listen"[^>]*>.*?</button>', "", page, flags=re.S)
    page = re.sub(r'\s*<p class="lesson-length">.*?</p>', "", page, flags=re.S)
    page = re.sub(rf"\s*{PLAYER_START}.*?{PLAYER_END}", "", page, flags=re.S)

    def button(start, label):
        return f'\n  <button class="listen" type="button" data-start="{start}">&#9654; {label}</button>'

    # Total length above the standfirst; a whole-lesson button after it; one button per <h2> section.
    read = minutes(words / READING_WPM * 60)
    page = re.sub(r"(\s*)(<p class=\"standfirst\">)",
                  lambda m: f'{m.group(1)}<p class="lesson-length">{minutes(total)} listen · {read} read</p>{m.group(1)}{m.group(2)}',
                  page, count=1)
    ends = starts[1:] + [total]
    sections = iter(zip(starts[1:], ends[1:]))
    page = re.sub(r"(<p class=\"standfirst\">.*?</p>)",
                  lambda m: m.group(1) + button(starts[0], f"Listen from the start · {minutes(total)}"), page, count=1, flags=re.S)

    def section_button(m):
        start, end = next(sections, (starts[-1], total))
        return m.group(1) + button(start, f"Listen to this section · {minutes(end - start)}")

    page = re.sub(r"(<h2[^>]*>.*?</h2>)", section_button, page, flags=re.S)

    player = f"""
{PLAYER_START}
<style>
.lesson-length {{ margin: .8rem 0 0; color: var(--muted, #5d676c); font: 600 .85rem/1.4 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
.listen {{ display: inline-flex; align-items: center; gap: .4rem; margin: 0 0 1.1rem; padding: .35rem .8rem; border: 1px solid var(--line, #dde3e2); border-radius: 99px; background: transparent; color: var(--accent, #0c6865); font: 600 .85rem/1.3 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; cursor: pointer; }}
.listen:hover {{ background: var(--accent-soft, #e6f1ee); }}
.listen:focus-visible {{ outline: 3px solid var(--accent, #0c6865); outline-offset: 2px; }}
.player {{ position: sticky; bottom: 0; z-index: 5; padding-bottom: env(safe-area-inset-bottom, 0px); border-top: 1px solid var(--line, #dde3e2); background: var(--paper, #fcfcfa); }}
.read-progress {{ height: 3px; background: var(--line, #dde3e2); }}
.read-progress div {{ width: 0; height: 100%; background: var(--accent, #0c6865); }}
.player-inner {{ display: flex; align-items: center; gap: .75rem; max-width: 42rem; margin: 0 auto; padding: .45rem 1.25rem; }}
.player audio {{ display: block; flex: 1; min-width: 0; height: 40px; margin: 0; }}
.read-label {{ flex: none; white-space: nowrap; color: var(--muted, #5d676c); font: 600 .8rem/1.3 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; font-variant-numeric: tabular-nums; }}
</style>
<div class="player">
  <div class="read-progress" aria-hidden="true"><div id="read-fill"></div></div>
  <div class="player-inner">
    <audio id="narration" controls preload="none" src="{audio_src}" data-total="{total}"></audio>
    <span class="read-label" id="read-label" aria-live="off">0% · {minutes(total)} left</span>
  </div>
</div>
<script>
(() => {{
  const audio = document.getElementById("narration");
  document.querySelectorAll("button.listen").forEach((btn) => {{
    btn.addEventListener("click", () => {{
      const start = Number(btn.dataset.start) || 0;
      const go = () => {{ audio.currentTime = start; audio.play().catch(() => {{}}); }};
      if (audio.readyState >= 1) go(); else {{ audio.addEventListener("loadedmetadata", go, {{ once: true }}); audio.load(); }}
    }});
  }});

  // Scroll progress: fill the bar above the player and show percent plus listening time left.
  const fill = document.getElementById("read-fill");
  const label = document.getElementById("read-label");
  const total = Number(audio.dataset.total) || 0;
  let queued = false;
  const update = () => {{
    queued = false;
    const doc = document.documentElement;
    const max = doc.scrollHeight - window.innerHeight;
    const pct = max > 0 ? Math.min(1, Math.max(0, window.scrollY / max)) : 1;
    fill.style.width = (pct * 100).toFixed(1) + "%";
    const left = Math.max(0, Math.round((total * (1 - pct)) / 60));
    label.textContent = Math.round(pct * 100) + "% · " + (left ? left + " min left" : "done");
  }};
  const onScroll = () => {{ if (!queued) {{ queued = true; requestAnimationFrame(update); }} }};
  window.addEventListener("scroll", onScroll, {{ passive: true }});
  window.addEventListener("resize", onScroll);
  update();
}})();
</script>
{PLAYER_END}"""
    page = page.replace("</article>", "</article>" + player, 1)
    return as_document(page)


def as_document(page):
    """Wrap a lesson fragment in a complete HTML document, so no host moves its <title> or stylesheet into <body>."""
    if re.match(r"\s*<!doctype", page, re.I):
        return page
    head, article, body = page.partition("<article")
    head = re.sub(r"<meta (charset|name=\"viewport\")[^>]*>\s*", "", head, flags=re.I).strip()
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f"{head}\n</head>\n<body>\n{article}{body.strip()}\n</body>\n</html>\n")


def main():
    args = sys.argv[1:]
    keep_audio = "--keep-audio" in args
    args = [a for a in args if a != "--keep-audio"]
    if len(args) != 1:
        sys.exit(__doc__)
    lesson = Path(args[0]).resolve()
    page = lesson.read_text()
    missing = [name for name, pattern in (("<article>", r"</article>"), ('<p class="standfirst">', r'<p class="standfirst">'), ("<h2> headings", r"<h2"))
               if not re.search(pattern, page)]
    if missing:
        sys.exit(f"{lesson.name} is missing {', '.join(missing)}; the narration buttons and player need them.")
    texts = section_texts(page)
    words = sum(len(t.split()) for t in texts)
    audio = lesson.parent / "audio" / f"{lesson.stem}.mp3"
    if keep_audio:
        starts = [float(x) for x in re.findall(r'class="listen" type="button" data-start="([0-9.]+)"', page)]
        if not audio.exists() or len(starts) != len(texts):
            sys.exit("--keep-audio needs the existing audio and one listen button per section; run without it.")
        total, voice = round(duration(audio), 2), "kept"
    else:
        starts, total, voice = narrate(texts, audio)
    lesson.write_text(inject(page, f"audio/{audio.name}", starts, total, words))
    print(json.dumps({"voice": voice, "audio": str(audio), "sections": len(texts), "words": words,
                      "starts": starts, "total": total, "mb": round(audio.stat().st_size / 1e6, 2)}))


if __name__ == "__main__":
    main()

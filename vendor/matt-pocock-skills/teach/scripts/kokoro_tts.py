"""Synthesize narration with the Kokoro neural voice model.

Called by narrate-lesson.py through uv, which supplies a compatible Python and
the kokoro package:

    (see narrate-lesson.py for the exact uv command)

job.json: {"voice": "af_heart", "speed": 1.0, "texts": [...], "outdir": "..."}
Writes <outdir>/<i>.wav (24 kHz mono) for each text, ending in a short pause.
"""
import json
import sys
from pathlib import Path

import numpy as np
import soundfile as sf
from kokoro import KPipeline

SAMPLE_RATE = 24000
PAUSE_SECONDS = 0.9


def main():
    job = json.loads(Path(sys.argv[1]).read_text())
    pipeline = KPipeline(lang_code="a", repo_id="hexgrad/Kokoro-82M")
    outdir = Path(job["outdir"])
    for i, text in enumerate(job["texts"]):
        chunks = [audio for _, _, audio in pipeline(text, voice=job["voice"], speed=job.get("speed", 1.0), split_pattern=r"\n+")]
        chunks.append(np.zeros(int(SAMPLE_RATE * PAUSE_SECONDS), dtype=np.float32))
        sf.write(outdir / f"{i}.wav", np.concatenate(chunks), SAMPLE_RATE)
        print(f"section {i + 1}/{len(job['texts'])}", file=sys.stderr, flush=True)


if __name__ == "__main__":
    main()

---
name: teach
description: Teach the user a new skill or concept, within this workspace.
disable-model-invocation: true
argument-hint: "What would you like to learn about?"
---

# Teach

Teach a topic across sessions in the current workspace. Ground every lesson in the user's mission and demonstrated understanding.

## Workspace records

Reach each format when creating or updating its record:

- `MISSION.md`: concrete purpose, success, and constraints. Use [MISSION-FORMAT.md](MISSION-FORMAT.md).
- `RESOURCES.md`: trusted knowledge sources and practitioner communities. Use [RESOURCES-FORMAT.md](RESOURCES-FORMAT.md).
- `learning-records/`: demonstrated insights, prior knowledge, and corrections. Read [LEARNING-RECORD-FORMAT.md](LEARNING-RECORD-FORMAT.md) when understanding is demonstrated, prior knowledge is disclosed, a misconception is corrected, or learning changes the mission; record qualifying insights then.
- `GLOSSARY.md`: understood terminology used consistently throughout the workspace. Use [GLOSSARY-FORMAT.md](GLOSSARY-FORMAT.md).
- `NOTES.md`: user preferences and working notes.
- `lessons/`: numbered HTML lessons, indexed in `lessons/README.md`.
- `reference/`: printable HTML references compressing reusable learning.
- `lessons/assets/`: shared styles and other reusable lesson components, kept beside the lessons so the same relative links work locally and when published.

## Select and teach

Teaching develops three different things: **knowledge** from trustworthy sources, **skills** through practice and feedback, and **wisdom** through real-world interaction with practitioners. Match the lesson strategy to what the learner actually needs.

Establish the mission before teaching if it is missing or unclear. Confirm changes to the mission and record their implications for future learning. Use learning records to infer the zone of proximal development when the user has not named a lesson.

Ground knowledge in high-trust resources rather than parametric guesses. Populate missing sources first and cite claims in lessons. Teach only the knowledge needed for the chosen skill, then give practice with a tight, preferably automatic feedback loop.

Choose skills by real practical use. Among skills within the learner's zone of proximal development, rank by how often the learner will actually use the skill in the situations listed under "Where I'll use it" in `MISSION.md`, and whether the goal can be accomplished without it. Break ties by cost of getting it wrong and by how many other skills it underpins. Favor what keeps paying off over the long run: first principles, judgment, and high-frequency building blocks such as core vocabulary, over facts that serve only one occasion, unless the mission itself centers on that occasion. Back the ranking with cited sources or practitioner communities; otherwise label it as practitioner judgment. Ask for those situations when none are recorded. Teach each skill to the depth the mission's situations and time horizon demand, and practice it in context: simulate the situations where it will be used, such as answering aloud for an interview, a real work task for a job, or the conversations the learner will actually have in a new language, adding realism as difficulty rises.

Aim for long-term storage strength, not just fluent immediate recall. Use retrieval practice, spacing, and interleaving related skills. Reduce difficulty during initial understanding; use desirable difficulty during practice.

## Teaching method

Use this method for every topic, weighting its parts by whether the target is knowledge, skill, or wisdom. For knowledge, the process is how to reason with the concept and the mastery check is explaining or applying it to a new case. For wisdom, the mastery check is a defended judgment call on a realistic case, followed by a pointer to practitioners who can critique it. The learner has ADHD: attention is the scarcest resource, so earn it through salience (stakes, story, a problem worth solving), not volume. Understanding means using the domain's reasoning and language to make and defend a decision. Reciting a definition is not evidence.

A lesson is one session of about 90 minutes that ends with the learner demonstrating the skill. The minutes below are rough guides. The lesson may open with quick retrieval of earlier material, then runs four parts in order:

1. **Concept and why (~15 min).** Open with a concrete situation where a real decision is on the line or something goes wrong, and say what happens without this skill. For a mechanism that misbehaves, lead with the failure. For a notation or structure, lead with its purpose and let failures appear later as consequences. Explain the underlying cause in plain words, then derive the rules from it. Rules compress the model; they never replace it.
2. **Problems and decisions (~20 min).** Map the two to four problem types the mission most needs and the decisions each one forces. For every decision, explain why it exists: what goes wrong when it is skipped or made badly. Name what a practitioner prioritizes, in ranked order and with reasons: the priorities that turn "it depends" into a decision. Cite them, or label them as practitioner judgment. When options compete, compare them on the factors that actually differ between them.
3. **Process (~15 min).** Give the repeatable sequence a practitioner follows to solve this type of problem, with each step naming the decision it settles. Walk through one worked example, narrating decisions, reasons, and tradeoffs as a practitioner would say them.
4. **Practice to mastery (~40 min).** Pose problems of rising difficulty. Collect the learner's answer before revealing any reference answer or rubric, then critique the reasoning: what they prioritized, what they missed, and how a practitioner would say it. Between problems, change one constraint so the learner sees which factor drives the decision. Finish with a mastery check: an unseen problem of the same type, solved with the process and without help, then the principle stated in a sentence or two (when it applies, what it trades away, how it fails). A pass qualifies for a learning record whose evidence notes a same-session check; delayed retrieval confirms it lasted. A miss names what the next session repairs.

Throughout, introduce each term when the story needs it, explained through the problem it names. A term is learned when the learner uses it correctly in their own reasoning.

Split a skill that does not fit one session. When a tangent uses up the time, move the mastery check to the next session. Parts 1–3 live in the lesson artifact. Part 4 needs the learner's own reasoning, so run it in conversation or as free-response prompts with hidden references. Never gate explanation behind a quiz; ask questions after the model is built.

Write parts 1–3 as narrative prose, like a strong long-form explanatory article: one continuous story that carries the concept, the decisions, and the process, with the causal links spelled out (because, so, which means). Encoding comes from that causal chain and from concrete stories, ideally from the learner's own experience as they have shared it (in `MISSION.md`, `NOTES.md`, learning records, or conversation) and never invented, not from memory devices. Let structure come from the story: use headings as article subheads, and use a table, list, or diagram only when it carries information prose cannot, such as several options compared across several factors. Avoid scaffolding that stands in for explanation, such as chips, badges, card grids, and labelled callout boxes.

Keep the load light and the pace lively: plain sentences; each paragraph advances one step of the story; never more than a few things for the learner to hold in mind at once; progress shown through subheads; varied activities in part 4. Follow the learner's curiosity when a tangent serves the mission, even if it departs from a planned sequence.

## Lesson artifact

Produce a focused HTML lesson with readable single-column article typography, sized for parts 1–3, for one tangible win tied to the mission, numbered `0001-<slug>.html` onward, following the teaching method. Link related lessons and references through anchors, recommend the best primary source to read or watch, and invite follow-up questions.

Narrate every lesson so it can be listened to away from a screen, unless `NOTES.md` opts out. Write the lesson as an `<article>` with a `<p class="standfirst">` summary under the title and `<h2>` section headings, then run `scripts/narrate-lesson.py <lesson.html>` from this skill before publishing. It writes one continuous audio file to `lessons/audio/<lesson>.mp3`, so playback survives a locked phone, and adds the lesson's total listening and reading time under the title, a listen button labelled with its length for the whole lesson and for each section, and a player pinned to the bottom of the page whose green scroll progress bar shows the percentage read and the time left. It also wraps the lesson in a complete HTML document (`<!doctype>`, `<head>` with the title and stylesheet, `<body>`), so hosts don't move head elements into the body. When only the page layout changes and the text does not, `--keep-audio` refreshes these without regenerating the audio. Publish that file at `audio/<lesson>.mp3` beside the page. If the script cannot run, say the lesson was not narrated; an updated lesson then keeps its old narration, which may no longer match the text.

Reuse existing assets before introducing new reusable components. Use a shared stylesheet so lessons form a consistent course. Choose structure that preserves the lesson's portability while sharing assets; repeated code belongs in assets rather than copied into each lesson.

Use quizzes, interactive tasks, or guided real-world practice. Retrieval questions come after the article, never inside it; the mastery check is free-response. Keep answer options parallel in length and formatting so presentation does not reveal the correct answer.

Create compact printable references for reusable knowledge as separate files, never inside a lesson, and adhere to established glossary terms. Open the finished lesson when possible and return its path. So the learner can open lessons on any device, also publish each new or updated lesson, and any existing lesson without a link in `lessons/README.md`, as a private page with its shared assets, unless `NOTES.md` opts out. If no artifact-publishing tool is available, say the lesson was not published. Update an existing published lesson in place so its link stays stable, point cross-lesson links at published pages, and keep one line per lesson (number, title, link) in `lessons/README.md`.

## Practitioner judgment

Answer questions that need experience, then direct the user toward reputable communities where real-world practice and feedback can build wisdom. Respect budget and recorded preferences against community participation.

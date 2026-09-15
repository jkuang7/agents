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
- `learning-records/`: demonstrated insights, prior knowledge, and corrections. Use [LEARNING-RECORD-FORMAT.md](LEARNING-RECORD-FORMAT.md).
- `GLOSSARY.md`: understood terminology used consistently throughout the workspace. Use [GLOSSARY-FORMAT.md](GLOSSARY-FORMAT.md).
- `NOTES.md`: user preferences and working notes.
- `lessons/`: numbered HTML lessons.
- `reference/`: printable HTML references compressing reusable learning.
- `assets/`: shared styles, widgets, and other reusable lesson components.

## Select and teach

Establish the mission before teaching if it is missing or unclear. Confirm changes to the mission and record their implications for future learning. Use learning records to infer the zone of proximal development when the user has not named a lesson.

Ground knowledge in high-trust resources rather than parametric guesses. Populate missing sources first and cite claims in lessons. Teach only the knowledge needed for the chosen skill, then give practice with a tight, preferably automatic feedback loop.

Aim for long-term storage strength, not just fluent immediate recall. Use retrieval practice, spacing, and interleaving related skills. Reduce difficulty during initial understanding; use desirable difficulty during practice.

## Lesson artifact

Produce a short, beautiful HTML lesson for one tangible win tied to the mission, numbered `0001-<slug>.html` onward. Keep typography readable and working-memory demands low. Link related lessons and references through anchors, recommend the best primary source to read or watch, and invite follow-up questions.

Reuse existing assets before introducing new reusable components. Use a shared stylesheet so lessons form a consistent course. Choose structure that preserves the lesson's portability while sharing assets; repeated code belongs in assets rather than copied into each lesson.

Use quizzes, interactive tasks, or guided real-world practice. Keep answer options parallel in length and formatting so presentation does not reveal the correct answer.

Create compact printable references for reusable knowledge and adhere to established glossary terms. Open the finished lesson when possible and return its path.

## Practitioner judgment

Answer questions that need experience, then direct the user toward reputable communities where real-world practice and feedback can build wisdom. Respect budget and recorded preferences against community participation.

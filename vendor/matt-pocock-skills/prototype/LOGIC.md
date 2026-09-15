# Logic prototype

Apply the common constraints and capture rules in [SKILL.md](SKILL.md). Build one shareable HTML/CSS/JS file that opens directly, without a framework, bundler, server, or external dependencies.

## Question and logic

State the explored model and question visibly at the top. Isolate the actual logic as a portable pure module independent of the DOM. Choose a reducer, state machine, pure functions, or state-owning module according to the question, rather than the page wiring. The page calls the logic through its interface.

## Demonstration

Write for a non-developer in domain language. Present:

1. Title and brief explanation of the question.
2. Full relevant state as readable labelled fields, refreshed after every action.
3. Free-play action buttons so users can explore arbitrary orders.
4. Tabbed guided scenarios with plain-language setup, what to watch, and real action buttons for each step. Reset to known initial state when starting a walkthrough.

Include the happy path and awkward or illegal transitions that expose assumptions. Use restrained typography, spacing, and one accent color so state and actions remain the focus.

Open or return the file for exploration, and extend scenarios as feedback reveals missing questions. When implementation adoption is authorized, retain the portable logic and keep the HTML shell on the captured throwaway branch. A walkthrough verdict does not replace production regression evidence.

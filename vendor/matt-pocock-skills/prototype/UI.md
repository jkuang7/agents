# UI prototype

Apply [SKILL.md](SKILL.md) common constraints and capture rules. Produce structurally different variants that the user can compare in real app context.

## Host and variants

Prefer the existing page or natural host section. Preserve its data fetching, parameters, and authorization; switch only rendering through `?variant=`. Create an obviously temporary route only when no suitable host exists, following repository routing conventions.

State the question and location. Default to three variants, with at most five. Vary layout, information hierarchy, and primary affordances, rather than colors or copy. Use the project's styling system. Share incidental elements when useful while keeping each layout free to differ.

## Switcher

Use one shared floating bottom-center switcher, visually distinct from the evaluated UI. Show the current variant key and name, with previous/next arrows that wrap. Update the URL so variants survive reload and can be shared. Support keyboard arrows without intercepting text editing. Hide the switcher in production builds.

Use read-only data or stub mutations. Return the URL and variant keys for comparison.

## Adoption

Capture the selected design and rationale, including a hybrid when useful. For authorized production adoption, apply normal implementation verification, remove losing variants and the switcher from main, and preserve the full exploration on the throwaway branch. Replace a temporary route with its real home when needed. Prototype constraints do not establish production correctness.

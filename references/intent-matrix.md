# Intent Matrix

Use this matrix as a starting point for asset type and placement. Route the task by objective with `references/scenario-matrix.md` before composing the prompt.

## Asset and surface starting points

| User outcome | Asset category | Prompt emphasis | Strong format defaults |
| --- | --- | --- | --- |
| Sell or clearly display a real item | E-commerce or product visual | subject fidelity, geometry, material, benefit visibility | 1:1 or 4:5 |
| Persuade, launch, or build brand memory | Campaign poster or key visual | concept, hero subject, visual metaphor, hierarchy | 4:5, 2:3, or 16:9 |
| Present a person or character | Portrait, talent, or character | identity cues, pose, expression, styling | 4:5, 3:2, 2:3, or 1:1 |
| Explain relationships or values | Infographic, diagram, or technical visual | data, labels, connectors, reading order | 16:9, 4:5, or A-series portrait |
| Show an interface or screen | UI, dashboard, or website visual | hierarchy, components, states, legible labels | 16:9, 4:5, or target screen ratio |
| Show a building or environment | Architecture, interior, or scene | perspective, scale, material, spatial logic | 16:9 or 4:5 |
| Express an artistic or editorial idea | Illustration, art print, or cover | medium, shape language, palette, concept | 1:1, 4:5, 2:3, or 16:9 |
| Change an existing image | Edit, restoration, or compositing | edit boundary, preservation, local continuity | Preserve source ratio unless changed |

## Objective selection

Use the objective route, not the asset label alone:

| If the task primarily requires... | Select |
| --- | --- |
| A real object, product, place, or material to stay accurate | Fidelity-first |
| A person or character to remain recognizable | Identity-first |
| Data, labels, UI states, or technical relationships to be correct | Information-first |
| A campaign or artwork to communicate a distinct idea | Concept-first |
| An environment or narrative moment to create a felt experience | Atmosphere-first |
| A bounded change to an existing image | Edit-first |

When goals overlap, select one primary objective and retain the others as secondary constraints. The primary objective determines the review rubric.

## Prompt anatomy by operation

### New generation

```text
Intent and asset type
Objective and success contract
Known subject or product facts
Must-preserve invariants
Creative variables
Scene and composition
Visual and material system
Exact text policy
Reference roles
Targeted constraints
```

### Reference-led generation

Assign each input a narrow role. Extract evidence relevant to that role before prompting. Do not use a product reference as permission to copy its background, or a style reference as permission to copy its subject identity.

### Edit

```text
Edit the supplied image.
Change only: [bounded visual change].
Preserve exactly: [identity, geometry, typography, framing, materials, and unaffected regions].
Do not: [specific undesired changes].
```

## Format selection

Choose the format from the placement surface first. A correct composition in the wrong format is not a usable asset. If the surface is unspecified, choose a common default and state the assumption in the direction section.

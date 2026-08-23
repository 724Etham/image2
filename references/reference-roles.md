# Reference Roles and Evidence Extraction

Assign every supplied image one role before using it. One image may have several useful details, but the prompt should state one primary role and keep the role boundary explicit.

## Roles

| Role | Use for | Prompt language |
| --- | --- | --- |
| Edit target | The user wants this image changed | `Edit the supplied image` |
| Product reference | The actual product, garment, package, object, or place must remain accurate | `Use the supplied image as a product reference only; preserve...` |
| Identity reference | A person or character must remain recognizable | `Use the supplied image as an identity reference; preserve...` |
| Composition reference | Framing, arrangement, camera, or spatial layout | `Use as a composition reference only; do not copy subject identity or product details` |
| Style reference | Palette, medium, texture, light, or rendering language | `Use as a style reference only; do not copy the subject or layout` |
| Material reference | Surface, weave, finish, transparency, reflection, or texture | `Use as a material reference only; preserve the requested subject and composition` |
| Result evidence | A prior output shown for evaluation or comparison | Do not use as a reference unless the user explicitly requests it |

## Evidence extraction

Before prompting with a reference, extract only evidence relevant to its role:

```text
Reference ID:
Primary role:
Must preserve:
Observed silhouette or geometry:
Observed color:
Observed material or surface:
Observed distinctive detail:
Observed proportion or identity cues:
Observed composition or layout cues:
Uncertain details:
Forbidden redesigns or substitutions:
```

Mark uncertain details as uncertain. Do not infer hidden construction, exact material composition, brand identity, or technical specifications from a single image.

## Product-reference gate

For a real product or garment, prioritize the following evidence in order:

1. Overall silhouette and proportion.
2. Distinctive construction and selling detail.
3. Color and material behavior.
4. Closures, seams, labels, and hardware.
5. Relationship between the product and the model or environment.

Keep the model, background, pose, and styling variable unless the user says they are also binding. Prohibit redesigns explicitly: do not move a closure, change a knot position, add pockets, alter the hem, invent a logo, or replace the material.

## Identity-reference gate

For a person or character, separate identity from the source image’s incidental styling:

- Preserve facial structure, skin tone, age range, hair pattern, distinctive marks, and requested body or character cues.
- Treat background, clothing, pose, and lighting as non-binding unless the user requests them.
- Do not promise an exact identity match before inspecting the output.

## Composition or style-reference gate

Do not let a composition or style reference change the requested product, person, or factual subject. State what the reference must not control. A style reference does not authorize copying a living artist’s identity or a protected brand campaign; translate the desired qualities into neutral visual attributes.

## Multiple references

Assign roles separately and avoid using a single image as authority for every property. Example:

```text
Image 1 is the product reference: preserve garment geometry and color.
Image 2 is the composition reference: use its camera height and subject placement only.
Image 3 is the material reference: use its matte woven surface only.
```

When references conflict, preserve the role with the highest priority for the selected objective and disclose the conflict. For fidelity-first work, product or identity evidence outranks style evidence. For concept-first work, confirmed product and brand facts still outrank a visual reference’s decorative details.

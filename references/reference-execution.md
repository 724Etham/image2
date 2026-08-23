# Reference Execution Protocol

A reference image is an input asset, not merely a sentence in the prompt. When one or more reference images are supplied, complete this protocol before writing the final prompt or making the image call.

## Reference manifest

Create a stable ordered manifest. The order in the manifest must match the order used in the actual image request.

```text
Reference manifest:
- Image 1: [role] | [accessible path] | [must preserve]
- Image 2: [role] | [accessible path] | [must preserve]
- Image 3: [role] | [accessible path] | [must preserve]
```

Valid primary roles are `edit target`, `product reference`, `identity reference`, `composition reference`, `style reference`, `material reference`, and `result evidence`.

## Role mapping

| Role | What the model may take from it | What the model must not take unless requested |
| --- | --- | --- |
| Edit target | The image being modified and its unaffected regions | A new composition or unrelated redesign |
| Product reference | Product geometry, color, material, construction, and distinctive detail | Its background, crop, model, lighting, or branding |
| Identity reference | Face, body, hair, age cues, distinctive marks, or character traits | Its incidental background, clothing, or pose |
| Composition reference | Framing, camera height, scale, arrangement, and negative-space logic | Subject identity, product design, or factual content |
| Style reference | Palette, medium, texture, lighting language, and rendering behavior | Protected artist or brand identity, subject, or exact layout |
| Material reference | Surface, weave, finish, transparency, reflectivity, and texture behavior | Its product shape, composition, or object identity |
| Result evidence | A prior result’s strengths and failures for evaluation | Automatic continuity or copied content |

## Evidence extraction

Extract only evidence relevant to each role. Mark uncertain observations as assumptions. Do not convert visual guesses into factual specifications.

```text
Reference ID:
Primary role:
Observed and confirmed:
Must preserve:
May borrow:
Must not copy:
Uncertain or not visible:
Likely failure if ignored:
```

For product references, record silhouette, color, material, construction, distinctive detail, proportion, labels or hardware, and forbidden redesigns. For identity references, record facial structure, hair, skin tone, age range, body cues, distinctive marks, and identity drift risks. For composition or style references, record camera, layout, palette, lighting, medium, and what must remain independent.

## Actual handoff requirement

The final generation or editing request must contain the actual accessible image files in its reference input. A path, filename, or description written only inside the prose prompt does not use the image.

Use the same ordering in both places:

```text
Prompt mapping:
- Image 1 is the edit target. Preserve its crop, framing, and unaffected areas.
- Image 2 is the product reference. Use it only to preserve garment geometry and material truth.
```

```text
Actual reference input:
references = [Image 1 path, Image 2 path]
```

If the provider uses a separate source-image field for edits, put the edit target in that field and pass additional references in the provider’s supported reference list. Document the mapping in the execution notes.

## Missing or inaccessible references

If the user refers to a reference that is not attached or cannot be opened:

1. Do not claim that the reference was used.
2. Ask for the missing file when it would change an invariant or identity decision.
3. If proceeding without it is safe, state that the result will be reference-free and label any replacement details as assumptions.
4. Never invent product labels, material specifications, identity traits, logos, or exact construction from an unavailable reference.

## Conflicting references

When references conflict, do not average them silently. Identify the conflict and apply the primary objective hierarchy:

- Fidelity-first: product or factual evidence outranks style and composition references.
- Identity-first: identity evidence outranks clothing, background, and style references.
- Information-first: source data and structural logic outrank decorative references.
- Concept-first: confirmed brand or product facts remain binding; style references may influence only the creative layer.
- Edit-first: the edit target and its preservation list outrank all secondary references.

If the conflict changes the route or invariant set, ask one focused question before generating.

## Reference-present preflight

Before generation or editing, confirm:

- Every supplied image has one primary role.
- The manifest order matches the actual reference input order.
- Evidence has been extracted for each role.
- The prompt names each image by the same stable number.
- The edit target is not confused with a product, style, or result reference.
- No unavailable reference is presented as used.
- The output review includes reference fidelity as a criterion.

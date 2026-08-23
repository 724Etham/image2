---
name: gpt-image-2-production-director
description: Production-grade direction for GPT-Image-2 image generation and editing across e-commerce, campaigns, portraits, products, packaging, social media, UI, diagrams, architecture, illustration, and controlled edits. Use when a brief needs task routing, fact and assumption separation, reference handling, a precise prompt, version tracking, or scenario-specific quality review.
---

# GPT-Image-2 Production Director

## Mission

Direct image work as a **task-specific production system**, not as a generic collection of style adjectives. Route the brief to the correct objective, separate what must remain true from what may be invented, compile a concise prompt, track its version, and judge the result with the correct scenario rubric.

> The universal rule is not “make it beautiful.” It is “preserve or express the right thing for the requested task.”

## Operating model

Run this sequence:

1. Identify the operation: `generate`, `reference-led`, or `edit`.
2. Identify the asset and intended surface.
3. Route the task to one primary objective mode.
4. Build a brief with facts, invariants, variables, assumptions, and risks.
5. Define the first-glance target and the success contract.
6. Select the scenario contract and rubric from the references.
7. Compose one prompt with the correct constraints and reference roles.
8. Assign a prompt version and save a ledger record when the work is iterative or commercial.
9. Run preflight checks.
10. Generate or deliver the prompt as requested.
11. Inspect the result using the selected rubric.
12. Change one causal variable per iteration and record the change.

When the user asks only for a prompt, provide the direction and prompt; do not generate an image unless generation is explicitly requested.

## 1. Identify the operation and input provenance

Choose exactly one primary operation:

- **Generate:** create a new image from a verbal brief.
- **Reference-led:** create a new image guided by one or more references.
- **Edit:** modify a supplied image within an explicit boundary.

Classify every supplied image with one narrow role:

| User intent or input | Role |
| --- | --- |
| The user asks to change the supplied image | Edit target |
| The user wants its arrangement or framing | Composition reference |
| The user wants its rendering, palette, or medium | Style reference |
| The user wants the same person or character | Identity reference |
| The supplied image is the actual product, garment, package, or object | Product reference |
| The user shows an earlier generated result for evaluation | Result evidence, not automatically a reference |

If the user requests an earlier prompt version, restore that version instead of silently improving it. Read `references/versioning.md` for version rules. Read `references/reference-roles.md` before using complex or multiple references.

Do not turn an edit into a new generation. Do not copy a reference merely because it is available. Preserve the requested role boundary.

## 2. Route the task by objective

Classify the task by its **primary objective**, not just by its visual category. Use the first matching rule in this order:

1. **Edit-first:** the user wants a bounded change to an existing image.
2. **Fidelity-first:** a real product, garment, package, place, object, or material must remain accurate.
3. **Identity-first:** a person or character must remain recognizable and consistent.
4. **Information-first:** data, labels, component relationships, UI states, connectors, or technical structure must be accurate.
5. **Concept-first:** a campaign, advertisement, poster, cover, or artwork must communicate a differentiated idea.
6. **Atmosphere-first:** the main goal is mood, environment, spatial experience, or narrative scene.

If two objectives apply, choose one primary mode and one secondary constraint. For example, a product launch poster with a supplied garment is `Fidelity-first` with a `Concept-first` secondary layer; a brand poster without a real product is `Concept-first`; a shopping image of a supplied garment is `Fidelity-first` even if the background is fashionable.

Read `references/scenario-matrix.md` for the route table, asset categories, default formats, and priority rules. Read `references/prompt-contracts.md` for the selected mode and asset type. Read `references/review-rubrics.md` for scoring.

## 3. Build the production brief

Separate the brief into five layers:

| Layer | Definition | Rule |
| --- | --- | --- |
| Known facts | User-provided or researched information | Preserve; never embellish as fact |
| Invariants | Details that must not change | Repeat in the prompt and review checklist |
| Creative variables | Details the director may choose | Use only when they serve the objective |
| Assumptions | Unprovided details needed to proceed | Label explicitly to the user |
| Risks | Likely failure modes | Convert into targeted constraints or workflow steps |

Use this internal schema:

```text
Task objective:
Asset and surface:
Primary mode:
Secondary constraint:
Known facts:
Invariants:
Creative variables:
Assumptions:
First-glance target:
Required text:
Reference roles:
Main risks:
Prompt version:
```

For a missing detail, ask one focused question only when its answer would change the route or the invariant set. Otherwise choose the smallest reasonable assumption and disclose it. Never invent real brand facts, product specifications, labels, logos, locations, history, or legal claims.

## 4. Define the success contract

Write one sentence that states what success means for the selected objective:

> **The viewer should [notice / understand / feel / verify] [specific result] while [critical constraint] remains true.**

Examples:

- **Fidelity-first:** The viewer should verify the skirt’s right-hip knot and asymmetric hem while the supplied garment’s geometry and color remain unchanged.
- **Concept-first:** The viewer should understand the campaign idea without the headline while the visual remains specific to the brand or product.
- **Information-first:** The viewer should follow the data or system relationship without ambiguity while labels and connectors remain accurate.
- **Identity-first:** The viewer should recognize the same person or character in a new setting while identity traits remain stable.
- **Edit-first:** The viewer should see only the requested change while all unaffected regions remain unchanged.

Do not force a concept-first requirement onto fidelity-first or information-first tasks. Do not force exact product preservation onto open-ended art unless the user requests it.

## 5. Lock invariants and variables

Before writing the prompt, create three lists:

| List | Purpose |
| --- | --- |
| **Must preserve** | Facts, geometry, identity, text, structure, or regions that cannot change |
| **May change** | Model, styling, background, lighting, camera, palette, or composition choices |
| **Must not introduce** | Common model errors, redesigns, extra objects, false labels, or unwanted edits |

For supplied references, extract evidence before prompting. Read `references/reference-roles.md` and record silhouette, color, material, construction, distinctive detail, proportion, identity cues, layout logic, and forbidden redesigns as applicable.

For e-commerce and real-product tasks, use the actual product’s geometry as the primary memory point. For concept-first tasks, use one dominant visual idea and one visible differentiator. For information-first tasks, use data relationships and reading order as the memory point. For identity-first tasks, use stable facial, body, costume, or character cues.

## 6. Build a causal visual chain

Map the selected objective to visible decisions:

```text
Task objective
  -> first-glance target
  -> invariant or core idea
  -> subject treatment
  -> composition and scale
  -> light, material, or rendering
  -> background or supporting elements
  -> text and viewer action
```

Every major element must support one link in this chain. Delete props, effects, colors, or scenery that only make the image look attractive without helping the task. Use one decisive visual anchor and a restrained style budget; do not solve weak direction by adding synonyms.

## 7. Compile the prompt

Use this order, adapting the fields to the routed objective:

1. Intent, asset type, surface, and prompt version.
2. Objective and success contract.
3. Known subject or product facts.
4. Must-preserve invariants.
5. Creative variables and their visual role.
6. Scene, composition, camera, and reading order.
7. Material, lighting, color, and rendering logic.
8. Exact in-image text and typography rules, if required.
9. Reference roles and evidence constraints.
10. Targeted avoid-list and output constraints.

Use concrete nouns and verbs. Keep one style anchor, one coherent palette, one main lighting logic, and only the negative constraints that prevent likely failure. Remove filler such as “8K,” “masterpiece,” “best quality,” or “trending on ArtStation.”

For image-generation calls, write the actual tool prompt in English even when the user-facing explanation is in another language. Preserve required in-image text in its original language. Do not promise perfect text rendering or exact pixel preservation before inspection.

Use this generic scaffold only after routing:

```text
Create a [asset type] for [surface and audience].
Prompt version: [V-number].

Objective: [primary objective and first-glance target].
Success contract: [what must be noticed, understood, felt, or verified].

Known subject or product facts: [confirmed facts only].
Must preserve: [invariants].
Creative variables: [chosen variables and why they support the objective].

Scene and composition: [format, framing, subject placement, scale, negative space, and reading order].
Visual system: [one style anchor, palette, lighting logic, and material or rendering behavior].

Text, verbatim and exactly once: [required strings and hierarchy]. Add no other text.
References: [role and evidence for each supplied image].

Avoid: [targeted failure modes and unwanted additions].
```

## 8. Scenario contracts

Use the appropriate contract rather than applying one universal prompt style:

- **Fidelity-first / e-commerce:** preserve product geometry, color, material, labels, proportions, and selling details; keep styling subordinate; usually prefer clean background and clear product visibility; prohibit redesign.
- **Concept-first / campaign:** preserve confirmed product and brand facts, then develop one differentiated concept with a visible subject memory point and a spatial or lighting metaphor.
- **Identity-first / portrait:** preserve identity cues, age, expression range, body proportions, and requested styling; vary setting and pose only within the identity brief.
- **Information-first / UI, diagram, infographic:** prioritize hierarchy, labels, connectors, states, values, and reading path; use structured or programmatic rendering when exactness exceeds image generation reliability.
- **Atmosphere-first / scene, architecture, lifestyle:** prioritize space, scale, material, light direction, camera, and narrative action; preserve real-world facts when the place or object is named.
- **Edit-first:** state the change boundary first, preserve all unaffected regions, and use the smallest possible edit scope.

Read `references/prompt-contracts.md` for detailed field requirements and scenario-specific examples.

## 9. Text and typography policy

Decide whether text belongs in the generated image:

| Text need | Default handling |
| --- | --- |
| No text required, such as a product main image | Prohibit all text |
| Short campaign headline | May generate; inspect exactly |
| Long copy, price, size, specifications, or legal text | Generate the visual first and typeset afterward |
| Data labels, UI content, or technical annotations | Use structured rendering or programmatic layout when exactness matters |
| Logo, trademark, packaging label, or regulated claim | Use supplied brand assets or post-production; do not invent |

Quote every required in-image string verbatim exactly once. When the task requires multiple text elements, specify hierarchy and placement. Prohibit extra words, random symbols, duplicate text, watermarks, and false labels.

## 10. Reference and edit gates

Read `references/reference-roles.md` for evidence extraction and `references/operation-gates.md` for research, edit boundaries, and provider-neutral cautions.

For edits, begin with:

```text
Edit the supplied image.
Change only: [bounded visual change].
Preserve exactly: [identity, geometry, typography, framing, materials, and all unaffected regions].
Do not: [specific undesired changes].
```

### Local edit distillation rule

When the user requests one or two bounded refinements to an existing image and wants the current image preserved, use **local edit distillation** instead of re-distilling the whole creative direction.

1. Keep the original operation, asset, surface, crop, framing, camera, background, lighting, and product or identity direction unless the user explicitly changes one.
2. Write `Change only these variables:` and enumerate no more than two causal changes. Separate each change from the preservation list.
3. Inherit the parent prompt version and create a minor revision such as `V2.3` or `V2.4`; record the exact changed variables and reason in the ledger.
4. Use physically precise language for the target change. Prefer `low-profile`, `broad`, `soft`, and `shallow natural volume` over an ambiguous instruction such as `make it flat` when some three-dimensional depth must remain.
5. If there are multiple images, identify the edit target and each reference role explicitly. Use a product reference only to judge product truth; do not copy its framing, background, or lighting unless requested.
6. Do not add new concepts, styling, props, text, or “improvements” unrelated to the bounded change.
7. Review the result with the Edit-first rubric. Re-route the task only when the edit boundary is unclear, reference roles conflict, the requested change alters the core subject, or the same failure persists across iterations.

Use this local-edit structure:

```text
Edit the supplied image.
Prompt version: [minor revision].
Parent version: [locked parent version].

Primary objective: [fidelity or edit objective].
Change only these variables:
1. [bounded change]
2. [bounded change, if needed]

Preserve exactly: [crop, framing, camera, subject geometry, color, lighting, background, shadows, proportions, and all unaffected areas].

Targeted correction: [precise physical description of the desired local result].
Reference roles: [edit target and product, identity, style, or material references].

Do not: [redesigns, new objects, extra text, unrelated style changes, or artifacts].
```

For real or named places, products, historical subjects, technical objects, or culturally specific materials, research when fidelity matters. Do not fill missing facts with invented labels, logos, history, or product details.

## 11. Versioning and iteration

Assign `V1` to the first locked prompt. Increment only after a deliberate change. For iterative or commercial work, save a ledger record using `references/versioning.md`.

When revising, classify the failure before changing anything:

| Failure | Correct action |
| --- | --- |
| Wrong text, anatomy, geometry, or missing object | Fix the relevant technical constraint or reference role |
| Attractive but generic | Change the concept or memory point, not the adjective list |
| Correct subject, weak hierarchy | Change scale, placement, negative space, or reading order |
| Correct concept, wrong mood | Change one lighting, palette, material, or camera variable |
| Real product or place inaccurate | Improve evidence extraction or research; do not invent details |
| Correct image, wrong requested version | Restore the locked version exactly |
| Same failure across iterations | Change the workflow or model strategy, not just the wording |

Change one causal variable per iteration and record `Changed from [version]: [variable]` plus the reason. Lock successful directions before exploring variations.

## 12. Preflight and result review

Before generating or delivering a prompt, verify:

1. Operation, asset, surface, format, and primary objective are explicit.
2. Known facts, invariants, variables, assumptions, and risks are separated.
3. The success contract is specific and appropriate to the objective.
4. The reference roles are explicit and evidence has been extracted when needed.
5. The prompt contains one clear visual anchor or reading path.
6. Required text is quoted verbatim exactly once, or text is intentionally prohibited.
7. The prompt version is recorded and an earlier version has not been silently rewritten.
8. The avoid-list targets likely errors without becoming a contradictory style pile.

After generation, inspect the rendered file on two axes:

- **Technical:** text, geometry, identity, anatomy, materials, framing, reference fidelity, extra objects, watermarks, and file format.
- **Task success:** the correct first-glance target, objective-specific memory point, reading path, and suitability for the intended surface.

Use the dynamic rubric in `references/review-rubrics.md`. A result is not complete merely because it is attractive. If the selected rubric fails its highest-weight criterion, revise that criterion first.

## Output contract

Return the following in the user’s language:

1. **Direction:** asset, surface, format, operation, primary objective, secondary constraint, success contract, known facts, assumptions, invariants, prompt version, and open decisions.
2. **Copyable prompt:** one complete prompt with no unexplained placeholders.
3. **Execution notes:** reference roles, research needs, text post-production advice, version history, and edit-preservation rules when relevant.
4. **Verification checklist:** three to six criteria tied to the selected objective, including technical and task-success checks.
5. **Result diagnosis:** after generation, report the selected rubric, score or pass/fail judgment, failure category, and the single next variable if iteration is needed.

If the user asks for several concepts, keep the asset and objective stable while varying the concept, subject treatment, palette, composition, or scene. Offer no more than three directions. If the user asks for one prompt, choose one route decisively.

## Resource routing

- Read `references/scenario-matrix.md` for objective routing, asset categories, formats, and priority rules.
- Read `references/prompt-contracts.md` for scenario-specific prompt fields and examples.
- Read `references/review-rubrics.md` for dynamic scoring and failure thresholds.
- Read `references/reference-roles.md` for reference classification and evidence extraction.
- Read `references/versioning.md` for Prompt Ledger records, restoration, and iteration history.
- Read `references/intent-matrix.md` for the legacy asset-format starting point when routing is uncertain.
- Read `references/operation-gates.md` for research decisions, edit boundaries, and provider-neutral cautions.
- Read `references/sources.md` only when reporting upstream sources or updating this skill.
- Run `scripts/route_brief.py` for an unusually short or ambiguous brief when a deterministic first-pass route is useful.

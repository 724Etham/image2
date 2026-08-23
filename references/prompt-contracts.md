# Prompt Contracts

Use one contract after routing. A contract is a constraint profile, not a fixed prose template. Fill only the fields relevant to the task.

## Shared contract fields

Every contract should specify:

```text
Objective:
First-glance target:
Known facts:
Must preserve:
May change:
Must not introduce:
References and evidence:
Text policy:
Output surface and format:
Selected review rubric:
```

## Fidelity-first contract

Use for e-commerce listings, product photography, packaging, real products, named places, and any task where the subject must remain accurate.

**Required fields:** product or subject identity, geometry or silhouette, color, material, distinctive details, proportions, reference role, forbidden redesigns, and the exact first-glance selling or verification target.

**Prompt order:** identify the real subject; state that the reference is a product reference; list immutable details; define the model, styling, scene, and camera as variables; describe the cleanest composition for verification; prohibit redesigns and false labels.

**Default rule:** creative styling is subordinate to subject fidelity. If a detail cannot be verified, label it as an assumption rather than a product fact.

**E-commerce checks:** product geometry, color, material, selling detail visibility, size or scale cues, unobstructed view, realistic fit, correct aspect ratio, no extra text unless requested, no price or false claims.

## Concept-first contract

Use for campaigns, advertising, posters, covers, brand key visuals, and open-ended art where the viewer must understand or feel an idea.

**Required fields:** audience, brand position or artistic intention, one-sentence proposition, one visible subject memory point, one spatial or lighting metaphor, reading order, and any required headline.

**Prompt order:** state the campaign idea; select one hero subject; make the memory point visible; make the environment or lighting prove the idea; reserve deliberate text space; keep style language to one anchor and a small supporting vocabulary.

**Default rule:** the image must still communicate the idea after removing the headline. Do not add generic luxury or cinematic adjectives to compensate for a weak concept.

**Campaign checks:** concept recognizability, subject memory point, brand or artistic distinctiveness, hierarchy, text usability, and technical integrity.

## Identity-first contract

Use for portraits, recurring characters, talent continuity, avatars, and identity-preserving transformations.

**Required fields:** identity reference role, stable facial and body cues, age range when relevant, hairstyle, costume or character invariants, acceptable expression range, pose and scene variables, and forbidden identity drift.

**Prompt order:** establish identity invariants; state the desired pose, wardrobe, camera, and environment; preserve facial structure and distinguishing cues; control retouching; prohibit additional people or identity substitutions.

**Default rule:** do not introduce a new creative feature that changes the recognizable identity. When a supplied image is the identity reference, do not treat its background or clothing as automatically binding.

**Portrait checks:** identity consistency, anatomy, expression, skin and hair realism, costume continuity, pose, framing, and unwanted age or feature drift.

## Information-first contract

Use for infographics, diagrams, flowcharts, technical visuals, UI mockups, dashboards, document illustrations, and data-driven imagery.

**Required fields:** source values or facts, reading order, node and connector logic, labels, component states, scale or unit conventions, layout grid, and output text policy.

**Prompt order:** define the information task; enumerate entities and relationships; specify reading order and label hierarchy; define layout, connectors, and state changes; use a restrained visual style only after the structure is fixed.

**Default rule:** correctness outranks atmosphere. For dense labels, exact values, or complex connectors, use structured or programmatic rendering when the image model cannot reliably guarantee them.

**Information checks:** factual accuracy, labels, connectors, hierarchy, reading path, state or unit consistency, legibility, and absence of invented data.

## Atmosphere-first contract

Use for lifestyle scenes, architecture, interiors, environments, narrative frames, and visual concepts where spatial or emotional experience is primary.

**Required fields:** viewer experience, setting, scale, camera position, spatial relationships, materials, lighting direction, action or story signal, and real-world facts when named.

**Prompt order:** state the experience; define the space and its geometry; establish camera and scale; define light and material behavior; add only actions or props that reinforce the scene.

**Default rule:** every environmental element must support the intended mood, spatial logic, or narrative beat. Avoid prop accumulation.

**Atmosphere checks:** mood, space and scale, perspective, material behavior, lighting logic, story signal, and unintended clutter.

## Edit-first contract

Use whenever the user asks to modify an existing image.

**Required fields:** edit target, exact change boundary, preserve list, forbidden side effects, mask or local region if available, and the unchanged output ratio unless the user asks for a change.

**Prompt order:** begin with `Edit the supplied image`; state `Change only`; state `Preserve exactly`; state `Do not`; describe only the affected region and the desired change.

**Default rule:** do not re-describe the whole image and do not introduce unrelated improvements. Use the smallest possible edit scope.

**Edit checks:** requested change, unaffected-region preservation, identity or geometry preservation, typography preservation, edge and material continuity, and absence of new artifacts.

## Secondary constraints

When a task combines goals, keep one primary contract and add one or more secondary constraints:

| Combination | Primary | Secondary |
| --- | --- | --- |
| Product launch using a real garment | Fidelity-first | Concept-first |
| Portrait in a cinematic location | Identity-first | Atmosphere-first |
| Branded technical diagram | Information-first | Concept-first or brand styling |
| Product packshot with a dramatic set | Fidelity-first | Atmosphere-first |
| Advertising image with a supplied model | Concept-first | Identity-first |
| Image edit with a new color treatment | Edit-first | Atmosphere-first or Concept-first |

Secondary constraints may influence styling, but they must never override the primary contract’s invariants.

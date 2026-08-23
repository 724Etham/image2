# Review Rubrics

Use a 1–5 score for each dimension. Select the rubric that matches the primary objective. Adjust weights only when the user states a different priority.

A result passes when its weighted score is at least 4.0/5 and no critical dimension is below 3. For high-risk commercial, legal, technical, or identity work, require at least 4 on every critical dimension.

## Fidelity-first rubric

Use for e-commerce, product references, packaging, real locations, and real objects.

| Dimension | Default weight | Critical? |
| --- | ---: | :---: |
| Subject geometry and identity | 30% | Yes |
| Color, material, and surface behavior | 20% | Yes |
| Distinctive selling or verification detail | 20% | Yes |
| Visibility, scale, and framing | 15% | Yes |
| Scene restraint and realism | 10% | No |
| Technical integrity and text policy | 5% | No |

**Pass question:** Can the viewer verify the real subject without the image inventing or hiding a meaningful detail?

For an e-commerce garment image, score the actual silhouette, construction, color, drape, hem, closures, fit, and unobstructed selling details. Do not deduct for a lack of abstract brand concept if the task is product listing fidelity.

## Concept-first rubric

Use for brand campaigns, advertising, posters, covers, and open-ended art with a communication goal.

| Dimension | Default weight | Critical? |
| --- | ---: | :---: |
| Concept recognizability without headline | 25% | Yes |
| Subject or brand memory point | 25% | Yes |
| Distinctiveness and non-substitutability | 20% | Yes |
| Composition, hierarchy, and surface fit | 15% | Yes |
| Visual system and emotional coherence | 10% | No |
| Technical integrity and text | 5% | No |

**Pass question:** Would the concept remain recognizable if the headline, model, or logo were removed or replaced?

Run the substitutability test: if three other brands could use the same image by changing only the logo, the result is under-differentiated. Revise the concept or memory point, not the adjective list.

## Identity-first rubric

Use for portraits, avatars, characters, talent continuity, and identity-preserving transformations.

| Dimension | Default weight | Critical? |
| --- | ---: | :---: |
| Face and identity consistency | 35% | Yes |
| Body, age, and distinctive feature continuity | 20% | Yes |
| Anatomy, hands, and pose | 20% | Yes |
| Expression, styling, and requested role | 15% | Yes |
| Lighting, framing, and technical integrity | 10% | No |

**Pass question:** Would a reasonable viewer recognize the same person or character in the new image?

Do not trade identity consistency for more dramatic styling. If identity is wrong, the image fails even when the composition is attractive.

## Information-first rubric

Use for diagrams, flowcharts, infographics, dashboards, UI, manuals, and technical visuals.

| Dimension | Default weight | Critical? |
| --- | ---: | :---: |
| Data, facts, and values | 30% | Yes |
| Relationship, connector, and state logic | 25% | Yes |
| Reading order and hierarchy | 20% | Yes |
| Text and label legibility | 15% | Yes |
| Visual consistency and restraint | 5% | No |
| Technical integrity | 5% | No |

**Pass question:** Can the intended information be followed without ambiguity or invented content?

When exact text, values, or geometry exceed reliable image generation, switch to structured or programmatic rendering and use the generated image only for visual reference.

## Atmosphere-first rubric

Use for environments, interiors, architecture concepts, lifestyle scenes, and narrative frames.

| Dimension | Default weight | Critical? |
| --- | ---: | :---: |
| Intended mood or experience | 25% | Yes |
| Spatial logic, scale, and perspective | 25% | Yes |
| Light, material, and surface behavior | 20% | Yes |
| Narrative or action signal | 15% | No |
| Composition and surface fit | 10% | No |
| Technical integrity | 5% | No |

**Pass question:** Does the viewer enter the intended space or emotional moment without the scene losing physical credibility?

For named places or real-world architecture, factual accuracy becomes a critical secondary constraint and may require research.

## Edit-first rubric

Use for edits, replacements, removals, recolors, restoration, and localized changes.

| Dimension | Default weight | Critical? |
| --- | ---: | :---: |
| Requested change is correct | 30% | Yes |
| Unaffected region preservation | 30% | Yes |
| Identity, geometry, and typography continuity | 20% | Yes |
| Edge, lighting, and material integration | 15% | Yes |
| File and output integrity | 5% | No |

**Pass question:** Is the requested change visible while everything outside the edit boundary remains as intended?

## Risk modifiers

Increase the weight or failure threshold for these dimensions when applicable:

| Risk signal | Modifier |
| --- | --- |
| User supplied the actual product or garment | Make geometry and distinctive detail critical |
| User supplied an identity reference | Make identity consistency critical |
| Exact numbers, labels, or technical connectors | Make facts and logic critical; consider structured rendering |
| Long or legally important text | Move typography to post-production unless exact rendering is verified |
| Multiple output images need to match | Add series consistency as a critical dimension |
| Real place, historic subject, or cultural material | Require research and factual review |
| Edit request affects a small region | Increase unaffected-region preservation weight |

## Result diagnosis

After scoring, classify the main failure:

| Pattern | Diagnosis | Next action |
| --- | --- | --- |
| Low critical technical dimension | Technical failure | Change only the relevant constraint, reference role, or rendering method |
| High technical score, low concept score | Creative under-distillation | Change the proposition or subject memory point |
| High concept score, low fidelity score | Creative direction overrode the subject | Reinstate invariants and strengthen product or identity references |
| Good single image, inconsistent series | Continuity failure | Lock identity, product, palette, camera, and version records |
| Repeated same failure | Strategy failure | Change the workflow, reference, or tool route instead of expanding the prompt |

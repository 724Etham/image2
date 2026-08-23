# Scenario Matrix

Use this file to route a brief before composing a prompt. Select one primary objective and, when necessary, one secondary constraint. Do not apply all rows at once.

## Objective modes

| Primary mode | Use when | First-glance target | Protect first |
| --- | --- | --- | --- |
| Fidelity-first | A real product, garment, package, place, object, or material must remain accurate | Verify the real subject | Geometry, color, material, label, proportion, or factual detail |
| Concept-first | A campaign, advertisement, poster, cover, or artwork must communicate an idea | Understand or feel the concept | Concept, visual metaphor, brand or subject memory |
| Information-first | A diagram, infographic, technical visual, UI, or data-driven image must explain relationships | Follow the information path | Values, labels, connectors, hierarchy, states, and reading order |
| Identity-first | A person, character, or recurring figure must remain recognizable | Recognize the same identity | Face, body, costume, character cues, and continuity |
| Atmosphere-first | The main goal is mood, environment, lifestyle, or narrative space | Feel or enter the scene | Scale, light, material, spatial logic, and action |
| Edit-first | The user asks to change an existing image | See only the requested change | Edit boundary and all unaffected regions |

## Routing precedence

Use the first applicable rule:

1. A bounded change to an existing image means `Edit-first`.
2. A supplied real product, place, package, object, or material that must remain true means `Fidelity-first`.
3. A supplied person or character that must remain recognizable means `Identity-first`.
4. Exact data, labels, UI states, technical structure, or connector relationships mean `Information-first`.
5. A campaign, advertising, poster, cover, or open-ended art brief means `Concept-first`.
6. An open scene, environment, or lifestyle brief without a stronger constraint means `Atmosphere-first`.

If several rules apply, keep only one primary mode. Add the others as secondary constraints. Examples:

- A product launch poster using an actual garment: `Fidelity-first` primary, `Concept-first` secondary.
- A brand poster without a real product: `Concept-first` primary.
- A portrait in a new location using a face reference: `Identity-first` primary, `Atmosphere-first` secondary.
- A technical product diagram with a brand style: `Information-first` primary; brand styling is secondary.

## Asset and surface defaults

| Asset category | Common surfaces | Strong format defaults | Typical route |
| --- | --- | --- | --- |
| E-commerce product or garment | Listing image, product detail, catalog | 1:1 or 4:5; use the actual store requirement | Fidelity-first |
| Brand poster or campaign key visual | Social, print, retail, website | 4:5, 2:3, or 16:9 according to placement | Concept-first |
| Portrait or character | Profile, editorial, campaign, character sheet | 4:5, 3:2, 2:3, or 1:1 | Identity-first |
| Product photography or packaging | Product page, sell sheet, packaging | 4:5 or 1:1 | Fidelity-first |
| Social content | Feed, story, reel cover, thumbnail | 4:5, 9:16, or 16:9 | Route by purpose |
| UI or web visual | Website, app, dashboard, prototype | 16:9, 4:5, or target screen ratio | Information-first |
| Infographic or technical diagram | Report, presentation, manual | 16:9, 4:5, or A-series portrait | Information-first |
| Architecture or interior | Presentation, portfolio, concept board | 16:9 or 4:5 | Atmosphere-first or Fidelity-first |
| Illustration or art print | Editorial, poster, collection, print | 1:1, 4:5, 2:3, or 16:9 | Concept-first or Atmosphere-first |
| Controlled edit or restoration | Existing image surface | Preserve source ratio unless changed | Edit-first |

These are starting points, not hard requirements. Follow the user’s target surface whenever it is specified.

## Route-specific questions

Ask only the highest-value missing question:

| Route | Highest-value question |
| --- | --- |
| Fidelity-first | What must remain exactly accurate in the supplied product or subject? |
| Concept-first | What should the viewer remember after the headline is removed? |
| Information-first | What is the required reading order or relationship structure? |
| Identity-first | Which identity traits must remain stable across the new image? |
| Atmosphere-first | What mood or spatial experience should the viewer enter? |
| Edit-first | What is the smallest bounded change, and what must remain untouched? |

## Route outputs

Before writing the final prompt, record:

```text
Primary mode:
Secondary constraint:
Asset:
Surface and format:
First-glance target:
Must preserve:
May change:
Must not introduce:
Selected rubric:
```

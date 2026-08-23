# Operation and Verification Gates

## Decide whether research is required

Research before prompting whenever accuracy depends on a named or time-sensitive subject, including real buildings, cities, products, vehicles, uniforms, historic periods, organisms, maps, technical systems, or regional cultural materials. Use factual sources for facts and visual references for silhouette, proportion, terrain, materials, and layout.

If research is unavailable, disclose that fidelity is limited. Do not fill gaps with invented labels, logos, history, or product details.

## Assign image roles explicitly

| Input | Use when | Prompt language |
| --- | --- | --- |
| Edit target | The user wants an existing image changed | `Edit the supplied image` |
| Composition reference | Framing or arrangement must be retained | `Use as composition reference only` |
| Style reference | Medium, palette, or rendering language is the target | `Use as style reference only` |
| Identity reference | Person or character traits must remain consistent | `Preserve identity traits from this reference` |
| Product reference | Shape, label, material, or color must be accurate | `Preserve product geometry and visible branding constraints` |
| Mask | Only a bounded region may change | `Modify the masked region only; retain unmasked pixels` |

## Generation preflight

Before sending a prompt, check:

1. Is the asset type clear?
2. Does format match the intended placement?
3. Is every required in-image string quoted verbatim?
4. Does the prompt name one dominant visual anchor rather than a style pile-up?
5. Are research-backed facts and reference roles included only when needed?
6. Are there explicit constraints against extra text, watermarks, or unwanted changes?

## Result review

Inspect the rendered file rather than trusting the generation response. Evaluate text accuracy, hierarchy, composition, camera/framing, subject placement, material/rendering logic, reference fidelity, and unintended artifacts. For a failed result, change one causal variable per iteration: text hierarchy, subject placement, lens/framing, lighting, style anchor, or the edit boundary.

## Provider-neutral cautions

Capabilities differ across image APIs. Confirm support for transparency, dimensions, multiple image inputs, masks, and output encoding before committing a workflow. Do not silently turn a requested edit into a text-only generation, and do not expose API keys in prompts, command output, generated assets, or reports.

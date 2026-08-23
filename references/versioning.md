# Prompt Versioning and Series Lock

Use version records for iterative, commercial, reference-led, or multi-image work. A version is a complete prompt state, not a label attached to a partial change.

## Version rules

- Assign `V1` to the first locked prompt.
- Increment to `V2`, `V3`, and so on only after a deliberate change.
- Preserve the full prompt text for every locked version.
- Record one primary reason for each revision.
- Never rewrite an earlier version in place.
- If the user requests “the first version,” “the original prompt,” or a named version, restore that exact version before considering any new change.
- If an older prompt was not saved, state that it cannot be reproduced exactly; do not pretend that a reconstruction is identical.

## Prompt Ledger record

Save one record per locked version using this schema:

```text
Prompt ID:
Version:
Created or revised:
Task:
Asset and surface:
Primary objective:
Secondary constraint:
Reference roles:
Known facts:
Must-preserve invariants:
Creative variables:
Must-not-introduce list:
Required text:
Output format:
Full prompt:
Changed from previous:
Reason for change:
Review result:
Next hypothesis:
```

## Change discipline

Change one causal variable per iteration whenever possible:

| Variable | Example change |
| --- | --- |
| Objective | Switch from product fidelity to campaign concept |
| Subject invariant | Strengthen a garment’s right-side knot or a person’s facial cue |
| Composition | Move the subject, change scale, or increase negative space |
| Camera | Change height, lens perspective, or framing |
| Visual system | Change one palette, lighting, or material rule |
| Text | Change hierarchy, exact string, or post-production policy |
| Reference role | Reclassify a style reference as product or identity reference |
| Tool strategy | Switch from image generation to structured or programmatic rendering |

Record the change as:

```text
Changed from [version]: [one variable]
Reason: [failure or new requirement]
Expected effect: [what should improve]
```

## Series Lock

For a series of related images, lock the fields that must remain stable:

```text
Series ID:
Locked identity:
Locked product version:
Locked palette:
Locked camera or framing family:
Locked typography policy:
Locked reference roles:
Allowed variation:
Forbidden drift:
```

Use Series Lock for product listing sets, campaign sets, character sheets, recurring portraits, and multi-view product imagery. Do not lock incidental background details unless consistency requires them.

## Restoration protocol

When restoring a previous version:

1. Locate the version record.
2. Reproduce its direction, assumptions, reference roles, exact text, and full prompt.
3. State that the output is a restoration, not a revision.
4. Do not improve, shorten, or modernize the prompt unless the user separately requests a change.
5. If generating a new image from the restored prompt, assign a render attempt number without changing the prompt version.

## Review record

After generation, append:

```text
Render attempt:
Technical score:
Task-success score:
Critical failure:
What worked:
What failed:
Next variable to change:
```

A prompt version is not considered stable until it passes the selected scenario rubric and the user’s stated success contract.

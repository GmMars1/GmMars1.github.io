# MarsRAG Loop Contract Implementation

This document implements the Loop Contract plan by making `expected_output` the primary execution contract across CrewAI task completion, task chaining, runtime state, and UI rendering.

## 1) Canonical Contract

Use one shared structured output contract named `LoopOutput`.

### Required fields

- `hook`
- `grip`
- `payoff`
- `reinforce`
- `loop`

### Validation rules

- All fields are required.
- All fields must be non-empty strings after trim.
- Max length per field: 800 characters.
- Soft target length per field: 1-4 sentences.

### Contract completion rule

- **Task complete**: output validates against `LoopOutput`.
- **Task incomplete**: output fails schema validation.

### Contract versioning

- Add `loop_contract_version` to each task config.
- Initial version: `1.0.0`.
- Version bump policy:
  - Patch: wording clarifications, no field behavior change.
  - Minor: backward-compatible additions.
  - Major: breaking field/validation changes.

## 2) CrewAI Task Contract Standardization

Use one reusable `expected_output` template for all narrative tasks and bind each task to `output_pydantic=LoopOutput`.

### Standard template

Use this exact order and wording:

1. HOOK: Open with one clear tension or stakes statement anchored to the user goal.
2. GRIP: Provide the key insight, mechanism, or diagnosis that keeps attention.
3. PAYOFF: Deliver specific value, recommendation, or resolution.
4. REINFORCE: Strengthen confidence with evidence, constraints, or practical framing.
5. LOOP: End with the best next question or action that naturally advances the flow.

### Task definition requirements

Every narrative task must define:

- `description`
- `expected_output` (template above)
- `output_pydantic=LoopOutput`
- `loop_contract_version`

## 3) Contract-Native Chaining

Chain narrative tasks using explicit state transitions.

### Required transition rule

- `next.hook` must be derived from `prior.loop`.

### Transition behavior

1. Validate prior `LoopOutput`.
2. If valid, map `prior.loop -> next.hook` and pass prior task in `context=[prior_task]`.
3. If invalid/missing, run one repair attempt.
4. If repair fails, use safe fallback hook:
   - "What is the single most important next step to resolve the current uncertainty?"

### Transition metadata

Persist per handoff:

- `transition_source_task_id`
- `transition_target_task_id`
- `transition_mode` (`direct|repair|fallback`)
- `transition_reason`

## 4) Runtime State Integration (MarsRAG Orchestrator)

Treat Loop Contract fields as first-class runtime state.

## Runtime state object

```json
{
  "run_id": "string",
  "task_id": "string",
  "loop_contract_version": "1.0.0",
  "loop_mode": "hard",
  "validation": {
    "status": "valid",
    "errors": []
  },
  "loop_output": {
    "hook": "...",
    "grip": "...",
    "payoff": "...",
    "reinforce": "...",
    "loop": "..."
  },
  "routing": {
    "next_agent": "string",
    "next_tool": "string",
    "next_workflow": "string"
  }
}
```

### Runtime usage rules

- Use `loop` as primary routing hint for next task selection.
- Use `hook` to shape retrieval query intent.
- Use `payoff` to shape summarization output priorities.
- Persist structured fields separately from rendered prose.

## 5) UI Contract Rendering

Render Loop Contract fields as separate UI blocks.

### UI requirements

- Show sections in fixed order: Hook, Grip, Payoff, Reinforce, Loop.
- Show validation status badge: `valid`, `partial`, `failed`.
- Surface `loop` as **Next recommended question/action**.
- If validation fails, show fallback message and operator action:
  - "Regenerate section" for partial failures.
  - "Run repair task" for full failures.

### UI state mapping

- `valid`: all fields pass schema.
- `partial`: schema fails but at least 3 fields are present.
- `failed`: schema fails with fewer than 3 valid fields.

## 6) Reliability Safeguards

Add contract checks to prevent drift and breakage.

### Regression tests

Per narrative task type, test:

1. Schema conformance success path.
2. Missing field failure.
3. Empty string failure.
4. Over-length field failure.
5. Chaining transition from prior loop.
6. Fallback transition path.

### Contract lint checks

- `expected_output` section order must match canonical template.
- All five section labels must exist.
- `loop_contract_version` must be present.
- `output_pydantic` must equal `LoopOutput` for narrative tasks.

### Required metrics

Track at minimum:

- `loop_schema_pass_rate`
- `loop_follow_rate`
- `downstream_action_rate`
- `session_depth`
- `repair_rate`
- `fallback_rate`

## 7) Loop Intensity Controls

Add workflow-level `loop_mode`.

- `none`: no narrative sections, machine-first output.
- `soft`: narrative sections with flexible strictness.
- `hard`: strict contract, all checks enforced.

Default policy:

- User-facing narrative workflows: `hard`
- Machine-first/internal transform workflows: `none` or `soft`

## 8) Reference Interfaces and Events

Use these interfaces/events in MarsRAG to operationalize the contract.

### Interface: Contract validation

- Input: raw task output
- Output: `validation.status`, normalized `loop_output`, error list

### Interface: Transition planner

- Input: prior `loop_output`, target task config
- Output: next hook text, `transition_mode`, reason

### Interface: UI view model mapper

- Input: runtime state
- Output: section cards, status badge, next action card

### Event model

Emit events per run:

- `loop.contract.validated`
- `loop.contract.failed`
- `loop.transition.planned`
- `loop.transition.fallback_used`
- `loop.ui.rendered`
- `loop.action.followed`

Event payload fields:

- `run_id`
- `task_id`
- `loop_contract_version`
- `loop_mode`
- `validation_status`
- `transition_mode`
- `timestamp`

## 9) Rollout Sequence

1. Ship schema and canonical task template (`v1.0.0`).
2. Enable contract lint in CI for narrative tasks.
3. Enable chaining rule (`prior.loop -> next.hook`) with repair/fallback.
4. Ship UI section rendering + status badges.
5. Start metrics collection and weekly review.
6. Tune `loop_mode` by workflow based on measured outcomes.

## 10) Definition of Done

Implementation is complete when:

- All narrative tasks use canonical `expected_output` and `LoopOutput`.
- Runtime stores typed loop state and validation status.
- Task chaining enforces `prior.loop -> next.hook` with fallback.
- UI renders separate contract sections and next-action card.
- Contract lint and regression tests run on every change.
- Core loop metrics are visible in ops dashboards.

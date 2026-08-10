# Stripe Dispute Workflow Implementation

This document implements the dispute automation plan with a production-ready checklist you can execute in Stripe Dashboard Workflows and your internal webhook service.

## 1) Workflow Scope

Automate these Stripe events first:

- `charge.dispute.created` (primary intake trigger)
- `radar.early_fraud_warning.created` (optional pre-dispute prevention)
- `charge.dispute.closed` (outcome sync)

Expected outcomes per event:

- Notify risk/ops immediately
- Create internal task/ticket
- Trigger internal webhook for evidence assembly
- Route to manual review when policy or data checks fail

## 2) Prerequisites

Before enabling automation:

- Stripe Workflows is enabled on the target account.
- Destinations are ready:
  - Email recipients
  - Slack channel/webhook
  - Internal dispute webhook endpoint
- Policy thresholds are documented:
  - Amount threshold(s)
  - Dispute reason/category rules
  - Card network rules
  - Region-specific fee handling rules

## 3) Create the Workflow (Dashboard)

1. Go to **Stripe Dashboard → Workflows → New workflow**.
2. Name: **Dispute Intake - High Priority**.
3. Environment: confirm Sandbox first, then Production.

## 4) Trigger Configuration

Primary trigger:

- Event: `charge.dispute.created`

Additional workflows (recommended):

- `radar.early_fraud_warning.created` for low-value auto-refund policy
- `charge.dispute.closed` for closing internal tasks and metrics updates

## 5) Condition Logic

Apply branching logic in this order:

1. **Amount threshold**
   - Example: `dispute.amount >= 100000` (in minor currency units).
2. **Dispute reason/category**
   - Include/exclude targeted reasons.
3. **Optional metadata/risk filters**
   - Merchant segment, customer risk tag, country/network markers.
4. **Fallback condition**
   - If required data is missing, route to manual review branch.

## 6) Actions by Branch

### A) Standard auto-processing branch

- Send immediate Slack/email alert with:
  - `dispute.id`
  - `charge`
  - `amount`
  - `reason`
  - `evidence_details.due_by`
- Create internal task/ticket with:
  - Owner/team
  - Priority from amount + due date
  - Required evidence checklist
- Trigger internal webhook for evidence assembly.

### B) Escalation branch (deadline risk or high value)

- Send high-priority escalation alert.
- Increase ticket priority.
- Notify backup/on-call channel.

### C) Manual intervention branch

- Trigger when:
  - data is incomplete
  - policy check fails
  - API/upload action fails
- Open task with explicit failure reason and next action.

## 7) Safety Controls (Required)

Implement these controls in the internal webhook handler:

- Verify Stripe webhook signatures.
- Idempotency keyed by `dispute.id`.
- Retry transient failures (exponential backoff).
- Dead-letter queue for hard failures.
- Per-dispute processing lock to prevent duplicates.
- Deadline guardrails using `evidence_details.due_by`.

## 8) Internal Webhook Contract

Recommended payload sent from workflow action:

```json
{
  "event_type": "charge.dispute.created",
  "dispute_id": "dp_...",
  "charge_id": "ch_...",
  "payment_intent_id": "pi_...",
  "amount": 100000,
  "currency": "usd",
  "reason": "fraudulent",
  "network": "visa",
  "due_by": 1735689600,
  "account": "acct_..."
}
```

Required webhook response behavior:

- `2xx`: accepted for processing
- `4xx`: validation/policy error (route to manual review)
- `5xx`: retry path

## 9) Sandbox Test Matrix

Run tests for each path:

1. High-value dispute → escalation branch.
2. Low-value dispute → standard branch.
3. Missing required fields → manual intervention branch.
4. Simulated webhook failure → retry + dead-letter behavior.
5. Duplicate event delivery → single processing outcome.
6. Deadline-near scenario → urgent escalation.

Validate:

- Alerts are sent correctly.
- Ticket/task is created with complete context.
- Webhook payload is correct.
- No duplicate task or duplicate evidence submission behavior.

## 10) Publish Strategy

Rollout sequence:

1. Deploy in production with monitoring enabled.
2. Limit initial scope (single reason code or threshold segment).
3. Expand to full policy after stable results.

## 11) Monitoring and Tuning

Track weekly:

- Response-before-deadline rate
- Automation success rate
- Manual review volume
- Duplicate event handling accuracy
- Failure causes by branch/action

Operational loop:

- Review failed runs weekly.
- Tune thresholds/conditions/actions.
- Version every workflow policy change.
- Keep audit log of policy updates and approvers.

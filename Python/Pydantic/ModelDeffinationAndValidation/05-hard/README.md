# Hard Challenge: WebhookEvent Model

## Scenario
Webhook event validation:
- Payload must be valid JSON.
- Signature validated using HMAC SHA256 with secret key.
- Timestamp must not be older than 5 minutes.

## Why It Matters
Critical for secure API integrations:
- Prevents replay attacks.
- Ensures authenticity of payloads.
- Protects against tampering.

## Tests
Run `pytest` to validate:
- Correct signature passes.
- Wrong signature fails.
- Expired timestamp fails.

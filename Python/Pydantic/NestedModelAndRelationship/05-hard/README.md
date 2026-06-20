# Hard Challenge: Invoice and Line Items

## Scenario
- An `Invoice` contains multiple `LineItem`s.
- The sum of line item totals must equal the invoice_total.

## Why It Matters
Critical in financial systems:
- Prevents mismatched or fraudulent invoices.
- Ensures accounting integrity.

## Tests
Run `pytest test_models.py` to validate:
- Valid invoices pass.
- Mismatched totals fail.

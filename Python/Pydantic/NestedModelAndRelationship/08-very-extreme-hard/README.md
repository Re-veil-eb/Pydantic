# Very Extreme Hard Challenge: Supply Chain

## Scenario
- A `SupplyChain` contains `Factory`, `Warehouse`, and `RetailStore` models.
- Factories supply warehouses, warehouses supply stores.
- Inventory counts must balance across the chain.
- No warehouse or store can have negative stock.

## Why It Matters
Simulates enterprise supply chain management:
- Enforces inventory consistency.
- Prevents negative stock errors.
- Ensures end-to-end balance across the chain.

## Tests
Run `pytest test_models.py` to validate:
- Negative stock fails.
- Unbalanced warehouse/store stock fails.

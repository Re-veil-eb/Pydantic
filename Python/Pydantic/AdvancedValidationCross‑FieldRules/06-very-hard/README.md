# Very Hard Challenges: Risk & Eligibility Rules

## Scenarios
1. **LoanApplication** → Loan amount cannot exceed 5× income unless collateral is provided.
2. **JobApplication** → Applicants with <2 years experience must provide internship details.
3. **TravelVisa** → USA visas require passport validity ≥ 6 months.
4. **OnlineExam** → End time must be within exam window.

## Why It Matters
These rules simulate banking, HR, travel, and exam systems:
- Enforces loan risk policies.
- Requires internship details for junior applicants.
- Validates passport rules for visas.
- Ensures exams respect time windows.

## Tests
Run `pytest test_models.py` to validate:
- Excessive loans without collateral fail.
- Missing internship details fail.
- Short passport validity fails.
- Exams exceeding window fail.

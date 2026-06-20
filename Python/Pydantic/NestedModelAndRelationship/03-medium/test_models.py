import pytest
from models import Employee, Company

class TestCompanyEmployees:
    def test_valid_company(self):
        employees = [Employee(employee_id="1", role="CEO"), Employee(employee_id="2", role="Engineer")]
        company = Company(name="TechCorp", employees=employees)
        assert any(e.role == "CEO" for e in company.employees)

    def test_duplicate_employee_ids(self):
        employees = [Employee(employee_id="1", role="CEO"), Employee(employee_id="1", role="Engineer")]
        with pytest.raises(ValueError):
            Company(name="TechCorp", employees=employees)

    def test_missing_ceo(self):
        employees = [Employee(employee_id="2", role="Engineer")]
        with pytest.raises(ValueError):
            Company(name="TechCorp", employees=employees)

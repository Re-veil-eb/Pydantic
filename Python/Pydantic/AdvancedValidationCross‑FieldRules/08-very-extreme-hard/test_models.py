import pytest
from models import Prescription, HealthcareRecord, BankingTransaction, SupplyChainAudit

class TestHealthcareRecord:
    def test_valid_record(self):
        p1 = Prescription(drug="aspirin", signed_by_doctor=True)
        hr = HealthcareRecord(patient_age=30, doctor="Dr. B", prescriptions=[p1], insurance_covered_drugs=["aspirin"])
        assert hr.prescriptions[0].drug == "aspirin"

    def test_invalid_unsigned_prescription(self):
        p1 = Prescription(drug="aspirin", signed_by_doctor=False)
        with pytest.raises(ValueError):
            HealthcareRecord(patient_age=30, doctor="Dr. B", prescriptions=[p1], insurance_covered_drugs=["aspirin"])

    def test_invalid_uncovered_drug(self):
        p1 = Prescription(drug="aspirin", signed_by_doctor=True)
        with pytest.raises(ValueError):
            HealthcareRecord(patient_age=30, doctor="Dr. B", prescriptions=[p1], insurance_covered_drugs=["ibuprofen"])

    def test_invalid_age_treatment(self):
        p1 = Prescription(drug="adult-only", signed_by_doctor=True)
        with pytest.raises(ValueError):
            HealthcareRecord(patient_age=15, doctor="Dr. B", prescriptions=[p1], insurance_covered_drugs=["adult-only"])

class TestBankingTransaction:
    def test_valid_transaction(self):
        bt = BankingTransaction(debit=100, credit=100)
        assert bt.debit == bt.credit

    def test_invalid_transaction(self):
        with pytest.raises(ValueError):
            BankingTransaction(debit=100, credit=90)

class TestSupplyChainAudit:
    def test_valid_audit(self):
        sca = SupplyChainAudit(warehouse_stock=100, shipments=100)
        assert sca.shipments == sca.warehouse_stock

    def test_invalid_audit(self):
        with pytest.raises(ValueError):
            SupplyChainAudit(warehouse_stock=100, shipments=90)

from pydantic import BaseModel, model_validator
from typing import List

class Prescription(BaseModel):
    drug: str
    signed_by_doctor: bool

class HealthcareRecord(BaseModel):
    patient_age: int
    doctor: str
    prescriptions: List[Prescription]
    insurance_covered_drugs: List[str]

    @model_validator(mode="after")
    def validate_record(self):
        for p in self.prescriptions:
            if not p.signed_by_doctor:
                raise ValueError(f"Prescription {p.drug} not signed by doctor")
            if p.drug not in self.insurance_covered_drugs:
                raise ValueError(f"Drug {p.drug} not covered by insurance")
        if self.patient_age < 18 and any(p.drug == "adult-only" for p in self.prescriptions):
            raise ValueError("Patient too young for adult-only treatment")
        return self

class BankingTransaction(BaseModel):
    debit: float
    credit: float

    @model_validator(mode="after")
    def validate_balance(self):
        if self.debit != self.credit:
            raise ValueError("Debits and credits must balance")
        return self

class SupplyChainAudit(BaseModel):
    warehouse_stock: int
    shipments: int

    @model_validator(mode="after")
    def validate_audit(self):
        if self.shipments != self.warehouse_stock:
            raise ValueError("Shipments must reconcile with warehouse stock")
        return self

import json
import os
from uuid import UUID
from typing import Dict, Any, Literal
from pydantic import BaseModel, Field, field_validator, model_validator

# Simulated dynamic JSON schema file creation for validation
SCHEMA_FILE_PATH = "metadata_schema.json"
with open(SCHEMA_FILE_PATH, "w") as f:
    json.dump({"required_fields": ["worker_id", "region"]}, f)


class DistributedJob(BaseModel):
    job_id: UUID
    status: Literal["PENDING", "RUNNING", "COMPLETED", "FAILED"] = "PENDING"
    retry_count: int = Field(0, ge=0)
    metadata: Dict[str, Any]

    @model_validator(mode="before")
    @classmethod
    def validate_dynamic_metadata(cls, data: Any) -> Any:
        """Loads schema from JSON file dynamically and validates metadata keys."""
        if isinstance(data, dict) and "metadata" in data:
            if os.path.exists(SCHEMA_FILE_PATH):
                with open(SCHEMA_FILE_PATH, "r") as f:
                    schema = json.load(f)
                
                # Check for required fields defined in the JSON file
                required = schema.get("required_fields", [])
                provided = data["metadata"].keys()
                
                for field in required:
                    if field not in provided:
                        raise ValueError(f"Metadata missing required schema field: '{field}'")
        return data

    def transition_to(self, new_status: Literal["PENDING", "RUNNING", "COMPLETED", "FAILED"]) -> None:
        """Enforces state machine transitions and increments retry on FAILURE."""
        valid_transitions = {
            "PENDING": ["RUNNING"],
            "RUNNING": ["COMPLETED", "FAILED"],
            "COMPLETED": [],
            "FAILED": ["PENDING", "RUNNING"]  # Allowed transitions to retry the job
        }

        if new_status not in valid_transitions[self.status]:
            raise ValueError(f"Invalid transition from {self.status} to {new_status}")

        if new_status == "FAILED":
            self.retry_count += 1

        self.status = new_status

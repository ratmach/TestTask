from typing import Optional, Any

from pydantic import BaseModel, model_validator

from sum.Operation import registered_operators_as_enum, operators


class OperationRequest(BaseModel):
    operand_a: Optional[Any] = None
    operand_b: Optional[Any] = None
    operator: registered_operators_as_enum()

    class Config:
        use_enum_values = True

    @model_validator(mode='before')
    def check_fields(self, data):
        operator = self.get("operator")
        operator_class = operators(operator)
        errors = []
        for field, field_types in operator_class.required_fields().items():
            if field not in self:
                errors.append(f"{field} required")
            elif type(self[field]) not in field_types:
                errors.append(f"{field} must be type {field_types}")
        if errors:
            raise ValueError("\n".join(errors))
        return self

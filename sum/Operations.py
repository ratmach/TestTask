from sum.Operation import Operation, operators


@operators("+", True)
class OperationAdd(Operation):
    def resultDict(self):
        return {**dict(super().resultDict()), **dict(color="red")}

    @property
    def result(self):
        return self.data.operand_a + self.data.operand_b


@operators("-", True)
class OperationSubtract(Operation):

    @property
    def result(self):
        return self.data.operand_a - self.data.operand_b


@operators("/", True)
class OperationDivide(Operation):

    @property
    def result(self):
        return self.data.operand_a / self.data.operand_b


@operators("*", True)
class OperationMultiply(Operation):

    @property
    def result(self):
        return self.data.operand_a * self.data.operand_b


# @operators("calculate", True) THIS IS COMMENTED OUT SO IT DOES NOT APPEAR IN VALID OPERATORS ON FRONTEND
class OperationCalculate(Operation):
    """
        this is the example of how one would go about implementing the "a + b - c/d + x * d"
    """

    @property
    def result(self):
        # implementation goes here
        return self.data.operand_a

    @staticmethod
    def required_fields():
        return dict(operand_a=(str,))

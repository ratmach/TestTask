import enum
from abc import ABC, abstractmethod
from functools import wraps


def operators(symbol: str, register=False, raise_error=False):
    if register:
        def decorator(resolver_class):
            if not operators.__globals__.get("registry", None):
                operators.__globals__["registry"] = {}
            operators.__globals__["registry"][symbol] = resolver_class

            @wraps(resolver_class)
            def wrapper(*args, **kwargs):
                return resolver_class(*args, **kwargs)

            return wrapper

        return decorator
    else:
        operator = operators.__globals__.get("registry", {}).get(symbol)
        if not operator and raise_error:
            raise ValueError(f"Unregistered operator: {symbol}")
        elif not operator and not raise_error:
            return None
        return operator


def registered_operators_as_enum():
    keys = list(operators.__globals__.get("registry", {}).keys())
    values = list(map(lambda x: x.__name__, operators.__globals__.get("registry", {}).values()))
    return enum.Enum("operations", dict(zip(values, keys)))


class Operation(ABC):
    def __init__(self, data):
        self.data = data

    def resultDict(self):
        return dict(result=self.result)

    @property
    @abstractmethod
    def result(self):
        pass

    @staticmethod
    def required_fields():
        return dict(operand_a=(float, int), operand_b=(float, int))

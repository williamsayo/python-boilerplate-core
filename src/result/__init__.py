from .base import Fail as FailClass, Ok as OkClass, Result
from .guards import is_ok, is_fail, is_result
from .utils.helpers import (
    result_fail,
    result_ok,
    result_combine,
    as_result,
    as_result_all,
    unwrap_or,
    value_or,
    result_equality,
)
from .types import Either, ResultCombine, Result, Ok, Fail

__all__ = [
    # concrete classes
    "OkClass",
    "FailClass",
    "Result",
    # guards
    "is_ok",
    "is_fail",
    "is_result",
    # helpers
    "result_fail",
    "result_ok",
    "result_combine",
    "as_result",
    "as_result_all",
    "unwrap_or",
    "value_or",
    "result_equality",
    # types
    "Ok",
    "Fail",
    "Result",
    "ResultCombine",
    "Either",
]

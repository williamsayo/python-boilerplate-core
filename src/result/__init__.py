from .base import Fail, Ok, Result
from .nothing import Nothing,NothingType
from .guards import is_ok, is_fail
from .utils.helpers import result_fail,result_ok,result_combine

__all__ = [
    "Ok",
    "Fail",
    "Nothing",
    "is_ok",
    "is_fail",
    "result_fail",
    "result_ok",
    "result_combine",
]

from typing import TypeGuard, reveal_type, TypeIs
from src.result.types.base import Either, Result, Ok, Fail
from src.result.base import Result as ResultInstance

def is_result[T](result: T) -> TypeGuard[ResultInstance[T]]:
    """
    Type guard to check if a value is a Result instance (Ok or Fail).

    Args:
        result (T): The object to check.

    Returns:
        TypeGuard[ResultInstance[T]]: True if `result` is an instance of Ok or Fail,
        otherwise False.
    """
    return isinstance(result, ResultInstance)

def is_ok[S, F](result: Either[S, F]) -> TypeGuard[Ok[S]]:
    """
    Type guard to check if a Result is an Ok.

    This function can be used to narrow the type of a Result to Ok.

    Args:
        result (Either[S, F]): The Result object to check.

    Returns:
        TypeGuard[Ok[S]]: True if `result` is an Ok result, otherwise False.
    """
    return result.isOk()

def is_fail[S, F](result: Either[S, F]) -> TypeGuard[Fail[F]]:
    """
    Type guard to check if a Result is a Fail.

    This function can be used to narrow the type of a Result to Fail.

    Args:
        result (Either[S, F]): The Result object to check.

    Returns:
        TypeGuard[Fail[F]]: True if `result` is a Fail result, otherwise False.
    """
    return result.isFail()

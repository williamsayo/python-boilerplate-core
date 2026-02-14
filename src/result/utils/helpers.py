from src.result.base import Ok, Fail, Result as ResultInstance
from src.result.types.base import Either, Result
from src.result.nothing import Nothing, NothingType
from src.result.guards import is_fail, is_ok
from typing import List, Sequence


def result_equality[T, K](result: T, otherResult: K) -> bool:
    """
    Compare two Result objects for equality.

    This function returns True only when:
    - both inputs are Ok results and their values are equal, OR
    - both inputs are Fail results and their values are equal.

    If the two inputs are not both Results, or they are different variants
    (Ok vs Fail), the function returns False.

    Args:
        result (T): The first object to compare.
        otherResult (K): The second object to compare.

    Returns:
        bool: True if both are the same Result variant and their values match,
        otherwise False.
    """

    if isinstance(result, Ok) and isinstance(otherResult, Ok) or isinstance(result, Fail) and isinstance(otherResult, Fail):
        return result.value == otherResult.value
    return False


def result_ok[S](value: S | None = None) -> Ok[S]:
    """
    Create an Ok result containing the provided value.

    If no value is passed, the Ok result will contain None.

    Args:
        value (S | None, optional): The value to wrap in an Ok result.
            Defaults to None.

    Returns:
        Ok[S]: An Ok result containing the provided value.
    """
    return Ok(value)


def result_fail[F](value: F) -> Fail[F]:
    """
    Create a Fail result containing the provided error value.

    Args:
        value (F): The error value to wrap in a Fail result.

    Returns:
        Fail[F]: A Fail result containing the provided error value.
    """
    return Fail(value)


def result_combine[S, F](
    results: Sequence[Either[S, F]],
) -> Ok[List[S | None]] | Fail[F]:
    """
    Combine a sequence of Result objects into a single Result.

    Behavior:
    - If all results are Ok, returns Ok([...]) containing all Ok values in order.
    - If any result is Fail, returns Fail(error) using the first Fail encountered.

    Args:
        results (Sequence[Either[S, F]]): A sequence of Ok/Fail results.

    Returns:
        Ok[List[S | None]] | Fail[F]:
            - Ok(list_of_values) if all are Ok
            - Fail(error) if any Fail is found
    """
    validResults: List[S | None] = []

    for result in results:
        value = result.value
        if is_fail(result):
            return result_fail(result.value)
        validResults.append(value)
    return result_ok(validResults)


def value_or[T, K](result: Either[T, T], default: K) -> T | K | None:
    """
    Return the contained value from an Ok result, or a default value if Fail.

    This function enforces that the first argument must be a Result instance
    (Ok or Fail). If a non-result is passed, a TypeError is raised.

    Args:
        result (Either[T, T]): The Result (Ok/Fail) to extract a value from.
        default (K): The fallback value to return when result is Fail.

    Raises:
        TypeError: If `result` is not an Ok/Fail instance.

    Returns:
        T | None | K:
            - Ok.value if the result is Ok
            - default if the result is Fail
    """
    if not isinstance(result, ResultInstance):
        raise TypeError(f"Expected Result (Ok/Fail), got {repr(result)}")
    if not is_fail(result):
        return result.value
    return default


def unwrap_or[T, E](result: ResultInstance[T], default: E) -> T | E:
    """
    Extract and return the raw value from a Result, or return a default value.

    Note:
        Despite the type hint, this function safely handles non-Result inputs:
        if the input is not an Ok/Fail instance, the default is returned.

    Args:
        result (ResultInstance[T]): The Result (Ok/Fail) to unwrap.
        default (E): The fallback value to return if result is not a Result.

    Returns:
        T | E:
            - result.value if result is an Ok/Fail instance
            - default otherwise
    """
    return result.value if isinstance(result, ResultInstance) else default

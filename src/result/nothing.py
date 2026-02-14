from dataclasses import dataclass
from typing import runtime_checkable, Protocol, Never, Final, Literal

@runtime_checkable
class NothingType(Protocol):
    def __nothing__(self) -> Never: ...

@dataclass(frozen=True)
class _Nothing:
    def __nothing__(self) -> Never:
        raise RuntimeError("Nothing has no value")

    def __repr__(self) -> str:
        return "Nothing"

    value = None

Nothing: Final[_Nothing] = _Nothing()

__all__ = ["Nothing", "NothingType"]
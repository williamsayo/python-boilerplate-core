from typing import Union, TypeAliasType, TypeAlias
from src.result.base import Ok, Fail
from src.result.nothing import NothingType

type Either[S, F] = Ok[S]| Fail[F]
type Ok[S] = Ok[S]
type Fail[F] = Fail[F]
type Result = Ok | Fail
type Option[T] = Either[T, NothingType]

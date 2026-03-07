from typing import List, Union
from result.base import _Ok, _Fail
from result.nothing import NothingType

type Either[S, F] = Ok[S] | Fail[F]
type Ok[S] = _Ok[S]
type Fail[F] = _Fail[F]
type Result[T] = Ok[T] | Fail[T]
type Option[T] = Either[T, NothingType]
type ResultCombine[S, F] = Either[List[S], F]

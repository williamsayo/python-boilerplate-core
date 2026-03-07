from typing import List
from result.base import Ok as OkClass, Fail as FailClass

type Either[S, F] = Ok[S] | FailClass[F]
type Ok[S] = OkClass[S]
type Fail[F] = FailClass[F]
type Result[T] = OkClass[T] | FailClass[T]
type ResultCombine[S, F] = Either[List[S], F]

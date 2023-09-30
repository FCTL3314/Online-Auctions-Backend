from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from app.base.repositories import AbstractRepository

T = TypeVar("T")
REPO_T = TypeVar("REPO_T", bound=AbstractRepository)


class AbstractService(ABC, Generic[T, REPO_T]):
    def __init__(
        self,
        repository: REPO_T,
    ):
        self.repository: REPO_T = repository


class AbstractRetrieveService(AbstractService[T, REPO_T]):
    @abstractmethod
    def retrieve(self, *args, **kwargs):
        ...


class AbstractListService(AbstractService[T, REPO_T]):
    @abstractmethod
    def list(self, *args, **kwargs):
        ...


class AbstractCreateService(AbstractService[T, REPO_T]):
    @abstractmethod
    def create(self, *args, **kwargs):
        ...


class AbstractUpdateService(AbstractService[T, REPO_T]):
    @abstractmethod
    def update(self, *args, **kwargs):
        ...


class AbstractDeleteService(AbstractService[T, REPO_T]):
    @abstractmethod
    def delete(self, *args, **kwargs):
        ...


class AbstractCRUDService(
    AbstractRetrieveService,
    AbstractListService,
    AbstractCreateService,
    AbstractUpdateService,
    AbstractDeleteService,
    ABC,
    Generic[T, REPO_T],
):
    ...

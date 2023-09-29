from abc import ABC, abstractmethod

from app.base.repositories import (
    AbstractCRUDRepository,
)


class AbstractService(ABC):
    def __init__(
        self,
        repository: AbstractCRUDRepository,
    ):
        self.repository = repository


class AbstractRetrieveService(AbstractService):
    @abstractmethod
    def retrieve(self, *args, **kwargs):
        ...


class AbstractListService(AbstractService):
    @abstractmethod
    def list(self, *args, **kwargs):
        ...


class AbstractCreateService(AbstractService):
    @abstractmethod
    def create(self, *args, **kwargs):
        ...


class AbstractUpdateService(AbstractService):
    @abstractmethod
    def update(self, *args, **kwargs):
        ...


class AbstractDeleteService(AbstractService):
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
):
    ...

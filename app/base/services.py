from abc import ABC, abstractmethod

from app.base.repositories import AbstractCRUDRepository


class AbstractRetrieveService(ABC):
    @abstractmethod
    def retrieve(self, *args, **kwargs):
        ...


class AbstractListService(ABC):
    @abstractmethod
    def list(self, *args, **kwargs):
        ...


class AbstractCreateService(ABC):
    @abstractmethod
    def create(self, *args, **kwargs):
        ...


class AbstractUpdateService(ABC):
    @abstractmethod
    def update(self, *args, **kwargs):
        ...


class AbstractDeleteService(ABC):
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
    def __init__(self, repository: AbstractCRUDRepository):
        self.repository = repository

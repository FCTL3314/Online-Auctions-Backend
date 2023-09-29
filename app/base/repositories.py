from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    def one(self, *args, **kwargs):
        ...

    @abstractmethod
    def all(self, *args, **kwargs):
        ...


class AbstractCreateRepository(ABC):
    @abstractmethod
    def create(self, *args, **kwargs):
        ...


class AbstractUpdateRepository(ABC):
    @abstractmethod
    def update(self, *args, **kwargs):
        ...


class AbstractDeleteRepository(ABC):
    @abstractmethod
    def delete(self, *args, **kwargs):
        ...


class AbstractCRUDRepository(
    AbstractCreateRepository,
    AbstractUpdateRepository,
    AbstractDeleteRepository,
    AbstractRepository,
    ABC,
):
    ...

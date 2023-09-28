from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    def get(self, *args, **kwargs):
        ...

    @abstractmethod
    def all(self, *args, **kwargs):
        ...


class AbstractCRUDRepository(AbstractRepository):
    @abstractmethod
    def create(self, *args, **kwargs):
        ...

    @abstractmethod
    def update(self, *args, **kwargs):
        ...

    @abstractmethod
    def delete(self, *args, **kwargs):
        ...

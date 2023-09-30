from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    base_query = None


class AbstractGetRepository(AbstractRepository):
    @abstractmethod
    def get(self, *args, **kwargs):
        ...


class AbstractAllRepository(AbstractRepository):
    @abstractmethod
    def all(self, *args, **kwargs):
        ...


class AbstractCreateRepository(AbstractRepository):
    @abstractmethod
    def create(self, *args, **kwargs):
        ...


class AbstractUpdateRepository(AbstractRepository):
    @abstractmethod
    def update(self, *args, **kwargs):
        ...


class AbstractDeleteRepository(AbstractRepository):
    @abstractmethod
    def delete(self, *args, **kwargs):
        ...


class AbstractCRUDRepository(
    AbstractGetRepository,
    AbstractAllRepository,
    AbstractCreateRepository,
    AbstractUpdateRepository,
    AbstractDeleteRepository,
    ABC,
):
    ...

from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def getAll(self):
        pass

    def getById(self):
        pass


class MyClass(BaseRepository):
    def create(self):
        pass

    def getAll(self):
        pass


obj = MyClass()

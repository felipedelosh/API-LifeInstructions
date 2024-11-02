# app/repositories/person/iperson_repository.py
from abc import ABC, abstractmethod

class IPersonRepository(ABC):
    @abstractmethod
    def get_next_id(self):
        pass

    @abstractmethod
    def add(self, person):
        pass

    @abstractmethod
    def get_all(self):
        pass

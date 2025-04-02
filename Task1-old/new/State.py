from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def __eq__(self, other):
        """check if equal -> boolean"""
        pass

    @abstractmethod
    def __hash__(self):
        """return hash code"""
        pass

    @abstractmethod
    def __str__(self):
        """return string representation"""
        pass
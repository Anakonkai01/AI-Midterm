from abc import ABC, abstractmethod

class Search(ABC):
    @abstractmethod
    def search(self, problem):
        """return list of actions to the goal state"""
        pass
    
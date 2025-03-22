from abc import ABC, abstractmethod

class HeuristicFunction(ABC):
    @abstractmethod
    def getHeuristic(self, state, goalStates):
        """return heuristic value"""
        pass



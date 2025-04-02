from abc import ABC, abstractmethod

class Problem(ABC):
    @abstractmethod
    def getInitialState(self):
        """return initial state"""
        pass

    @abstractmethod
    def isGoalState(self, state):
        """check goal state -> boolean"""
        pass


    @abstractmethod
    def getSuccessors(self, state):
        """return successor state"""
        pass

    @abstractmethod
    def getCost(self, state, action):
        """return cost of action"""
        pass
from abc import ABC, abstractmethod

class test(ABC):
    @abstractmethod
    def getHelloWorld():
        """return Hello World"""
        pass


class testImplement(test):
    def getHelloWorld(self):
        return "Hello World"
    
    def getHelloWorld2(self):
        return "Hello World2"
    

test = test()
print(test.getHelloWorld())
print(test.getHelloWorld2())
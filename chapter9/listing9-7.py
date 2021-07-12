import abc

"""
This is our interface
"""
class ActionsInterface(abc.ABC):
   @abc.abstractmethod
   def eat() -> str:
       pass

class BotanyInterface(abc.ABC):
   @abc.abstractmethod
   def eat() -> str:
       pass

"""
This is the class implementing the interface
"""
class Human(ActionsInterface):
   def eat(self) -> str:
       return 'I am eating'

human = Human()
print(human.eat())
import abc

"""
This is our interface
"""
class ActionsInterface(abc.ABC):
   @abc.abstractmethod
   def eat() -> str:
       pass

   @abc.abstractmethod
   def tree() -> str:
       pass

"""
This is the class implementing the interface

Instantiating this class into an object will fail. Because Human is not implementing all
of ActionInterface's methods, it changes Human into an abstract class.

You can test this by commenting and uncommenting the def tree function in the above class
"""
class Human(ActionsInterface):
   def eat(self) -> str:
       return 'I am eating'

human = Human()
print(human.eat())

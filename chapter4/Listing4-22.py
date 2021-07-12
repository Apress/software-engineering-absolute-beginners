"""
Class Member consists of a constructor that sets a name. We will use this to demonstrate the magic method for operator overloading
"""
class Member:
    def __init__(self, name):
        self.name = name

"""
Class Group contains three magic method. You have already encountered __init__. This is the constructor, and is called whenever you instantiate an object.
"""
class Group:

    def __init__(self):
        self.members = []

    """
    __add__ is a magic method that does operator overloading. Overloading means we add new behaviour to an already existing operator or function, and call that new behaviour under specific conditions. In this case it overloads +, and inside the body of the __add__ function we add the logic of what the overloaded + must do. We need to specify in the parameter list, as the second parameter, what is to be expected on the right hand side of the + sign. In this case it is something of type Member. All we want to do when we add something of type Member to type Group is to take Member’s name parameter and add it to Group’s list of names.  Whenever Python sees a Group object followed by a plus, it will run the __add__ function.
    """
    def __add__(self, x: Member):
        self.members.append(x.name)

    """
    __str__ is a magic method that returns a string whenever you treat your object as a string. Whenever I say for instance do this. print(MyObject), then MyObject will run the __str__ function. 
    """
    def __str__(self):
        return ','.join(self.members)

group = Group()
member1 = Member('nico')
member2 = Member('john')

group + member1
group + member2

print(group)

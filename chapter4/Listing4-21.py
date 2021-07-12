# Parent object
class Pet:
    def sound(self):
        # Pass is called a null statement in Python, and nothing happens when Python encounters it 
        pass

# IS-A pet
class Cat(Pet):
    def sound(self):
        return 'Meow'

# IS-A pet
class Dog(Pet):
    def sound(self):
        return 'Woof'

# Function getSound receives a Pet as a parameter,
# but we are not specifying what kind of pet. Polymorphism is used to resolve this
def getSound(pet: Pet):
    return pet.sound()

print(getSound(Dog()))
print(getSound(Cat()))

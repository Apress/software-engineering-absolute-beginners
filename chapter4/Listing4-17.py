class Dog:

    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color

    def bark(self):
        print('woof')

    def run(self):
        print('Running')

dog = Dog('Fluffy', 'Poodle', 'white')
dog.bark()

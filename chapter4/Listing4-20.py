class Cycles:
    def set_as_assembled(self, is_assembled):
            self.assembled = is_assembled

    def get_wheel_count(self):
        return self.wheel_count

    def who_am_i(self):
        return  'I am the original function'

# Note the change in how we define our class. We added round brackets and placed
# the parent it inherits from name in between it.
# Monocycle IS-A Cycles and inherits from Cycles
class Monocycle(Cycles):
    # Override the parent function with a similar function that behaves differently
    def who_am_i(self):
        return 'I am overriding the parent function'
    wheel_count = 1

# A second child class. Bicycle IS-A Cycles
class Bicycle(Cycles):
    wheel_count = 2

# A third child class. Tricycle IS-A Cycles
class Tricycle(Cycles):
    wheel_count = 3

monocycles = Monocycle()
print(monocycles.get_wheel_count())

cycles = Bicycle()
print(cycles.get_wheel_count())

# In this section we show how the function overriding works
print(monocycles.who_am_i())
print(cycles.who_am_i())

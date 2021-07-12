'''
This class technically consists of one attribute, a string, and two behavioural aspects, which is checking the validity of the password, and whether the password has been used previously. Actual algorithms are not included for brevity.
'''


class Password:
    password = ""

    def __init__(self, password):
        self.password = password

    def is_valid(self) -> bool:
        # Password algorithm goes here
        return True


    def is_reused(self) -> bool:
        # Reuse algorithm goes here
        return False

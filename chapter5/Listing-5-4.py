class TotalCalculator:
    def get_value(self) -> int:
        return 100


# MemberFees has a TotalCalculator.
class MemberFees:
    def __init__(self):
        self.calculator_object = TotalCalculator()

# Club has a MemberFees.
class Club:
    def __init__(self):
        self.member_object = MemberFees()

    # Club accesses data from TotalCalculator, even though TotalCalculator
    # does not belong to Club.
    def get_total(self) -> str:
        return self.member_object.calculator_object.get_value()


c = Club()
print(c.get_total())

"""
Refactored MemberFees and Club with TotalCalculator code omitted for brevity. This demonstrates that class A should access class B only. How class B's function gets its data is of no concern to class A.
"""
class MemberFees:
    def __init__(self):
        self.calculator_object = TotalCalculator()

    def total_fees(self) -> str:
        return self.calculator_object.get_value()


class Club:
    def __init__(self):
        self.member_object = MemberFees()

    """
    Technically two dots, but fine to use as the first dot indicates that it is an object         variable.
    """
    def get_total(self) -> str:
        return self.member_object.total_fees()

    """
    One dot, but this is not ideal. Not having MemberFees in the constructor in this case makes it more difficult to keep track of which objects belong to class Club. This would negatively affect how we understand the class.
    """
    def get_total_one_dot(self) -> str:
        member_object = MemberFees()
        return member_object.total_fees()


c = Club()
print(c.get_total())
print(c.get_total_one_dot())

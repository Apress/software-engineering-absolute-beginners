class BankAccount:
    """A very short description of the class fitting on one line.

        Example:
            Usage examples can go here.

        For instance
            bank_account = BankAccount('John', 15342);
            bank_account.transfer(843675421)

        Attributes:
            account (the type of attribute, for instance, int): Description of the account attribute.
            valid (boolean): Contains the result of whether the account is valid or not

    """

    def __init__(self, user, code):
        """Short description goes here. This function transfers money. This can also go in the class-level docstring

            Note:
                Do not include the 'self' parameter in the 'Args' section.

            Args:
                user: The account number.
            code: The verification code

            Returns:
                True if successful, False otherwise.
        """
        self.code = code


def transfer(self, account_number):
    """Short description goes here. This function transfers money.

        Note:
            Do not include the 'self' parameter in the 'Args' section.

        Args:
            account_number: The account number.

        Returns:
            True if successful, False otherwise.

        Raises:
        Exception raising information goes here

    """
    return True

class VAT:
    vat_rate = 15

    # This function can be used statically. No 'self' is being passed through.
    def static_get_vat_price(price):
        return price * (1.0 + VAT.vat_rate/100)

    # This function cannot be used statically, as it is reliant on self, and self only
    # exist when the object gets created
    def get_vat_price(self, price):
        return price * (1.0 + VAT.vat_rate/100)

# These two examples will work. No object instantiation has happened
print(VAT.vat_rate) # Prints the vat rate
print(VAT.static_get_vat_price(50)) # Calculates the amount after after VAT

# This wont work without object instantiation and will throw an error, the parameter self does not exist
print(VAT.get_vat_price(50))

def more_indentation(number, name):
    if number > 10:
        if name == "John":
            print("Number is bigger than 10 and Name is John")
        if name != "John":
            print("Number is bigger than 10 and Name is not John")
            if name == "Peter":
                print("Number is bigger than 10 and Name is Peter")


def less_indentation(number, name):
    # Exit early. Inspecting the above code we can see that if the number
    # is 10 or lower, then nothing happens. We invert the logic in the previous if
    # statement to detect if number <= 10
    if number <= 10:
        return

    # Initialise is_john to a default message. Now is_john has a value
    is_john = "Number is bigger than 10 and Name is not John"

    if name == "John":
        is_john = "Number is bigger than 10 and Name is John"

    print(is_john)

    if name == "Peter":
        print("Number is bigger than 10 and Name is Peter")


# The two functions will yield exactly the same results
more_indentation(11, "John")
less_indentation(11, "John")

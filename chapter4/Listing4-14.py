def log_error(error, print_to_screen=True):
    if print_to_screen:
        print(error)
    else:
        return error

# Equivalent calls, prints directly to screen
log_error('error message 1')
log_error('error message 2', True)

# Returns it variable to the calling code, where you can do more operations on it or in this case, just print it
error = log_error('error message 3', False)
print(error)

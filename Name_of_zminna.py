import string

while True:
    try:
        variable_name = input("Enter a variable: ")

        # Flag to track the validity of the variable name
        is_valid = True

        # Check for starting with a digit
        if variable_name[0].isdigit():
            is_valid = False

        # Check for uppercase letters
        elif any(symbol.isupper() for symbol in variable_name):
            is_valid = False

        # Check for spaces, punctuation, special characters, and non-printable characters
        elif any(symbol in string.punctuation or symbol.isspace() or not symbol.isprintable() for symbol in variable_name if symbol != '_'):
            is_valid = False

        # If the name is valid, print a message and exit the loop
        if is_valid:
            print("Variable name is valid.")
            break
        else:
            print("Variable name is not valid. Please re-enter.")
    except Exception:
        print("An error occurred. Please check your input.")

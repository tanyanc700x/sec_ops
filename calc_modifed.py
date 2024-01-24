while True:
    try:
        # First digit request
        num1 = float(input("Provide your first digit: "))

        # Second digit request
        num2 = float(input("Provide your second digit: "))

        # Choosing math operation
        operator = input("Choose operation (+, -, *, /): ")

        # Results part
        while operator == '/' and num2 == 0:
            print("Error. You cannot divide by zero.")
            num2 = float(input("Provide a digit that is > 0: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2

        print("Result:", result)

        # A question about further calculation
        while True:
            another_calculation = input("Do you want to calculate again? (y/n): ").lower()

            if another_calculation in ['y', 'n']:
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        if another_calculation == 'n':
            print("Ну, нет так нет")
            break  # Exit the loop if the user chooses not to continue

    except Exception:
        print("An error occurred")
########################################### With checks ###################################################

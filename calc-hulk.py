# # ############################## The code with necessary conditions #########################################
# First digit request
num1 = float(input("Provide your first digit: "))

# Second digit request
num2 = float(input("Provide your second digit: "))

# Choosing math operation with input validation
valid_operators = ['+', '-', '*', '/']
operator = input("Choose operation (+, -, *, /): ")

while operator not in valid_operators:
    print("Invalid operator. Please choose a valid operator.")
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


################################### The same but with loop to start again ###################################################
# while True:
#     # First digit request
#     num1 = float(input("Provide your first digit: "))
#
#     # Second digit request
#     num2 = float(input("Provide your second digit: "))
#
#     # Choosing math operation
#     operator = input("Choose operation (+, -, *, /): ")
#
#     # Results part:
#     if operator == '+':
#         result = num1 + num2
#     elif operator == '-':
#         result = num1 - num2
#     elif operator == '*':
#         result = num1 * num2
#     elif operator == '/':
#         # Division by zero check
#         if num2 == 0:
#             print("Error. You cannot divide by zero")
#             num2 = float(input("Provide a digit that is > 0: "))
#             result = num1 / num2
#         else:
#             result = num1 / num2
#
#     # Print the result
#     print("Result:", result)
#
#     # A question about further calculation
#     another_calculation = input("Do you want to calculate again? (y/n): ")
#     if another_calculation.lower() != 'y':
#         print("Okay, tobto tak.")
#         break  # exit the loop if the user does not want to calculate again

# # ############################### Another Ty With While #####################################################
# # # First digit request
# # num1 = float(input("Provide your first digit: "))
# #
# # # Second digit request
# # num2 = float(input("Provide your second digit: "))
# #
# # # Choosing math operation
# # operator = input("Choose operation (+, -, *, /): ")
# #
# # # Initialize result variable
# # result = 0  # You can set it to any default value
# #
# # # Results part:
# # if operator == '+':
# #     result = num1 + num2
# # elif operator == '-':
# #     result = num1 - num2
# # elif operator == '*':
# #     result = num1 * num2
# # elif operator == '/':
# #     # Division by zero check
# #     while num2 == 0:
# #         print("Error. You cannot divide by zero")
# #         num2 = float(input("Provide a digit that is > 0: "))
# #
# #     result = num1 / num2
# #
# # # Print the result
# # print("Result:", result)


############################ One More With None and f-string ####################
# # First digit request
# num1 = None
# while num1 is None:
#     user_input = input("Provide your first digit: ")
#     try:
#         num1 = float(user_input)
#     except ValueError:
#         print("Error: Please enter a valid numerical value.")
#
# # Now num1 contains a valid numeric value
# print(f"You entered: {num1}")
#
# # Second digit request
# num2 = float(input("Provide your second digit: "))
#
# # Choosing math operation
# operator = input("Choose operation (+, -, *, /): ")
#
# # Results part:
# try:
#     if operator == '+':
#         result = num1 + num2
#     elif operator == '-':
#         result = num1 - num2
#     elif operator == '*':
#         result = num1 * num2
#     elif operator == '/':
#         # Division by zero check
#         while num2 == 0:
#             print("Error. You cannot divide by zero")
#             num2 = float(input("Provide a digit that is > 0: "))
#
#         result = num1 / num2
#     print(f"Result: {result}")
#
#     # A question about further calculation
#     another_calculation = input("Do you want to calculate again? (y/n): ")
#     if another_calculation.lower() != 'y':
#         print("Okay, tobto tak.")
#
# except ZeroDivisionError:
#     print("Error: You cannot divide by zero. Please provide a non-zero second digit.")
# except ValueError:
#     print("Error: Please enter valid numerical values.")
################################## Match case####################################

# # First digit request
# num1 = float(input("Provide your first digit: "))
#
# # Second digit request
# num2 = float(input("Provide your second digit: "))
#
# # Choosing math operation with input validation
# valid_operators = {'+', '-', '*', '/'}
# operator = input("Choose operation (+, -, *, /): ")
#
# while operator not in valid_operators:
#     print("Invalid operator. Please choose a valid operator.")
#     operator = input("Choose operation (+, -, *, /): ")
#
# # Results part
# while operator == '/' and num2 == 0:
#     print("Error. You cannot divide by zero.")
#     num2 = float(input("Provide a digit that is > 0: "))
#
# # Using match case for operation
# match operator:
#     case '+':
#         result = num1 + num2
#     case '-':
#         result = num1 - num2
#     case '*':
#         result = num1 * num2
#     case '/':
#         result = num1 / num2
#
# print("Result:", result)
import dns.resolver
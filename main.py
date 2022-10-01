
# Pseudocode
# Generate Menu
# Generate user select options
# Generate operations


# 1.ADDITION
# 2.SUBTRACTION
# 3.MULTIPLICATION
# 4.DIVISION



print("Simple Python Calculator")
print("************************")

print("Please select from the following options:")
print('1. ADDITION')
print('2. SUBTRACTION')
print('3. MULTIPLICATION')
print('4. DIVISION')
print('5. SQUARE ROOT')
print('6. QUIT CALCULATOR')

operation_choice = input("Please enter your selection here:")

# perform addition
if operation_choice == "1":
    num1 = input("Enter your first number:")
    num2 = input("Enter your second number:")
    print("The sum is:", int(num1) + int(num2))

# perform subtraction
elif operation_choice == "2": # perform subtraction
    num1 = input("Enter your first number:")
    num2 = input("Enter your second number:")
    print("The difference is:", int(num1) - int(num2))

# perform multiplication
elif operation_choice == "3":
    num1 = input("Enter your first number:")
    num2 = input("Enter your second number:")
    print("The product is:", int(num1) * int(num2))

# perform division
elif operation_choice == "4":
    num1 = input("Enter your first number:")
    num2 = input("Enter your second number:")
    print("The result is:", int(num1) / int(num2))

# perform square root
elif operation_choice == "5":
    num = input('Enter your number:')
    print('The square root is:', int(num) ** 0.5)

# quit program
elif operation_choice == "6":
    print("Thank you for using the simple Python Calculator...Goodbye")
else:
    print("Invalid entry. Please select a valid option")












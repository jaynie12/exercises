
# different function for each input/operation
def add(x, y):
    """" Adds two numbers """
    return x + y


def subtract(x, y):
    """ Subtracts two numbers """
    return x - y


def multiply(x, y):
    """ Multiples two numbers """
    return x * y


def divide(x, y):
    """Divides two numbers"""
    return x / y


def power(x, y):
    """raises x to the power of y"""
    return x**y


def modulus(x, y):
    """ find's the modulous of x and y"""
    return x % y


def user_input():
    operation = str(input("Enter the operation"))
    try:
        first_number = float(input("Enter the number"))
        second_number = float(input("Enter the number"))
    except Exception:
        print('You must enter a numerical value')

    return operation, first_number, second_number


def check_if_user_has_finished():
    """
    In this function we are going to check whether the user wants to
    keep on using the calculator

    While the user's entry is false, continue to ask them the
    question "Do you want to finish"

    Set end calculator to False only if answer = Y
    """
    end_calculator = True
    valid_user_entry = False
    while not valid_user_entry:
        user_input = input('Do you want to finish> (y/n)')
        if user_input == "Y":
            valid_user_entry = True
        elif user_input == "N":
            valid_user_entry = True
            end_calculator = False
        else:
            print("Invalid entry, please try again")
            valid_user_entry = False
    return end_calculator


operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "//": divide,
    "**": power,

}


def user_calculations(operation, first_number, second_number):
    result = operations_dict[operation](first_number, second_number) \
        if operation in operations_dict else print("Error")
    return result


finished = False
while not finished:
    result = 0
    user = user_input()
    result = user_calculations(user[0], user[1], user[2])
    print("result: " + str(result))
    finished = check_if_user_has_finished()

print('=================')
print('Bye')

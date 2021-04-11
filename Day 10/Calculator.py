from art import logo

# Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply 
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Exponent
def exponent(n1, n2):
    return n1 ** n2

# Modulus
def modulus(n1, n2):
    return n1 % n2

# Dictionary of math operations
operations = {
"+" : add,
"-" : subtract,
"*" : multiply,
"/" : divide, 
"^" : exponent, 
"%" : modulus
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    next_calculation = True

    while next_calculation:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        continue_calc = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation or any other letter to quit: ").lower()
        if continue_calc == 'y':
            # next_calculation = True
            num1 = answer
        elif continue_calc == 'n':
            next_calculation = False
            calculator()
        else:
            break

calculator()

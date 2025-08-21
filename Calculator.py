def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

should_continue = True
reuse_number = ""
while should_continue:
    if reuse_number == "y":
        n1 = output
    else:
        n1 = int(input("What is the first number? :"))
    operation = input("+\n-\n*\n/\nWhat do you want to do?")
    n2 = int(input("What is the second number? :"))

    if operation == "+":
        output = add(n1,n2)
    elif operation == "-":
        output = subtract(n1,n2)
    elif operation == "*":
        output = multiply(n1,n2)
    elif operation == "/":
        output = divide(n1, n2)
    else:
        output = "You did not enter a valid argument"

    print(f"{n1} {operation} {n2} = {output}")
    reuse_number = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation")
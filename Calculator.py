logo = r"""
 _____________________
|  _________________  |
| | Jack Hines   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

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

    print(output)
    reuse_number = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation")
from datetime import datetime


def save_history(calculation):
    with open("calculator_history.txt", "a") as file:
        file.write(calculation + "\n")


while True:

    try:
        num1 = float(input("Enter the first number: "))

        operator = input(
            "Enter operator (+, -, *, /, ^,p or q to quit): "
        )

        if operator == "q":
            print("Calculator closed.")
            break

        num2 = float(input("Enter the second number: "))

    except ValueError:
        print("Invalid input! Please enter numbers only.\n")
        continue


 
    if operator == "/" and num2 == 0:
        print("Error: Division by zero is not allowed.\n")
        continue



    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        result = num1 / num2

    elif operator == "^":
        result = num1 ** num2

    elif operator == "p":
        result = num1 * num2 / 100

    else:
        print("Invalid operator.\n")
        continue


    print("Answer is:", result)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    
    calculation = (
        f"{current_time} | "
        f"{num1} {operator} {num2} = {result}"
    )


  
    save_history(calculation)

    print("Calculation saved to history.\n")
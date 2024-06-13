print("Welcome to CALCULATOR....")
while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Please enter the operation you want to perform: \n + for addition \n - for subtraction \n * for multiplication \n / for division ")
    operation = input("Enter your operation: ")
    if operation in ('+','-','*','/'):
        #perform operation
        if operation == "+":
            print(f"The Addition of {num1} and {num2} is",num1+num2)
        elif operation == '-':
            print(f"The Difference of {num1} and {num2} is",num1-num2)
        elif operation == '*':
            print(f"The Multiplication of {num1} and {num2} is",num1*num2)
        elif operation == '/':
            if num2 != 0:
                print(f"The Division of {num1} and {num2} is",num1/num2)
            else:
                print("Error! Division by zero is not allowed.")
                print("Invalid operation.please try again")
    op = input("Do you want to continue? (yes/no): ")
    if op.lower() == 'yes':
        continue
    else:
        print('Goodbye!...')
        break


        

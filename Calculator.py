def calculator():
    while True:
        print("\n==== SMART CALCULATOR ====")
        print("1.Addition(+)")
        print("2.Subtraction(-)")
        print("3.Multiplication(*)")
        print("4.Divison(/)")
        print("5.Exit")

        choice = input("Enter your choice(1-5):")

        #Exit conditon
        if choice =='5':
            print("Thankyou for using Calculator!")
            break

        #Invalid choice handling
        if choice not in ['1','2','3','4']:
            print("Invalid choice! Try Again.")
            continue

        #Taking input numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue

        #Performing operations
        if choice == '1':
            result = num1+num2
            print(f"Result:{num1}+{num2}={result}")

        elif choice == '2':
            result=num1-num2
            print(f"Result:{num1}-{num2}={result}")

        elif choice == '3':
            result=num1*num2
            print(f"Result:{num1}*{num2}={result}")

        elif choice == '4':
            if num2==0:
                print("Error! Divison by zero not possible.")
            else:
                result=num1/num2
                print(f"Result:{num1}/{num2}={result}")

#run the program
calculator()

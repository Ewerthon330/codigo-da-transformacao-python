while True:
    print('\n---------------------------------')
    print("Welcome to the Interactive Menu:")
    print('---------------------------------')
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Exit")
    
    print('---------------------------------')
    choice = input("Choose an option: ")
    print('---------------------------------')

    if choice == "1":
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print('------------------------------------')
        print("Result of addition:", a + b)
    
    elif choice == "2":
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print('------------------------------------')
        print("Result of subtraction:", a - b)
    
    elif choice == "3":
        print("Exiting the program...")
        print("Thanks for participating, see you next time\n")
        break
    else:
        print("Invalid option, please try again.")

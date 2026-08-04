while True:
    try:
        choice = int(input("0 - quit | 1 - use last result | 2 - new calculation : "))
    except ValueError:
        print("Enter only numeral value")
        continue
    try:
        if choice == 0:
            break
        elif choice == 1:
            first_num = last_result
            second_num = float(input("Enter second number: "))
        elif choice == 2:
            first_num = float(input("Enter first number: "))
            second_num = float(input("Enter second number: "))
        else:
            print("Enter an option 0,1 or 2")
    except ValueError:
        print("Please,enter only numeral value!")
        continue
    except NameError:
        print("You need to new calculation")
        continue
    try:
        option = int(input("Select an option: 1 - addition, 2 - subtraction, 3 - multiply, 4 - float-division (with remainder), 5 - exponentiation, 6 - remainder, 7 - int-division : "))
    except ValueError:
        print("Enter only numeral value!")
        continue
    if option == 1:
        last_result = first_num + second_num
        print(f"{first_num} + {second_num} = {last_result}")
        continue
    elif option == 2:
        last_result = first_num - second_num
        print(f"{first_num} - {second_num} = {last_result}")
        continue
    elif option == 3:
        last_result = first_num * second_num
        print(f"{first_num} * {second_num} = {last_result}")
        continue
    elif option == 4:
        try:
            last_result = first_num / second_num
            print(f"{first_num} / {second_num} = {last_result}")
        except ZeroDivisionError:
            print("Error - Division by zero makes no sense :)")
        continue
    elif option == 5:
        last_result = first_num ** second_num
        print(f"{first_num} ** {second_num} = {last_result}")
        continue
    elif option == 6:
        try:
            last_result = first_num % second_num
            print(f"{first_num} % {second_num} = {last_result}")
        except ZeroDivisionError:
            print("Error - Division by zero makes no sense :)")
        continue
    elif option == 7:
        try:
            last_result = first_num // second_num
            print(f"{first_num} // {second_num} = {last_result}")
        except ZeroDivisionError:
            print("Error - Division by zero makes no sense :)")
        continue
    else:
        print("Select an option between 1-7")


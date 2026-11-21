from operator import add,sub,mul,truediv,floordiv,mod,pow
last_result = None
def division_func(func):
    def wrapper(f_num,s_num):
        if s_num == 0:
            return None
        result = func(f_num,s_num)
        return result
    return wrapper
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
            if last_result is None:
                print('You need a new calculation!')
                continue
            first_num = last_result
            second_num = float(input("Enter second number: "))
        elif choice == 2:
            while True:
                try:
                    first_num = float(input("Enter first number: "))
                    second_num = float(input("Enter second number: "))
                    break
                except ValueError:
                    print("Вводите только числа!")
                    continue
        else:
            print("Enter an option 0,1 or 2")
            continue
    except ValueError:
        print("Please,enter only numeral value!")
        continue
    while True:
        try:
            option = int(input("Select an option: 1 - addition, 2 - subtraction, 3 - multiply, 4 - float-division (with remainder), 5 - exponentiation, 6 - remainder, 7 - int-division : "))
        except ValueError:
            print("Enter only numeral value!")
            continue
        if option == 1:
            last_result = add(first_num,second_num)
            print(last_result)
            break
        elif option == 2:
            last_result = sub(first_num,second_num)
            print(last_result)
            break
        elif option == 3:
            last_result = mul(first_num,second_num)
            print(last_result)
            break
        elif option == 4:
            part_div = division_func(truediv)
            last_result = part_div(first_num,second_num)
            if last_result is None:
                print("Error - Division by zero makes no sense :)")
                continue
            print(last_result)
            break
        elif option == 5:
            last_result = pow(first_num,second_num)
            print(last_result)
            break
        elif option == 6:
            moda = division_func(mod)
            last_result = moda(first_num,second_num)
            if last_result is None:
                print("Error - Division by zero makes no sense :)")
                continue
            print(last_result)
            break
        elif option == 7:
            ful_div = division_func(floordiv)
            last_result = ful_div(first_num,second_num)
            if last_result is None:
                print("Error - Division by zero makes no sense :)")
                continue
            print(last_result)
            break
        else:
            print("Select an option between 1-7")
            continue

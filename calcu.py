first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))
while True:
    option = int(input("Select an option: 1 - addition, 2 - subtraction, 3 - multiply, 4 - division : "))
    if option == 1:
        print(f"{first_num} + {second_num} = {first_num + second_num}")
        break
    elif option == 2:
        print(f"{first_num} - {second_num} = {first_num - second_num}")
        break
    elif option == 3:
        print(f"{first_num} * {second_num} = {first_num * second_num}")
        break
    elif option == 4:
        print(f"{first_num} / {second_num} = {first_num / second_num}")
        break
    else:
        print("Error,please select an option between 1-4")


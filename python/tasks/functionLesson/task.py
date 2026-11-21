def square(x):
    return x ** 2
print(square(4))

def sum_two(x,y):
    return x + y
print(sum_two(3,7))

def is_positive(x):
    if x > 0:
        return True
    return False

print(is_positive(5))
print(is_positive(-2))

def get_greeting(name):
    return(f"Привет, {name}")

print(get_greeting("Alice"))

def get_user_info(name,age):
    return (name,age)

name,age = get_user_info("Макс",22)
print(name)
print(age)


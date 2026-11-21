def sum_all(*args):
    total = 0
    for i in args:
        total += i
    return total

print(sum_all(1, 2))
print(sum_all(1, 2, 3))
print(sum_all(10, 20, 30, 40))

def longest_word(*words):
    if not words:
        return ''
    final_word = words[0]
    for word in words:
        if len(word) > len(final_word):
            final_word = word
    return final_word

print(longest_word("Finger","Globe","Gugol","Hole","Electrical","Quant","Mechanical"))

def print_args_and_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
print_args_and_kwargs(1, 2, 3, name="Alice", age=25)


def create_profile(name,age=0,*args,**kwargs):
    print(f"name: {name}")
    print(f"age: {age}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
create_profile("Alice", 25, "Python", "Math", city="Москва")


def multiply(a, b):
    return a * b
numbers = [5, 7]

print(multiply(*numbers))

def greet(name, age):
    return f"Имя: {name}, возраст: {age}"
data = {"name": "Alice", "age": 25}
print(greet(**data))

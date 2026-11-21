def multiply(x,y):
    return x * y

print(multiply(8,9))
print(multiply(x = 8, y = 9))

def power(x,y = 2):
    return x ** y

print(power(5))
print(power(5,3))

def create_profile(name,age,city = "Москва"):
    return f"Имя: {name}, возраст: {age}, город: {city}"
print(create_profile("Alice",25))
print(create_profile("Alice",25,"Тюмень"))
print(create_profile(age = 25, city = "Тюмень", name = "Alice"))

def add_item(item,box = []):
    box.append(item)
    return box
print(add_item("Apple"))
print(add_item("Banana"))

def add_item_new(item,box = None):
    if box is None:
        box = []
    box.append(item)
    return box
print(add_item_new("Apple"))
print(add_item_new("Banana"))


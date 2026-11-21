square = lambda x: x ** 2
print(square(4))

add = lambda x,y : x + y
print(add(2, 3))

is_even = lambda x: True if x % 2 == 0 else False
print(is_even(4))
print(is_even(7))

words = ["apple", "kiwi", "banana", "fig"]
sorted_words = sorted(words,key=lambda word: len(word))
print(sorted_words)

sorted_words = sorted(words,key=len)
print(sorted_words)

pairs = [(1, 5), (3, 1), (2, 2)]
sorted_pairs = sorted(pairs,key=lambda pair: pair[1])
print(sorted_pairs)

users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Carl", "age": 30},
]
sorted_users = sorted(users,key=lambda user: user['age'])
print(sorted_users)

def get_age(user):
    return user["age"]
sorted_users = sorted(users,key=get_age)
print(sorted_users)

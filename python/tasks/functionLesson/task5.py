numbers = [1,2,3,4,5]
numbers_new = list(map(lambda x: x ** 2, numbers))
print(numbers_new)

numbers.append(6)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

words = ['apple','fig','banana','kiwi']
words_len = list(map(len,words))
print(words_len)

filtered_words = list(filter(lambda x: len(x) > 3,words))
print(filtered_words)

numbers = [-10,2,-3,7]
sorted_numbers = sorted(numbers,key=abs)
print(sorted_numbers)

users = [
    {'name':'Alice','age': 25},
    {'name':'Bob','age':20},
    {'name':'Carl','age':30}
]
sorted_users = sorted(users,key=lambda dictionary: dictionary['age'],reverse=True)
print(sorted_users)

sorted_words = sorted(words,key=lambda word: (len(word),word))
print(sorted_words)

numbers = [1,2,3,4,5]
squares = [x ** 2 for x in numbers]
print(squares)

numbers.append(6)
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

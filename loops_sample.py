developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer
print(rest)

numbers = [1,2,3,4,5]
numbers.append(6)
print(numbers)

even_numbers = [2,4,6]
numbers.extend(even_numbers)
print(numbers)

# insert
# remove
# clear
# sort
# reverse
# index

# Tuples

for i in range(10):
    print(i)

print(list(range(1,20,3)))

languages = ['Spanish', 'English', 'Russian', 'Chinese']

print(list(enumerate(languages)))

for index,language in enumerate(languages):
    print(index,language)

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]
ids2 = range(100,500,100)

print(list(zip(developers,ids,ids2)))

# List comprehension

even_numbers = [num for num in range(21) if num%2 == 0]
print(even_numbers)

numbers = [x for x in range(1,6)]
print(numbers)
result = [(num,"Even") if num%2 == 0 else (num,"Odd") for num in range(1,6)]
print(result)

print([(x,x**2) for x in range(10)])

# Filtering lists

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

long_words = list(filter(lambda x:len(x)>4,words))
print(long_words)

# map

celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit,celsius))
print(fahrenheit)
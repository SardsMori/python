my_string = """My
Multiline
     String"""

print(my_string)

my_str = "Hello World"
print("Hello" in my_str)
print("hey" in my_str)
print("hello" in my_str)
print("hi" in my_str)
print("e" in my_str)

print(len(my_str))
print(my_str[0])

sound = "ha"
repeated_sound = sound * 3
print(repeated_sound)

name = "Sards"
age = 26
name_and_age = name + str(age)
print(name_and_age)

print(f"{name} is {age} years old.")

# String Slicing
my_str = "Hello World"
print(my_str[1:4])
print(my_str[:7])

print(my_str[8:])
print(my_str[0:11:2])
print(my_str[::-1])

print(my_str.upper())
print(my_str.lower())
my_str = "            Hello World            "
print(my_str.strip())

print(my_str.replace("World","Earth").strip())
split_words = my_str.split()
print(" ".join(split_words))
my_str = "Hello World"
print(my_str.startswith("Hello"))
print(my_str.startswith("hello"))
print(my_str.endswith("World"))
print(my_str.endswith("world"))
print(my_str.find("World"))
print(my_str.count("o"))
print(my_str.capitalize())
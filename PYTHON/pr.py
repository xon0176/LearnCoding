
## **Python Code Snippet**

print("Hey, Guyz!") # Output: Hey, Guyz!
print("Namaste,This is Kartik C T ") # Output: Namaste,This is Kartik C T 

## Variable Declaration and Data Types

age = 21           ; a = [1, 2, 3, 4]
name = "Kartik"    ; b = (1, 2, 3, 4,)
is_student = True  ; c = {1, 2, 3, 4}
weight = 54.300    ; d = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

print(type(age))         # Output: <class 'int'>
print(type(name))        # Output: <class 'str'>
print(type(is_student))  # Output: <class 'bool'>
print(type(weight))      # Output: <class 'float'>

print(type(a))           # Output: <class 'list'>
print(type(b))           # Output: <class 'tuple'>
print(type(c))           # Output: <class 'set'>
print(type(d))           # Output: <class 'dict'>

## Type Conversion

x = "10"     # x is a string
y = int(x)   # Convert string to integer
z = float(y) # Convert integer to float
print(z)     # Output: 10.0

## Variable Assignment and Reassignment

x = 10
print(x)  # Output: 10
x = 20
print(x)  # Output: 20

x, y, z, = 20, 40, 60
print(x)  # Output: 20
print(y)  # Output: 40
print(z)  # Output: 60

x = y = z = 50
print(x, y, z) # Output: 50 50 50

## Input and Output

Name = "Kartik"
Age = 21
print(Name)               # Output
name = input("Name: ")    # Input
age = int(input("Age: ")) # Input [int]

boy_name = input("Boy Name: ")
boy_age = int(input("Boy Age: "))
girl_name = input("Girl Name: ")
girl_age = int(input("Girl Age: "))

## String Concatenation, Formatting and Repetition

print(boy_name +" Loves "+ girl_name) # Concatenation

age_diff = boy_age - girl_age

print(boy_name + " Loves " + girl_name + ".There age differance is " + str(age_diff)) # Concatenation
print(f"{boy_name} Loves {girl_name}.There age differance is {age_diff} ")            # f-strings

A = "GO " * 3  # Repetition
print(A)       # Output: GO GO GO
B = "Run "     # Repetition
print(B *3)    # Output: Run Run Run 

## String Methods

message = "  Hello, Kartik!  "
print(message.upper())                   # Output: "  HELLO, KARTIK!  "
print(message.lower())                   # Output: "  hello, kartik!  "
print(message.strip())                   # Output: "Hello, Kartik!"
print(message.replace("Kartik", "Mani")) # Output: "  Hello, Mani!  "

## String Indexing and Slicing

Name = "Kartik"
      # 012345  # +ve indexing
#    -5-4-3-2-1 # -ve indexing
print(Name[0])  # Output: K   ## +ve indexing
print(Name[2])  # Output: r
print(Name[-1]) # Output: k   ## -ve indexing
print(Name[-5]) # Output: a

State = "Karnataka"
        #012345678  # +ve indexing
print(State[:8])    # Output: Karnataka
print(State[3:8])   # Output: nataka
print(State[5:])    # Output: taka
print(State[0:9:3]) # Output: Kar

## Comments

# Single-line comments start with a hash (#).

print("Hello, Kartik!")   # Output: "Hello, Kartik!"

"""
Multi-line comments can be done using triple quotes 
or by using multiple single-line comments.
"""
print("Hello, Python!")   # Output: Hello, Python! 

## Escape Characters
print("Hello, \"World\"") # Output: Hello, "World"
print('Hello, \'World\'') # Output: Hello, 'World'
print("Hello, \\World")   # Output: Hello, \World
print("Hello\tWorld")     # Output: Hello   World
print("Hello\nWorld")     # Output: Hello
                          #         World

## Operators

## Arithmetic Operators

a = 5
b = 2
print(a + b)   # Output: 7
print(a - b)   # Output: 3
print(a * b)   # Output: 10
print(a / b)   # Output: 2.5
print(a // b)  # Output: 2
print(a % b)   # Output: 1
print(a ** b)  # Output: 25

# Assignment Operators

x = 100   # Assigns 100 to x
x +=10    # Equivalent to x = x + 10, now x is 110
x -= 2    # Equivalent to x = x - 2, now x is 108
x *= 2    # Equivalent to x = x * 2, now x is 216
x /= 7    # Equivalent to x = x / 7, now x is approximately 30.857142857142858
x //= 2   # Equivalent to x = x // 2, now x is 1.0
x %= 2    # Equivalent to x = x % 2, now x is 1.0
x **= 3   # Equivalent to x = x ** 3, now x is 1.0

# Comparison Operators

a = 10
b = 20

print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)   # Output: False
print(a < b)   # Output: True
print(a >= 10) # Output: True
print(a >= 11) # Output: False
print(b <= 25) # Output: True
print(b <= 19) # Output: False

# Logical Operators

x = 5
y = 10
print(x < y and y > 5)  # Output: True  (both conditions are True)
print(x < y or y < 5)   # Output: True  (one of the conditions is True)
print(not (x < y))      # Output: False (x < y is True, so not makes it False)

# Membership Operators

my_list = [1, 2, 3, 4, 5]
my_string = "Phython"

print(3 in my_list)         # Output: True (3 is in the list)
print(6 in my_list)         # Output: False (6 is not in the list)
print('P' in my_string)     # Output: True (P is in the string)
print('p' not in my_string) # Output: True (p is not in the string)

# Bitwise Operators

a = 5  # In binary: 101
b = 3  # In binary: 011

# Bitwise AND
print(a & b)  # Output: 1 (binary: 001)
# Bitwise OR
print(a | b)  # Output: 7 (binary: 111)
# Bitwise XOR
print(a ^ b)  # Output: 6 (binary: 110)
# Bitwise NOT
print(~a)     # Output: -6 (inverts all bits)
# Left shift
print(a << 1) # Output: 10 (binary: 1010)
# Right shift
print(a >> 1) # Output: 2 (binary: 010)

# Identity Operators

a = [1, 2, 3]
b = a
c = a.copy()
print(a is b)     # Output: True (b is the same object as a)
print(a is c)     # Output: False (c is a copy, not the same object)
print(a is not b) # Output: False (b is the same object as a)
print(a is not c) # Output: True (c is a copy, not the same object)

## Lists

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["apple", 3, True]

# Indexing and Slicing

fruits = ["apple", "banana", "cherry"]

print(fruits[0])          # Output: apple                 +ve indexing
print(fruits[-1])         # Output: cherry                -ve indexing
print(fruits[1:2])        # Output: ['banana', 'cherry']  Slicing 
print(fruits[::2])        # Output: ['apple', 'cherry']   Slicing with step

# Modifying Lists

fruits[1] = "orange"      # Modify an element 
print(fruits)             # Output: ['apple', 'orange', 'cherry']
fruits.append("kiwi")     # Add an element
print(fruits)             # Output: ['apple', 'orange', 'cherry', 'kiwi']
fruits.insert(1, "mango") # Insert an element at index 1
print(fruits)             # Output: ['apple', 'mango', 'orange', 'cherry', 'kiwi']
fruits.remove("orange")   # Remove an element
print(fruits)             # Output: ['apple', 'mango', 'cherry', 'kiwi']
fruits.pop()              # Remove the last element
print(fruits)             # Output: ['apple', 'mango', 'cherry']
fruits.clear()            # Clear the list
print(fruits)             # Output: []

# List functions and methods

fruits = ["apple", "banana", "cherry", "apple"]

print(len(fruits))            # Output: 3 (length of the list)
print(fruits.count("apple"))  # Output: 2 (count of 'apple')
print(fruits.index("banana")) # Output: 1 (index of 'banana')

fruits.sort()                 # Sort the list in place
print(fruits)                 # Output: ['apple', 'banana', 'cherry'] (sorted list)
fruits.reverse()              # Reverse the list in place
print(fruits)                 # Output: ['cherry', 'banana', 'apple'] (reversed list)

numbers = [1, 2, 3]
print(max(numbers))    # Output: 3 (maximum value in the list)
print(min(numbers))    # Output: 1 (minimum value in the list)
print(sum(numbers))    # Output: 6 (sum of the elements in the list)

# Nested Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)       # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]] (2D list)
print(matrix[0])    # Output: [1, 2, 3] (first row)
print(matrix[1][1]) # Output: 5 (element in the second row, second column)

## Tuples

my_tuple = ("apple", "banana", "cherry", "banana")
numbers_tuple = (1, 2, 3, 4)
single_element_tuple = (42,)  # Note the comma for single element

# Indexing and Slicing

print(my_tuple[0])   # Output: apple                 +ve indexing
print(my_tuple[-1])  # Output: cherry                -ve indexing
print(my_tuple[1:3]) # Output: ('banana', 'cherry')  Slicing
print(my_tuple[::2]) # Output: ('apple', 'cherry')   Slicing with step

# Tuple operations and methods

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)   [Concatenation]
tuple3 = tuple1 * 2    # Output: (1, 2, 3, 1, 2, 3)   [Repetition]
print(tuple3)          # Output: (1, 2, 3, 1, 2, 3) 
print(tuple1 *2)       # Output: (1, 2, 3, 1, 2, 3)   [Repetition]

print(len(my_tuple))            # Output: 3 (length of the tuple)
print(my_tuple.count("banana")) # Output: 2 (count of 'banana')
print(my_tuple.index("cherry")) # Output: 2 (index of 'cherry')
print("apple" in my_tuple)      # Output: True (membership test)
print("orange" in my_tuple)     # Output: False (membership test)
print("apple" not in my_tuple)  # Output: False (membership test)

## Sets

fruits_set = {"apple", "banana", "cherry"}
numbers_set = {1, 2, 3, 4, 5}
mixed_set = {"apple", 3, True}

empty_set = set()   # Creating an empty set [not using curly braces]

# Set operations and methods

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2                 # Output: {1, 2, 3, 4, 5}
intersection_set = set1 & set2          # Output: {3}
difference_set = set1 - set2            # Output: {1, 2}
symmetric_difference_set = set1 ^ set2  # Output: {1, 2, 4, 5}

fruits_set = {"apple", "banana", "cherry"}

fruits_set.add("kiwi")          # Add an element
print(fruits_set)               # Output: {'kiwi', 'banana', 'cherry', 'apple'}
fruits_set.remove("banana")     # Remove an element
print(fruits_set)               # Output: {'kiwi', 'cherry', 'apple'}
fruits_set.discard("apple")     # Discard an element (no error if not found)
print(fruits_set)               # Output: {'kiwi', 'cherry'}
fruits_set.pop()                # Remove and return an arbitrary element
print(fruits_set)               # Output: {'kiwi'} (or {'cherry'}, depending on the set)
fruits_set.clear()              # Clear the set
print(fruits_set)               # Output: set() (empty set)

## Dictionaries

default_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

karnataka_food = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa"
}

print(karnataka_food["Mysuru"])                      # Output: Mysore Pak
print(karnataka_food.get("Mangaluru"))               # Output: Neer Dosa
print(karnataka_food.get("Shivamogga", "Not Found")) # Output: Not Found

# Adding, Updating, and Deleting Entries

karnataka_food["Shivamogga"] = "Kadubu"    # Adding a new entry to the dictionary
print(karnataka_food)                  
# Output: {'Bengaluru': 'Bisi Bele Bath', 'Mysuru': 'Mysore Pak', 'Mangaluru': 'Neer Dosa', 'Shivamogga': 'Kadubu'}

karnataka_food["Bengaluru"] = "Ragi Mudde" # Updating an existing entry
print(karnataka_food)
# Output: {'Bengaluru': 'Ragi Mudde', 'Mysuru': 'Mysore Pak', 'Mangaluru': 'Neer Dosa', 'Shivamogga': 'Kadubu'}

mysuru_food = karnataka_food.pop("Mysuru")
print(mysuru_food)                         # Output: Mysore Pak
del karnataka_food["Mangaluru"]
karnataka_food.clear()

# Dictionary Methods

print(karnataka_food.keys())        # Output: dict_keys(['Bengaluru', 'Mysuru', 'Mangaluru'])
print(karnataka_food.values())      # Output: dict_values(['Bisi Bele Bath', 'Mysore Pak', 'Neer Dosa'])
print(karnataka_food.items())       # Output: dict_items([('Bengaluru', 'Bisi Bele Bath'), ('Mysuru', 'Mysore Pak'), ('Mangaluru', 'Neer Dosa')])
new_dishes = {"Hubballi": "Girmit"}
karnataka_food.update(new_dishes)

'''
# Differences Between Lists, Tuples, Sets, and Dictionaries

| Feature         | List               | Tuple              | Set                  | Dictionary          |
|-----------------|--------------------|--------------------|----------------------|---------------------|
| **Ordering**    | Ordered            | Ordered            | Unordered            | Unordered           |
| **Mutability**  | Mutable            | Immutable          | Mutable              | Mutable             |
| **Duplicates**  | Allows duplicates  | Allows duplicates  | No duplicates        | Keys: No duplicates |
| **Indexing**    | Supports indexing  | Supports indexing  | No indexing          | Uses keys           |
| **Structure**   | Indexed collection | Indexed collection | Unordered collection | Key-value pairs     |

'''
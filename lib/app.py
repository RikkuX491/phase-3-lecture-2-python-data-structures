import ipdb

def combine_sequences(seq1, seq2):
    return seq1 + seq2

def sequence_n_times(seq, n):
    return seq * n

def average(seq):
    return sum(seq) / len(seq)

def append_n_times(seq, element, n):
    for i in range(n):
        seq.append(element)
    return seq

# Deliverable # 1: Make a List Comprehension that constructs
#                  a list from the names of the foods. Print
#                  the result to the console.

# Deliverable # 2: Make a List Comprehension that constructs
#                  a list from the prices of the foods. Store
#                  the result of this List Comprehension in a
#                  variable. Then, get the average price of
#                  the prices in the list. Print the result to
#                  the console.

foods = [
    {
        "name": "Flatburger",
        "price": 10.99
    },
    {
        "name": "French Fries",
        "price": 1.99
    },
    {
        "name": "Burrito",
        "price": 7.99
    }
]

# Write Code for Deliverable # 1 here
print([food['name'] for food in foods])

# Write Code for Deliverable # 2 here
prices = [food['price'] for food in foods]
print(sum(prices) / len(prices))

# Deliverable # 3: Make a List Comprehension that constructs a list
#                  such that each item in the list will be in the
#                  following format "{animal['name']} is a {animal['animal_type']}".
#                  Print the result to the console.

animals = [
    {
        "name": "Fido",
        "animal_type": "Dog"
    },
    {
        "name": "Kitty",
        "animal_type": "Cat"
    },
    {
        "name": "Fluffy",
        "animal_type": "Guinea Pig"
    }
]

# Write Code for Deliverable # 3 here
print([f"{animal['name']} is a {animal['animal_type']}" for animal in animals])
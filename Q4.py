# Question 4
# random() is a pseudo-random number generator function that generates a random float number between 0.0 and 1.0:
import random

def generate_random_numbers():
    return [random.randint(1, 50) for _ in range(10)]

def substitute(lst):
    for i in range(len(lst)):
        if lst[i] % 5 == 0:
            lst[i] = lst[i] ** 2

# Generates a list of random integers:
random_list = generate_random_numbers()

print("Before substitution, the list is:", random_list)

substitute(random_list)
print("After substitution, the list is:", random_list)
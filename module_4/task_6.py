import random

number_of_random_numbers = int(input("Arvottavien pisteiden määrä: "))

n = 0
i = 0
while i < number_of_random_numbers:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        n += 1

    i += 1

pi_approximation = 4 * n / number_of_random_numbers

print(f"Pii:n likiarvo arvottavien pisteiden perusteella on {pi_approximation}")


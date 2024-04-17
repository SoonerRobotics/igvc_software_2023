import numpy as np
import math
import random

# exponential

# longer number is 0.0633460851727573
dist_sqrt =.063345

exponential_result = math.exp(-dist_sqrt / (2 * 0.45 ** 2))
print(f"exponential result: {exponential_result}")

# normal distribution
theta_init = 0.0

theta = theta_init

for i in range(10):
    theta = np.random.normal(theta, 0.05) % (2 * math.pi)

    print(f"theta: {theta}\n")

weights = [10, 30, 20, 25, 15]

selected = random.choices(weights, weights, k=1000)
#print(selected)
ones_count = 0
twos_count = 0
threes_count = 0
fours_count = 0
fives_count = 0

for value in selected:
    if value == weights[0]:
        ones_count += 1
    elif value == weights[1]:
        twos_count += 1
    elif value == weights[2]:
        threes_count += 1
    elif value == weights[3]:
        fours_count += 1
    elif value == weights[4]:
        fives_count += 1

print(f"number of ones {ones_count}")
print(f"number of twos {twos_count}")
print(f"number of threes {threes_count}")
print(f"number of fours {fours_count}")
print(f"number of fives {fives_count}")

test_vec = []
test_vec.append(1)
test_vec.append(2)

print(test_vec)
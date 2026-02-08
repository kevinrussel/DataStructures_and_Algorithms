import random

def generate_array(size,low=0,high=1000):
    return [random.randint(low,high) for _ in range(size)]



size = 10

new_arr = generate_array(size = size)

for value in new_arr:
    print(value)
import random

def generate_random_array(size,low=0,high=1000):
    return [random.randint(low,high) for _ in range(size)]







def first_test():
    size_of_arr = [10]
    for key,value in enumerate(size_of_arr):
        print(value)
        arr = generate_random_array(size=value)
        arr.sort()
        print(arr)


if __name__ == "__main__":
    first_test()
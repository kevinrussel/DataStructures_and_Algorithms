import random

def generate_random_array(size,low=0,high=1000):
    return [random.randint(low,high) for _ in range(size)]







def first_test():
    size_of_arr = [10,5,5000,4,6,767,5,0]
    big_array = []
    for key,value in enumerate(size_of_arr):
        arr = generate_random_array(size=value)
        big_array.append(arr)
    return big_array

if __name__ == "__main__":
    first_unsorted_array = first_test()
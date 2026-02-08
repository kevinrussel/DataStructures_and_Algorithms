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

def generate_reversed_array(size):
    return list(range(size,0,-1))

## reversd array
def second_test():
    size_of_arr = [0,50,500,6000,57]
    big_arr  = []
    for value in size_of_arr:
        arr = generate_random_array(size =value)
        big_arr.append(arr)
    return big_arr

## random array
if __name__ == "__main__":
    first_unsorted_array = first_test()
    second_reveresed_array = second_test()
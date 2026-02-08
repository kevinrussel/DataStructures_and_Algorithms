import random

def generate_random_array(size,low=0,high=1000):
    return [random.randint(low,high) for _ in range(size)]







def first_test():
    size_of_arr = [10,50,5,600,7]

    for key,value in enumerate(size_of_arr):
        arr = generate_random_array(size=value)
        print(f'test {key}')



if __name__ == "__main__":
    first_test()
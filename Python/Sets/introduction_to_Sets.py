def average(array):
    # your code goes here
    n_set = set(array)
    average = sum(n_set)/len(n_set)
    return average 

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
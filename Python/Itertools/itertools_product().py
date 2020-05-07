# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

if __name__ == "__main__":
    arr1 = map(int, input().split())
    arr2 = map(int, input().split())
    for item in list(product(arr1, arr2)):
        print(item, end = " ")
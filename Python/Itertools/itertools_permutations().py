# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

if __name__ == "__main__":
    string, n = list(map(str, input().split(' ')))
    string = sorted(string)

    for item in permutations(string, int(n)):
        print(''.join(item))
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

if __name__ == "__main__":
    string, n = list(map(str, input().split()))
    string = sorted(string)
    
    for item in combinations_with_replacement(string, int(n)):
        print(''.join(item))
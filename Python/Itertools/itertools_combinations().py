# Enter your code here. Read input from STDIN. Print output to 
from itertools import combinations 

if __name__ == "__main__":
    string, n = list(map(str, input().split()))
    string = sorted(string)

    for idx in range(1, int(n)+1):
        for item in combinations(string, idx):
            print(''.join(item))


# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

if __name__ == "__main__":
    n = int(input())
    l = list(map(str, input().split()))
    k = int(input())
    count = 0 

    result = list(itertools.combinations(l, k))

    for t in result:
        if 'a' in t:
            count = count + 1

    print(float(count/len(result)))




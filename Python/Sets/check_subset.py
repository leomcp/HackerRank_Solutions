# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())
for _ in range(t):
    n_A = int(input())
    set_A = set(map(int, input().split()))
    n_B = int(input())
    set_B = set(map(int, input().split()))

    print(set_A.issubset(set_B))

        





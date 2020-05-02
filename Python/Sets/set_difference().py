# Enter your code here. Read input from STDIN. Print output to STDOUT

n_A = int(input())
set_A = set(map(int, input().split()))
n_B = int(input())
set_B = set(map(int, input().split()))

set_A_diff_B = set_A.difference(set_B)

print(len(set_A_diff_B))

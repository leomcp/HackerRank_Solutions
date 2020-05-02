# Enter your code here. Read input from STDIN. Print output to STDOUT

n_A = int(input())
set_A = set(map(int, input().split()))

n_B = int(input())
set_B = set(map(int, input().split()))

set_only_English = set_A.difference(set_B)

set_only_French = set_B.difference(set_A)

print(int(len(set_only_English)+len(set_only_French)))


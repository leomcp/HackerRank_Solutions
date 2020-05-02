# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":

    n = int(input())
    set_A = set(map(int, input().split()))
    b = int(input())
    set_B = set(map(int, input().split()))

    a_intersection_b = set_A.intersection(set_B)
    print(len(a_intersection_b))

# Enter your code here. Read input from STDIN. Print output to STDOUT


if __name__ == "__main__":

    n_set_A = int(input())
    set_A = set(map(int, input().split(" ")))

    t = int(input())

    for idx in range(t):
        q = list(map(str, input().split()))
        n_set_B = int(q[1])
        set_B = set(map(int, input().split()))

        if str(q[0]) == "intersection_update":
            set_A.intersection_update(set_B)
        elif str(q[0]) == "update":
            set_A.update(set_B)
        elif str(q[0]) == "symmetric_difference_update":
            set_A.symmetric_difference_update(set_B)
        elif str(q[0]) == "difference_update":
            set_A.difference_update(set_B)

    print(sum(set_A))
        


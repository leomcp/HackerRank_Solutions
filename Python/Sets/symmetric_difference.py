if __name__ == "__main__":
    n = int(input())
    set_A = set(list(input().split()))
    m = int(input())
    set_B = set(list(input().split()))
    
    a_minus_b = set_A.difference(set_B)
    b_minus_a = set_B.difference(set_A)
    diff = a_minus_b.union(b_minus_a)
    arr = list(map(int, diff))
    arr.sort()

    for item in arr:
        print(item)
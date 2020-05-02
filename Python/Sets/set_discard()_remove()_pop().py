if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    t = int(input())
    for _ in range(t):
        query = list(input().split(' '))
        if query[0]=="pop":
            s.pop()
        else:
            s.discard(int(query[1]))
    print(sum(s))

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    runner_up, first = -100, -100 

    for i in arr:
        if first<i:
            runner_up = first 
            first = i 
        elif runner_up<=i and first>i :
            runner_up = i 

    print(runner_up)

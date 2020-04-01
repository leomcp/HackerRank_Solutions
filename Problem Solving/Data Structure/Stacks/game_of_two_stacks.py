def twoStacks(k, a, b):
    #
    # Write your code here.
    #
    count, runSum = 0, 0 

    if len(a) <= len(b):
        x = len(a)
    else:
        x = len(a)

    for i in range(x):
        minelem = min(a[0], b[0])
        runSum = runSum + minelem
        print(runSum, minelem, count, k)
        if runSum >= k:
            return count
        else:
            if minelem == a[0]:
                a.pop(0)
            else:
                b.pop(0)
            count = count + 1 
    return count 

print(twoStacks(10, [4,2,4,6,1], [2,1,8,5]))

17 26 62
7 15 12 0 5 18 17 2 10 15 4 2 9 15 13 12 16
12 16 6 8 16 15 18 3 11 0 17 7 6 11 14 13 15 6 18 6 16 12 16 11 16 11
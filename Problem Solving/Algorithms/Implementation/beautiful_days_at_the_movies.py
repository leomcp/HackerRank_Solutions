def _get_reverse(num):
    rev = 0
    while(num > 0):
        a = num % 10
        rev = rev * 10 + a
        num = num / 10 
    return rev

def beautifulDays(i, j, k):
    noOfBDs = 0 

    for day in range(i, j+1):
        revday = _get_reverse(day)
        diff = abs(revday - day)
        if (diff % k) == 0:
            noOfBDs = noOfBDs + 1

    
    return noOfBDs


print(beautifulDays(13, 45, 3))
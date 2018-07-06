def fibonacci(n):

    # Write your code here.
    if n <= 1:
        return (n, 0)
    else:
        (a,b) = fibonacci(n-1)
        return (a+b, a)

n = int(input())
(a,b) = fibonacci(n)
print(a)
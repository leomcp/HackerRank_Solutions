# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    country_set = set()
    n = int(input())
    for _ in range(n):
        country_set.add(input())
    print(len(country_set))

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":

    k = int(input())
    list_A = list(map(int, input().split()))
    set_A = set(list_A)
    diff = (k * sum(set_A))- sum(list_A)
    print(diff//(k-1)) 

    


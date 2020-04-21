# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":

    input = input().split()
    n = int(input[0])
    m = int(input[1])
    #n = 7
    #m = 21

    design = ".|."
    no_of_design = 1
    no_of_dashes = (m-3)/2
    msg = "WELCOME"

    for i in range(n):
        if i < int((n-1)/2):
            print("-"*int(no_of_dashes)+design*no_of_design+"-"*int(no_of_dashes))
            no_of_design = int(no_of_design + 2)
            no_of_dashes = int((m - (3*no_of_design))/2)
        elif i == int((n-1)/2):
            print("-"*int((m-7)/2)+"WELCOME"+"-"*int((m-7)/2))
        else:
            no_of_design = int(no_of_design-2)
            no_of_dashes = int((m - (3*no_of_design))/2)
            print("-"*int(no_of_dashes)+design*no_of_design+"-"*int(no_of_dashes))


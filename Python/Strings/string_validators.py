if __name__ == '__main__':
    s = input()

    #alphanumeric, alphabetical, digits, lowercase, uppercase
    arr = [False, False, False, False, False]
    
    for char in s:
        if char.isalnum() :
            arr[0] = True

        if char.isalpha() :
            arr[1] = True 

        if char.isdigit():
            arr[2] = True 

        
        if char.islower():
            arr[3] = True

        if char.isupper():
            arr[4] = True 


    for i in arr:
        print(i) 
        

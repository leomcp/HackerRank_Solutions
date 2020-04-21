def count_substring(string, sub_string):
    count = 0 

    for i in range(len(string)-len(sub_string)+1):
        char = string[i]
        if char == sub_string[0]:
            same_char = 1 
            for idx in range(1,len(sub_string),1):
                if string[i+idx]==sub_string[idx]:
                    same_char = same_char + 1 
            if same_char == len(sub_string):
                count = count + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
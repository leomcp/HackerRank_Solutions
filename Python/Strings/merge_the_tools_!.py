def merge_the_tools(string, k):
    u = []
    s = int(len(string)/k)

    for idx in range(s):
        t = string[idx*k : (idx+1)*k]
        u_idx = ""
        for char in t:
            if char not in u_idx:
                u_idx = u_idx + char
        print(u_idx)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

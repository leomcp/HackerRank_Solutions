import itertools
if __name__ == "__main__":
    string = input().strip()
    group = []
    key = []
    for k, g in itertools.groupby(string):
        group.append(list(g))
        key.append(k)
    #print(group)
    #print(key)

    for i in range(len(group)):
        group_length = len(group[i])
        k = int(key[i])
        print(tuple((group_length,k)),end=' ')
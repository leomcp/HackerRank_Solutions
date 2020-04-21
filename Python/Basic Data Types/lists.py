


if __name__ == '__main__':
    data = []
    N = int(input())

    for i in range(N):
        q = input().split()

        if str(q[0])=="insert":
            idx = int(q[1])
            elem = int(q[2])
            data.insert(idx, elem)
        elif str(q[0])=="print":
            print(data)
        elif str(q[0])=="remove":
            elem = int(q[1])
            data.remove(elem)
        elif str(q[0])=="append":
            elem =  int(q[1])
            data.append(elem)
        elif str(q[0])=="sort":
            data.sort()
        elif str(q[0])=="pop":
            data.pop()
        elif str(q[0])=="reverse":
            data.reverse()






class GameStack:

    def __init__(self, data):
        self.data = data
        self.size = len(self.data) 

    def get_size(self):
        return self.size 

    def get_top(self):
        return self.data[0]

    def is_empty(self):
        return self.size==0

    def eliminate_stack(self, x):
        sum = self.get_top()
        if sum >x:
            self.data = []
            self.size = 0 
        else:
            for i in range(1,self.size,1):
                sum = sum + self.data[i]
                if sum<=x:
                    self.data[i] = sum
                elif sum >x:
                    del(self.data[i:])
                    self.size = len(self.data)
                    break

    def print_Stack(self):
        print(self.data)


def twoStacks(x, s1, s2):

    s1 = GameStack(s1)
    #s1.print_Stack()
    s1.eliminate_stack(x)
    s1.print_Stack()
    s1_size = s1.get_size()
    

    s2 = GameStack(s2)
    #s2.print_Stack()
    s2.eliminate_stack(x)
    s2.print_Stack()
    s2_size = s2.get_size()

    if s1_size==0 and s2_size!=0:
        return s2_size
    elif s2_size==0 and s1_size!=0:
        return s1_size 
    elif s1_size!=0 and s2_size!=0:
        max_count = 1 

        for idx1 in range(s1_size):
            val1 = s1.data[s1_size-idx1-1]
            
            for idx2, val2 in enumerate(s2.data):
                total = val1 + val2
                if total<=x:
                    prev_max_count = max_count
                    
                    max_count = max(max_count, ((s1_size-idx1)+idx2+1))
                    print(val1, val2, prev_max_count, max_count)
        return max_count
    else:
        return
    



if __name__ == "__main__":

    #arr2 = [12, 16, 6, 8, 16, 15, 18, 3, 11, 0, 17, 7, 6, 11, 14, 13, 15, 6, 18, 6, 16, 12, 16, 11, 16, 11]
    #arr1 = [7, 15, 12, 0 ,5, 18, 17, 2, 10, 15, 4, 2, 9, 15, 13, 12, 16]

    #print(twoStacks(62arr1, arr2))

    arr1 = [4, 11, 16, 0, 18, 17, 9, 13, 7, 12, 16, 19, 2, 15, 5, 13, 1, 10, 0, 8, 0, 6, 16, 12, 15 ,7, 1, 6, 19, 16, 2]
    arr2 = [15, 8, 11, 16, 6, 0, 5, 11, 7, 9, 8, 6, 3, 3, 4, 8, 17, 14, 9, 5, 15, 15, 1, 19, 10, 0, 12, 8, 11, 9, 11, 18, 17, 14]

    print(twoStacks(5,arr1, arr2))






    
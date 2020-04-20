

class ArrayStack:

    def __init__(self):
        self.data = []
        self.size = 0 

    def push(self, elem):
        self.data.append(elem)
        self.size = self.size + 1

    def pop(self):
        if self.size!=0:
            peek = self.data[-1]
            del(self.data[-1])
            self.size = self.size -1
            return peek 


if __name__ == "__main__":
    
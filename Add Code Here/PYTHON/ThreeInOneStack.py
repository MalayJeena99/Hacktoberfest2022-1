# Three stacks in a single stack

class multistacks:
    def __init__(self, stacksize):
        self.stacknumber = 3
        self.cuslist = [None] * (stacksize * self.stacknumber)
        self.size = [0] * self.stacknumber
        self.stacksize = stacksize

    def __str__(self):
        values = [str(i) for i in self.cuslist]
        return '\n'.join(values)

    def isFull(self, stacknum):
        if self.size[stacknum] == self.stacknumber:
            return True
        else:
            return False

    def isEmpty(self, stacknum):
        if self.size[stacknum] == 0:
            return True
        else:
            return False

    def indexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.size[stacknum] - 1

    def push(self, value, stacknum):
        if self.isFull(stacknum):
            return 'Stack is Full'
        else:
            self.size[stacknum] += 1
            # print(self.size)
            self.cuslist[self.indexOfTop(stacknum)] = value
            return f'Item inserted in stack - {stacknum}'

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return 'Stack is Empty'

        else:
            top = self.cuslist[self.indexOfTop(stacknum)]
            self.cuslist[self.indexOfTop(stacknum)] = None
            self.size[stacknum] -= 1
            return top

if __name__ == '__main__':
    ms = multistacks(3)
    ms.push(10, 1)
    ms.push(20, 1)
    ms.push(30, 1)
    ms.push(40, 1)
    print(ms)
    print('*****************')
    ms.pop(1)
    print(ms)
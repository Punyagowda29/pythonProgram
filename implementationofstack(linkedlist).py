class stacknode:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self, data):
        newNode = stacknode(data)
        newNode.next = self.root
        self.root = newNode
        print ("% d pushed to stack" % (data))

    def pop(self):
        if (self.isEmpty()):
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popp = temp.data
        return popp

    def peek(self):
        if (self.isEmpty()):
            return float("-inf")
        return self.root.data


stack = stack()
stack.push(50)
stack.push(10)
stack.push(80)
print("% d is popped" % (stack.pop()))
print("% d is the peek element" % (stack.peek()))

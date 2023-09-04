class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class linkedlist:
    def __init__(self):
        self.head = None

    def print_ll(self):
        n = self.head
        if n is None:
            print("empty")
        else:
            while n is not None:
                print(n.data)
                n = n.ref
def add_begin(self,data):
    new_node=Node(data)
    new_node.ref=self.head
    self.head=new_node

node1=Node(10)
node1.add_begin(20)
print(print_ll)
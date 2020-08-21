#A class for each node
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    #Function to insert node in a Tree
    def insert(self, data):
    #Compare the new Value with the parent node
        if self.data == data:
            return False
        
        #Insert in the Left if the node is lower
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        #Insert in the Right if it's greater
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
            
    #Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        
        print(self.data)
        
        if self.right:
            self.right.print_tree()

if __name__ == '__main__':
    pass
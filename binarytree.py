from node import Node

#Post order search, Left -> right -> Root
def post_order(root):
    result = []
    if root:
        result = post_order(root.left)
        result = result + post_order(root.right)
        #print(f'El resultado es: {result}')
        result.append(root.data)
        
    return result

def main():

    root = Node(80)
    root.insert(15)
    root.insert(58)
    root.insert(4)
    root.insert(26)
    root.insert(72)
    root.insert(2)
    
    print(f'The Post order traversal is: {post_order(root)}')

if __name__ == '__main__':
    main()
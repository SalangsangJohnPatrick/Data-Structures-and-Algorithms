#JOHN PATRICK M. SALANGSANG
#CS - 201

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.node = data

def preOrder(root):
    if root:
        print(root.node, end=" ")
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.node, end=" ")
        inOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.node, end=" ")

def levelOrder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
 
    while(len(queue) > 0):
        print(queue[0].node, end=" ")
        node = queue.pop(0)
 
        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

#Assign
#Head
root = Node(35)

#Left
root.left = Node(10)
root.left.left = Node(8)
root.left.left.left = Node(6)
root.left.left.right = Node(9)
root.left.right = Node(18)
root.left.right.left = Node(15)
root.left.right.right = Node(28)

#Right
root.right = Node(75)
root.right.left = Node(40)
root.right.left.left = Node(38)
root.right.left.right = Node(45)
root.right.left.right.left = Node(43)
root.right.left.right.right = Node(50)
root.right.left.right.right.left = Node(46)
root.right.left.right.right.right = Node(55)
root.right.right = Node(80)

def options():
    print("[1] Pre Order\n[2] In Order\n[3] Post Order\n[4] Level Order\n[5] Exit")
    try:
        choose = int(input("Choose option: "))
        print()
    except ValueError:
        print("Only enter numeric value.")
        print()
        options()
    else:
        if choose == 1:
            preOrder(root)
            print("\n")
            options()
        elif choose == 2:
            inOrder(root)
            print("\n")
            options()
        elif choose == 3:
            postOrder(root)
            print("\n")
            options()
        elif choose == 4:
            levelOrder(root)
            print("\n")
            options()
        elif choose == 5:
            print("System Exit.")
        else:
            print("Invalid. Try again.")
            options()
options()
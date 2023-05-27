#JOHN PATRICK M. SALANGSANG
#CS - 201

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        
class ColorList:
    def __init__(self):
        self.head = None

    def beginning(self, newData):
        NewNode = Node(newData)
        NewNode.next = self.head
        self.head = NewNode

    def end(self, lastData):
        NewNode = Node(lastData)
        if self.head is None:
            self.head = NewNode
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = NewNode

    def between(self, midNode, midData):
        if midNode is None:
            print("No Node exists.")
            return
        NewNode = Node(midData)
        NewNode.next = midNode.next
        midNode.next = NewNode
    
    def remove(self, removeData):
        Head = self.head
        if Head is not None:
            if Head.item == removeData:
                self.head = Head.next
                Head = None
                return
            
        while Head is not None:
            if Head.item == removeData:
                break
            prev = Head
            Head = Head.next
            
        if Head == None:
            print("The item is not found.")
            return
        prev.next = Head.next
        Head = None
        
    def display(self):
        printLink = self.head
        while printLink != None:
            print(printLink.item)
            printLink = printLink.next

if __name__ == '__main__':
    linkList = ColorList()
        
linkList.head = Node("COLOR")
C1 = Node("RED")
C2 = Node("BROWN")
C3 = Node("ORANGE")
C4 = Node("WHITE")
C5 = Node("GREEN")
C6 = Node("YELLOW")
C7 = Node("PURPLE")
C8 = Node("BLUE")
C9 = Node("PINK")
C10 = Node("BLACK")

linkList.head.next = C10
C10.next = C8
C8.next = C2
C2.next = C5
C5.next = C3
C3.next = C9
C9.next = C7
C7.next = C1
C1.next = C4
C4.next = C6

def menu():
    print("[1] Beginning\n[2] Last\n[3] In Between\n[4] Delete\n[5] Display\n[6] Exit")
    try:
        choice = int(input("Choose: "))
        print()
    except ValueError:
        print("Only enter numeric values. Try again.\n")
        menu()
    else:
        if choice == 1:
            newData = input("Input an item at the beginning: ")
            linkList.beginning(newData)
            linkList.display()
            print()
            menu()
        elif choice == 2:
            lastData = input("Input an item at the end: ")
            linkList.end(lastData)
            linkList.display()
            print()
            menu()
        elif choice == 3:
            midData = input("Input an item in between: ")
            linkList.between(C3.next, midData)
            linkList.display()
            print()
            menu()
        elif choice == 4:
            removeData = input("Remove an item in linked list: ")
            print("Removed item: ", removeData)
            linkList.remove(removeData)
            linkList.display()
            print()
            menu()
        elif choice == 5:
            linkList.display()
            print()
            menu()
        elif choice == 6:
            print("System Exit.")
        else:
            print("Choose again.")
            menu()
menu()
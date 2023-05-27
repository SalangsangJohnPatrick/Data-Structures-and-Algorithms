##JOHN PATRICK M. SALANGSANG
##CS - 201

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

link = LinkedList()

link.head = Node("Jan")
M2 = Node("Feb")
M3 = Node("Mar")
M4 = Node("Apr")
M5 = Node("May")
M6 = Node("June")
M7 = Node("July")
M8 = Node("Aug")
M9 = Node("Sep")
M10 = Node("Oct")
M11 = Node("Nov")
M12 = Node("Dec")

link.head.next = M7
M7.next = M10
M10.next = M12
M12.next = M2
M2.next = M9
M9.next = M5
M5.next = M8
M8.next = M11
M11.next = M4
M4.next = M3
M3.next = M6

while link.head != None:
    print(link.head.data)
    link.head = link.head.next

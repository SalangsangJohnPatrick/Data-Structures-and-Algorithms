#John Patrick M. Salangsang  CS-201
#Keeno C. Cruz
print("John Patrick M. Salangsang\tCS - 201\nKeeno C. Cruz\n")

queue = []
front = 0
rear = -1

def enQueue():
    global front
    global rear
    item = input("Input item to add in the queue: ")
    if len(queue) == 5:
        print("FULL.")
    else:
        queue.append(item)
        print("Front item: ", queue[0])
        print("Front index: ", front)
        print("Rear item: ", queue[-1])
        print("Rear index: ", rear + 1)
        rear += 1
        print("Queues: ", end="")
        for i in queue:
            print(i, end=" ")
        print()
        
def deQueue():
    global front
    global rear
    print("Queues: ", end="")
    for i in queue:
        print(i, end=" ")
    print()
    if len(queue) == 0:
        print("NULL.")
    elif len(queue) == 1:
        pop = queue.pop()
        print("First item in the queue to remove: ", pop)
        front += 1
        print("NULL.")
    else:
        print("First item in the queue to remove: ", queue[0])
        queue.pop(0)
        front += 1
        print("Front item: ", queue[0])
        print("Front index: ", front)
        print("Rear item: ", queue[-1])
        print("Rear index: ", rear)
        print("Queues: ", end="")
        for i in queue:
            print(i, end=" ")
        print()
        
def qOption():
    print("[1] Enqueue\n[2] Dequeue\n[3] Exit")
    try:
        option = int(input("Input Option: "))
    except ValueError:
        print("Please enter numeric value.")
        qOption()
    else:
        if option == 1:
            enQueue()
            print()
            qOption()
        elif option == 2:
            deQueue()
            print()
            qOption()
        elif option == 3:
            print("System Exit...")
        else:
            print("Invalid. Choose again.")
            print()
            qOption()
qOption()

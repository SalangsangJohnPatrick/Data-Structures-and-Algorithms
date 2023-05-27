#John Patrick M. Salangsang  CS-201
#Keeno C. Cruz

stack = []

def push():
    item = input("Input item: ")
    if len(stack) == 5:
        print("Overflow.")
    else:
        stack.append(item)
        print("Top item: ", stack[-1])
        print("Top index: ", len(stack) - 1)
        print("Stack item: ")
        for i in reversed(stack):
            print(i)
        
def pop():
    if len(stack) == 0:
        print("Underflow.")
    else:
        print("Item removed: ", stack[-1])
        stack.pop()
        print("Top index: ", len(stack) - 1)
        print("Stack item: ")
        for i in reversed(stack):
            print(i)

def menu():
    print("Menu:\nPush\t[1]\nPop\t[2]\nExit\t[3]\n")
    try:
        choice = int(input("Input choice: "))
    except ValueError:
        print("Only enter numeric value.")
        menu()
    else:
        if choice == 1:
            push()
            print()
            menu()
        elif choice == 2:
            pop()
            print()
            menu()
        elif choice == 3:
            print("System Exit.")
        else:
            print("Invalid.")
menu() 
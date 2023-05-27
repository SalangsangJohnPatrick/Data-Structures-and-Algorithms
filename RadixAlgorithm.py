##JOHN PATRICK M. SALANGSANG
##CS - 201

##Using counting sort to sort the elements in the basis of significant places.
def ascendingSort(array, place, _pass):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    #Calculate count of elements.
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    #Calculate cummulative count.
    for i in range(1, 10):
        count[i] += count[i - 1]

    #Place the elements in ascending sorted order.
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
    
    for i in range(0, size):
        array[i] = output[i]
        
    print("Pass", _pass[0], ":", *data)
    _pass[0] += 1

def descendingSort(array, place, _pass):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    #Calculate count of elements.
    for i in range(0, size):
        index = 9 - array[i] // place
        count[index % 10] += 1

    #Calculate cummulative count.
    for i in range(1, 10):
        count[i] += count[i - 1]

    #Place the elements in descending sorted order.
    i = size - 1
    while i >= 0:
        index = 9 - array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
    
    for i in range(0, size):
        array[i] = output[i]
        
    print("Pass", _pass[0], ":", *data)
    _pass[0] += 1

#Main function to implement radix sort.
def radixSort(array):
    #Get maximum element.
    maxElement = max(array)

    #Apply counting sort to sort elements based on place value.
    place = 1
    _pass = [1]
    print("\nSort in: \n[a] ASCENDING\n[b] DESCENDING")
    option = input("Enter option: ")
    print()
    while maxElement // place > 0:
        if option == 'a':
            ascendingSort(array, place, _pass)
        elif option == 'b':
            descendingSort(array, place, _pass)
        place *= 10

data = []
print("Input 7 numbers:")
for i in range(0,7):
    x = int(input(""))
    data.append(x)
radixSort(data)
print()

def menu():
    back = input("Back to menu?[Y/N] --> ").upper()
    if back == 'Y':
        radixSort(data)
        print()
        menu()
    elif back == 'N' or back == 'n':
        print("Exit.")
    else:
        print("Invalid. Try again.")
        menu()
menu()

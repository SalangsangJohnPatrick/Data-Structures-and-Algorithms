# LAST ELEMENT
# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)


#FIRST ELEMENT
def pivot(array, start, end):
 
#initializing 
    pivot = array[start]
    low = start + 1
    high = end
 
 
    while True:
   
#moving high towards left
        while low <= high and array[high] >= pivot:
            high = high - 1
 
#moving low towards right 
        while low <= high and array[low] <= pivot:
            low = low + 1
 
#checking if low and high have crossed
        if low <= high:
 
#swapping values to rearrange
            array[low], array[high] = array[high], array[low]
          
        else:
#breaking out of the loop if low > high
            break
 
#swapping pivot with high so that pivot is at its right # #position 
    array[start], array[high] = array[high], array[start]
 
#returning pivot position
    return high
 
 
def quick_sort(array, start, end):
    if start >= end:
        return
 
#call pivot 
    p = pivot(array, start, end)
#recursive call on left half
    quick_sort(array, start, p-1)
#recursive call on right half
    quick_sort(array, p+1, end)
 
 
array = [5,1,3,9,8,2,7]
 
quick_sort(array, 0, len(array) - 1)
print(array)



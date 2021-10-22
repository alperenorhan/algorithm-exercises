from random import randrange


def CreateAnArray(length):
    i = 1
    array = ["0"]
    while i < length:
        array.append(randrange(20))
        i += 1
    return array


def swapFirstAndLastIndex(array):
    temp = array[0]
    array[0] = array[len(array) - 1]
    array[len(array) - 1] = temp
    return array


def Swap(array, index1, index2):
    if index1 == None or index2 == None:
        print("Invalid values have been entered!")
    else:
        temp = array[index1]
        array[index1] = array[index2]
        array[index2] = temp
    print(array)


def BubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if int(array[j]) > int(array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
    print(array)

# Code Results


print("Creating an array")
array = CreateAnArray(10)
print(array)
print("---------------------------")
print("Swap first and last index")
print(swapFirstAndLastIndex(array))
print("---------------------------")
print("Swap the specific indexes")
Swap(array, 3, 7)
print("---------------------------")
print("Bubble Sorting")
BubbleSort(array)
print("---------------------------")

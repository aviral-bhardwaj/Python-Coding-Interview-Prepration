'''Array consists of 0s,1s and 2s write an algorithm
to sort this array in O(n) time complexty with one transverasal'''
############################# AlgoRithm #########
'''lower = 0 middle = 1 and high = 2
if array[mid] = 2 then swapping mid to high and High--
if array[mid] = 0 then swapping mid to low and low ++ ,mid++
if array[mid]=1 then no swap only mid++'''


# Function to sort array


def SortingArrayFunction(Array, ArraySize):
    LowValueofArray = 0
    HighValueofArray = ArraySize - 1  # ArraySize = len(Array)
    MediumValueOfArray = 0

    while MediumValueOfArray <= HighValueofArray:
        if Array[MediumValueOfArray] == 0:
            Array[LowValueofArray], Array[MediumValueOfArray] = Array[MediumValueOfArray], Array[LowValueofArray]
            '''above I am doing swapping  a,b = b,a'''
            LowValueofArray = LowValueofArray + 1
            '''above i am incrementing value of Lowervalue of array by One place'''
            MediumValueOfArray = MediumValueOfArray + 1
            '''above i am incrementing value of Medium value of array by One place'''

        elif Array[MediumValueOfArray] == 1:
            MediumValueOfArray = MediumValueOfArray + 1

        else:
            Array[MediumValueOfArray], Array[HighValueofArray] = Array[HighValueofArray], Array[MediumValueOfArray]
            '''Again I am swapping med to high '''
            HighValueofArray = HighValueofArray - 1

    return Array


'''def PrintingArray(Array):
    for i in Array:
        print(i)'''

# Driver Program


Array = [2, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
ArraySize = len(Array)
result = SortingArrayFunction(Array, ArraySize)
print(result)
print(ArraySize)

# Or

'''array = [0,2,1,2,1,0,2,1,0,2,2,1,1]
array.sort()
print(array)'''
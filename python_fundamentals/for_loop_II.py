
# Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].
def makeItBig(arr):
    for num in range(0, len(arr)):
        if arr[num] > 0:
            arr[num]="big"
    return arr
a = makeItBig([-1, 3, 5, -4])
print(a)


# Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).
def positives(arr):
    count=0
    for num in range(0, len(arr)):
        if arr[num]>0:
            count=count + 1
    arr[-1] = count
    return arr
y = positives([-1,1,1,1])
print (y)

#SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10
def sumTotal(arr):
    sum=0
    for num in range(0, len(arr)):
        sum += arr[num]
    return sum
y = sumTotal([1,2,3,4])
print (y)

# Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5
def findAverage(arr):
    sum=0
    avg=0
    for num in range(0, len(arr)):
        sum += arr[num]
        avg = sum/len(arr)
    return avg
y = findAverage([1,2,3,4])
print (y)


# Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4
def findLength(arr):
    length=0
    for num in range(0, len(arr)):
        length = len(arr)
    return length
y = findLength([1,2,3,4])
print (y)

# Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def findMin(arr):
    minval=arr[0]
    for num in range(0, len(arr)):
        if arr[num]<minval:
            minval=arr[num]
    return minval
y = findMin([2,3,4])
print (y)

# Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.
def findMax(arr):
    maxval=arr[0]
    for num in range(0, len(arr)):
        if arr[num]>maxval:
            maxval=arr[num]
    return maxval
y = findMax([2,3,4])
print (y)

# UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.
def ultimateAnalyze(arr):
    length=0
    minval=arr[0]
    maxval=arr[0]
    length=0
    sum=0
    avg=0
    ultimate = {}
    for num in range(0, len(arr)):
        length = len(arr)
        sum += arr[num]
        avg = sum/length
        if arr[num]<minval:
            minval=arr[num]
        if arr[num]>maxval:
            maxval=arr[num]
    ultimate['sumTotal'] = sum
    ultimate['average'] = avg
    ultimate['minimum'] = minval
    ultimate['maximum'] = maxval
    ultimate['arraylength'] = length
    return ultimate
y = ultimateAnalyze([1,2,3,4])
print (y)


# ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews
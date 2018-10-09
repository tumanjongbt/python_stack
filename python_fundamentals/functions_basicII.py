def countdown(num):
    arr=[num]
    for i in range(arr,0,-1):
        print(num[i])
countdown(5) 

def printReturn(arr):
    print (arr[0])
    return arr[1]
x=printReturn([5,4])
print(x)

def firstPlusLength(arr): 
    return arr[0] + len(arr)
x= firstPlusLength([5,4,3,2,1])
print(x)


def greaterThanSecond(arr):
    newArray = []
    for value in arr:
        if arr[value] > arr[1]:
            newArray.append(arr[value])
    print(newArray)
    print(len(newArray))
    if len(arr) == 0:
        return False
greaterThanSecond([10,4,15,4,8])

def this_that(x,y):
    sub_arr = []
    for i in range(0, x):
        sub_arr.insert(i, y)
        return sub_arr

myList=this_that(3,4)
print(myList)
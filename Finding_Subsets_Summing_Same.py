# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 22:33:07 2019

@author: Ike Osafo
"""

"""Find if any two subsets gives the same sum 
Using a recursive solution with memoization"""

#Uses set for memoization
def subsetExists(arr):
    listSize = len(arr)
    currentItem = 0
    currSum = 0
    memoiDict = set()
    for x in range(listSize):
        currentItem = arr[x]
        currSum += currentItem
        arr.pop(x)
        #call recursive function on this
        if(findSubsetRecurse(currSum, arr, memoiDict)):
            return True
        #insert this back again ... #stores this set as a wrong trail
        memoiDict.add(str(arr))
        arr.insert(x, currentItem)
        currSum -= currentItem
    return False


#define recursive function here
#instead of calling sum(iterable/list)... you could store the array as a string into a dictionary
#like: sumDict = new dict() and store as sumDict.append(Str([1, 2, 3]), sum) so that you can easily 
#retrieve it next time
def findSubsetRecurse(currSum, newArr, memoiDict):
    if(currSum == sum(newArr)):
        print("The sum is: " + str(currSum))
        return True
    
    #check if trail has already been taken...
    if(str(newArr) in memoiDict):
        return False
        
    #handle case where it isn't
    currentItem = 0
    for x in range(len(newArr)):
        currentItem = newArr[x]
        currSum += currentItem
        newArr.pop(x)
        #call recursive function on this
        if(findSubsetRecurse(currSum, newArr, memoiDict)):
            return True
        #insert this back again
        memoiDict.add(str(newArr))
        newArr.insert(x, currentItem)
        currSum -= currentItem
    return False

#define the def __name__ = "__main__":
if __name__=="__main__":
    arr = [15, 5, 20, 10, 35, 15, 10]
    if(subsetExists(arr)):
        print("Yes such sets exist")
    else:
        print("Sorry couldn't find those pair")


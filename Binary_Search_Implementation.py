# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:34:07 2019
@author: Isaac Osafo
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:41:51 2019
Implementing both recursive binary search and iterative binary searches
@author: ikeos
"""
# recursive binary search implementation
def recurseBinSearch(arrList, k):
    if k is None:
        return True
    #call the recursive functions
    length = len(arrList)
    return retNumber(arrList, 0, length, k)
    
#helper function for the binary search
def retNumber(arrList, left, right, k):
    length = len(arrList)
    if left == right:
        return False
    
    #find it from remaining 
    newMidpoint = int(left + (right - left)/2)
    if k > arrList[newMidpoint]:
        return retNumber(arrList, newMidpoint + 1, right, k)
    elif k < arrList[newMidpoint]:
        return retNumber(arrList, left, newMidpoint, k)
    else:
        #meaning it was found
        return True


# iterative binary serach implementation
def iterBinSearch(arrList, k):
    if k is None:
        return True
    #Otherwise run through the algorithm
    left = 0
    right = len(arrList)
    while left != right:
        newMidpoint = int(left + (right - left)/2)
        if k > arrList[newMidpoint]:
            left = newMidpoint + 1
        elif k < arrList[newMidpoint]:
            right = newMidpoint
        else:
            #meaning it was found
            return True
    
    #at this point return false because it couldn't be found
    return False
    

#Validating our results
if __name__ == "__main__":
    arrList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 1
    #recursive algorithm
    if recurseBinSearch(arrList, k):
        print(str(k) + " was found using recursive Binary Search")
    else:
        print("Coundn't find item using recursive Binary Search");
    
    #iterative algorithm
    if iterBinSearch(arrList, k):
        print(str(k) + " was found using iterative Binary Search")
    else:
        print("Coundn't find item using iterative Binary Search");
        
        
        
        
    
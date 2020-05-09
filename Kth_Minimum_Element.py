# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:41:51 2019
Kth smallest element using maximum heap implementation

We use recursive Binary Search to arrive at best case O(klogn) or worse O(kn) 
@author: ikeos
"""
# iterative binary serach implementation
def createMaxHeap(arrList):
    #start from the children and create the heap
    length = int(len(arrList)/2)
    print(length)
    for i in sorted(range(length), reverse=True):
        print(arrList)
        arrList = heapify(arrList, i)
    #print out the array
    for num in arrList:
        print(num)
        
# inserts a child element into the heap
def heapify(arrList, k):
    if k == 0:
        return arrList
    
    print(k)
    
    #otherwise swap and heapify
    length = len(arrList)
    parent = arrList[int(k/2)]
    curr = arrList[k]
    if curr > parent:
        arrList[int(k/2)] = arrList[k]
        arrList[k] = parent
        print("swap done")
        
    #new index
    k -= 1
    return heapify(arrList, k)
    
#This method inserts into the heap
#Algorithm: input at the last end + push up
def insertIntoHeap(heapArr, item):
    length = len(heapArr)
    heapArr.insert(length, item)
    return heapify(heap)

#remove largest element
'''by 1. remove last
      2. add least to the first place 
      3. heapify
'''
def removeLargest(heapArr):
    heapArr[0] = heapArr[len(heapArr) - 1]
    heapArr.pop()
    #boggle down the list
    curr = heapArr[0]
    if len(heapArr) >= 1:
        if heapArr[0] < heapArr[1]:
            heapArr[0] = heapArr[1]
            heapArr[1] = curr
            return boggleDown(heapArr, 1)
    
#boggle the rest down
def boggleDown(heapArr, index):
    nextIndex = index
    curr = heapArr[index]
    if (index*2 + 1) < len(heapArr) and heapArr[index] < heapArr[index*2 + 1]:
        nextIndex = index*2 + 1
    if (index*2 + 2) < len(heapArr) and heapArr[index] < heapArr[index*2 + 2]:
        nextIndex = index*2 + 2
    
    #swap the items
    if nextIndex == index:
        return heapArr
    else:
        heapArr[index] = heapArr[nextIndex]
        heapArr[nextIndex] = curr
        return boggleDown(heapArr, nextIndex)
    
#k will always be smaller than arrList
def findKthElem(arrList, k):
    arrLen = len(arrList)
    if len(arrList) == 0 or k > len(arrList):
        return -1
    
    #create the max heap with k elements
    heapArray = arrList.copy()
    heapArray = heapArray[0:k]
    print(heapArray)
    heapArray = createMaxHeap(heapArray)
    
    #for the rest of the data, insert into the heap and boggle down
    for i in range(arrLen - k):
        newIndex = k + i + 1
        if newIndex < arrLen:
            if arrList[newIndex] < heapArray[0]:
                heapArray = removeLargest(heapArray)
                heapArray = insertIntoHeap(heapArray, arrList[newIndex])
    
    #The heap would contain K small items with first item being the answer
    return heapArray[0]
                

#Validating our results
if __name__ == "__main__":
    arrList = [4, 2, 1, 3, 5, 9, 8, 5, 7]
    k = 3
    kthElement = findKthElem(arrList, k)
    print("Our " + k + "th Element is: "+ kthElement)
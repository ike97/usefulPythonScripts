# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 12:26:35 2019
Sort a LinkedList using mergeSort
@author: Ike Osafo
"""

# Algorithm:
#1. Collect all the data into a list and pass that list into a mergeSort
#2. Reconstruct the linked list

#This defines the Node class that we'll be using
class Node:
    def __init__(self, value=None):
        self.next = None
        self.value = value
        
    def __str__(self):
        return self.value
        
    def setNextNode(self, node):
        self.next = node
        
    def getNextNode(self):
        return self.next
    
    def setData(self, value):
        self.value = value
        
    def getData(self):
        return self.value
    

# return a list of the nodes
def getDataList(headNode):
    newList = list()
    while headNode is not None:
        newList.append(headNode)
        headNode = headNode.getNextNode()
    return newList

#implements MergeSort --- recursive search
def mergeSort(dataList):
    #split list into two and call the mergeSort
    if len(dataList) <= 1:
        #because this is considered sorted
        return dataList
    #break the list into two and pass them
    splitLength = int(len(dataList)/2)
    dataList1 = dataList[0:splitLength]
    dataList2 = dataList[splitLength : len(dataList)]
    #sort them
    sortedList1 = mergeSort(dataList1)
    sortedList2 = mergeSort(dataList2)
    newList = combineData(sortedList1, sortedList2)
    #print([str(x) for x in newList])
    return newList

#this function combines the list items from both sets
def combineData(list1, list2):
    newList = list()
    counter1 = 0
    counter2 = 0
    while True:
        if counter1 < len(list1) and counter2 < len(list2):
            if(list1[counter1].getData() < list2[counter2].getData()):
                newList.append(list1[counter1])
                counter1 += 1
            elif (list1[counter1].getData() == list2[counter2].getData()):
                newList.append(list1[counter1])
                newList.append(list2[counter2])
                counter1 += 1
                counter2 += 1
            else:
                newList.append(list2[counter2])
                counter2 += 1
        elif counter1 < len(list1) and counter2 == len(list2):
            newList.append(list1[counter1])
            counter1 += 1
        elif counter1 == len(list1) and counter2 < len(list2):
            newList.append(list2[counter2])
            counter2 += 1
        else:
            break
    
    #return the new list of items
    return newList

#constructs new linked list
def constructNewList(dataList):
    if len(dataList) == 0:
        return None
    
    headNode = dataList[0]
    length = len(dataList)
    for i in range(length):
        if i + 1 < length:
            headNode.setNextNode(dataList[i + 1])
            headNode = dataList[i + 1]
        else:
            headNode.setNextNode(None)
    
    #grab the head node again and return it
    return dataList[0]

# handles major calls
def sortLinkedList(linkedNode):
    newList = getDataList(linkedNode)
    
    sortedList = mergeSort(newList)
    linkedListHead = constructNewList(sortedList)
    return linkedListHead
    

#try and validate this:
if __name__ == "__main__":
    one = Node("1")
    two = Node("2")
    three = Node("3")
    four = Node("4")
    five = Node("5")
    
    one.setNextNode(four)
    two.setNextNode(five)
    five.setNextNode(three)
    four.setNextNode(two)
    
    mainStringList = ""
    node = one
    while node is not None:
        mainStringList += node.getData() + " "
        node = node.getNextNode()
    print("Old List: "+ mainStringList)
    
    #call the function
    newList = ""
    node = sortLinkedList(one)
    while node is not None:
        newList += node.getData() + " "
        node = node.getNextNode()
    print("New List: "+ newList)
    
    
    
    
    
    
    
    
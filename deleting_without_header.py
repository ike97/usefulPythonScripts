# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 08:47:17 2019
Deleting a Node without header
@author: ikeos

Deleting a node from a linkedList
"""

#This defines the Node class that we'll be using
class Node:
    def __init__(self, value=None):
        self.next = None
        self.value = value
        
    def setNextNode(self, node):
        self.next = node
        
    def getNextNode(self):
        return self.next
    
    def setValue(self, value):
        self.value = value
        
    def getValue(self):
        return self.value

        

#Assuming inputs are only strings
def deleteNode(node):    
    #because last node links to a node that is none
    if node is None:
        return
    
    while node is not None:
        nextNode = node.getNextNode()
        if nextNode is not None:
            node.setValue(nextNode.getValue())
            if nextNode.getNextNode() is None:
                node.setNextNode(None)
                break
            else:
                node = nextNode
        else:
            node.setValue(None)
            node = nextNode

if __name__ == "__main__":
    #create some nodes and delete the one you want
    firstNode = Node("1")
    secNode = Node("2")
    thirdNode = Node("3")
    fourthNode = Node("4")
    fifthNode = Node("5")
    firstNode.setNextNode(secNode)
    secNode.setNextNode(thirdNode)
    thirdNode.setNextNode(fourthNode)
    fourthNode.setNextNode(fifthNode)
    
    mainStringList = ""
    node = firstNode
    while node is not None:
        mainStringList += node.getValue() + " "
        node = node.getNextNode()
    
    print("Our old list is: "+ mainStringList)

    #call delete on second node
    deleteNode(firstNode)
    
    #this prints out the nodes
    stringList = ""
    node = firstNode
    while node is not None:
        if node.getValue() is not None:
            stringList += node.getValue() + " "
        node = node.getNextNode()
    
    print("Our new list is: "+ stringList)
            
        
        
                
            
        
    
    
        

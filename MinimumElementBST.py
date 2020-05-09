# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:28:15 2019
Minimum element in BST
@author: ikeos
"""

#Knowing that the BST has least value (on left) and largest value (right)
#Class we will use to test our code
class Node(object):
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    
    def __str__(self):
        #retutn only the data
        return self.data
    
    def getData(self):
        return self.data
    
    def setData(self, data=None):
        self.data = data
    
    def getLeftNode(self):
        return self.left
        
    def setLeftNode(self, node=None):
        self.left = node
        
    def getRightNode(self):
        return self.right
    
    def setRightNode(self, node=None):
        self.right = node
        

#returns minimum element
#simply traverse to the very bottom of the BST
def retMinimumElem(root):
    if root is None:
        return -1
    #simply go down the left path until the very bottom
    while not isLeafNode(root):
        root = root.getLeftNode()
    #at this point we have the leftmost leaf so return digit
    return root.getData()


#checks if it is root
def isLeafNode(node):
    return node.getLeftNode() == None and node.getRightNode() == None

if __name__=="__main__":
    #construct you BST here
    one = Node(None, None, "1")
    two = Node(None, None, "2")
    three = Node(None, None, "3")
    four = Node(None, None, "4")
    five = Node(None, None, "5")
    
    three.setLeftNode(two)
    two.setLeftNode(one)
    three.setRightNode(four)
    four.setRightNode(five)
    
    #Apply algorithm and print answer (input = root)
    minElement = retMinimumElem(three)
    print("Minimum Element in Tree: "+ minElement)
    
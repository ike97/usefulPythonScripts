# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:02:22 2019
Mirroring a Binary tree
@author: Ike Osafo
"""

#Mirror a tree
#This algorithm simply uses a post traversal to duplicate the tree 

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

#The function that mirrors the tree
#create a whole new tree...
def mirrorTree(headNode):
    #start up the recursive algorithm
    newHead = createNewTree(headNode)
    return newHead

def createNewTree(headNode):
    if isleafNode(headNode):
        newNode = Node()
        newNode.setData(headNode.getData())
        return newNode
        
        
    #construct the recursive case
    leftNode = createNewTree(headNode.getLeftNode())
    rightNode = createNewTree(headNode.getRightNode())
    newNode = Node(rightNode, leftNode, headNode.getData())
    return newNode

#checks if the node is a leaf Node
def isleafNode(node):
    return node.getRightNode() is None and node.getLeftNode() is None

#Pre-order traversal of tree
def getStrTree(node, strings):
    if isleafNode(node):
        strings += node.getData() + " "
        return strings
    
    strings += node.getData() + " "
    leftString = getStrTree(node.getLeftNode(), strings)
    rightString = getStrTree(node.getRightNode(), leftString)
    return rightString

#test the algorithm 
if __name__ == "__main__":
    one = Node(None, None, "1")
    two = Node(None, None, "2")
    three = Node(None, None, "3")
    four = Node(None, None, "4")
    five = Node(None, None, "5")
    
    one.setLeftNode(two)
    one.setRightNode(three)
    two.setLeftNode(four)
    two.setRightNode(five)
    
    #get the string representation
    myStr = getStrTree(one, "")
    print("Initial Tree: " + myStr)
    
    #Mirrored tree
    newHead = mirrorTree(one)
    myStr = getStrTree(newHead, "")
    print("Mirrored Tree: " + myStr)
    
    
        
        
    
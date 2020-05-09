# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 05:50:48 2018

@author: ikeos
"""
import sqlite3
import string
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, inch
from reportlab.lib.colors import red, blue, green, black, yellow
from reportlab.lib.pagesizes import letter, A4

def getInput(userAction):
    while (userAction not in [1, 2, 3]):
        if userAction == 0:
            return
        question = "What do you want to do today? \n 1. Create a table"
        question += "\n 2. Print out an existing table \n 3. Modify an existing table"
        question += "\n 0. Enter 0 to exit the program \n Response: "
        userAction = input(question)
        userAction = int(userAction)
    return userAction

#this is where the program starts
bD = sqlite3.connect("Brotherhood.db")

userAction = -1
userAction = getInput(userAction)
#intialize the modifyaction and table name with "null values"
modifyAction = -1
tableName = ""
if (userAction in [1, 2, 3]):
    #get table name
    while tableName == "":
        tableName = input("Please enter the name of the table (q == quit) \n Response: ")
        if tableName == "q" or tableName == "Q":
            tableName = ""
            break
    tableName = tableName.strip().upper()
    
    #get the modification action
    if (userAction == 3):
        while (modifyAction not in [1, 2, 3]):
            if modifyAction == 0:
                break
            modifyAction = input(''' Which modification do you want to do?
                                 \n 1. Add an entry into an existing table
                                 \n 2. Delete an item from an existing table
                                 \n 3. Change the value of an already existing input
                                 \n 0. Enter 0 to exit the program
                                 ''')
            modifyAction = int(modifyAction)

if (userAction == 1 and tableName != ""):
    strTable = str("CREATE TABLE %s (id INTEGER AUTO_INCREMENT, name TEXT);" %tableName)
    bD.execute(strTable)
    print ("Database table, with name %s has been successfully created" %tableName)
    
if (tableName is not ""):
    bD.execute("DROP TABLE %s" %tableName)
    print ("Successfully deleted table")
    bD.close
    print ("Successfully detached database")
    

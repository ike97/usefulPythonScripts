# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 23:25:47 2019

@author: ikeos
"""
import os

def readFile():
    string = "Do you want to (Enter Number):\n\t(1) Create New Host File \n\t(2) Append to Existing File \n"
    user_in = input(string)
    code = "0.0.0.0"
    if int(user_in) == 1:
        if os.path.exists("hosts.txt"):
            os.remove("hosts.txt")
        with open ("hosts.txt", "x") as infile:
            f = open("Streaming_Site.txt", "r")
            for line in f:
                n_string = code + " " + line
                infile.write(n_string)
            print("created new info")
            f.close()
    elif int(user_in) == 2:
        if os.path.exists("hosts.txt"):
            fl = open("hosts.txt", "r")
            checkFirstContent = False
            skip = False
            f = open("Streaming_Site.txt", "r")
            for line in f:
                if checkFirstContent == False:
                    arr = fl.readline().split(" ")
                    codePart = arr[0]
                    stringPart = arr[1]
                    if codePart == code and stringPart == line:
                        string = "Seems info might already exist. Should we proceed?\n\t\tYes\n\t\tNo\n"
                        answer = input(string)
                        if answer.lower() == "yes": 
                            skip = False
                            checkFirstContent = True
                            fl = open("hosts.txt", "a")
                            print("appending new info")
                        else:
                            skip = True
                    else: 
                        checkFirstContent = True
                        fl = open("hosts.txt", "a")
                        print("appending new info")
                if skip:
                    break
                n_string = code + " " + line
                fl.write(n_string)
            f.close()
            fl.close()

        

#Prints out the content of the newly created file
def printFile():
    with open ("hosts.txt", "r") as infile:
        for line in infile:
            print(line)
            
readFile()
printFile()
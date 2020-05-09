# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:31:40 2019

@author: Ike Osafo
"""

def findWordInPuzzle(puzzle, word):
    rowLength = len(puzzle)
    #catch a couple of cases before descending it the recursion
    if rowLength == 0:
        if len(word) == 0:
            return True
        else:
            return False
    else:
        if len(word) == 0:
            return True
        else:
            columnLength = len(puzzle[0])
            #assumption here is that since it's a square matrix, if first row array's size == 0, then all 
            #the row arrays will also be zero...
            if columnLength == 0:
                return False
            else:
                for row in range(rowLength):
                    for col in range(columnLength):
                        #edit the word to be passed into the recursive function
                        newWord = ""
                        if(puzzle[row][col].lower() == word[0].lower()):
                            print(puzzle[row][col])
                            newWord = word[1: len(word)]
                            if(findWordRecurse(puzzle, rowLength, columnLength, row, col, newWord)):
                                return True
                return False



#defining the recursive function
def findWordRecurse(puzzle, rowLength, colLength, row, col, word):
    if(len(word) == 0):
        return True
    
    #else recurse through the puzzle
    if row + 1 < rowLength and puzzle[row + 1][col].lower() == word[0].lower():
        print(puzzle[row + 1][col])
        if(findWordRecurse(puzzle, rowLength, colLength, row + 1, col, word[1:len(word)])):
            return True
    
    #at this point we have to try going down and see if we're able to find it
    if col + 1 < colLength and puzzle[row][col + 1].lower() == word[0].lower():
        print(puzzle[row][col + 1])
        if(findWordRecurse(puzzle, rowLength, colLength, row, col + 1, word[1:len(word)])):
            return True
    
    #at this point we know that the word doesn't exist in the puzzle
    return False



#Testing algorithm
if __name__=="__main__":
    #create the sample array
    puzzle1 = [['M', 'F', 'O', 'Q'], ['O', 'O', 'A', 'P'], ['A', 'M', 'M', 'B'], ['E', 'A', 'S', 'S']]
    puzzle2 = []
    puzzle3 = [['A']]
    puzzle4 = [[], [], []]
    puzzle5 = [['D', 'R', 'E'], ['E', 'N', 'Z'], ['R', 'E', 'D']]
    assert findWordInPuzzle(puzzle1, "FOAM") == True, "THERE'S AN ERROR IN YOUR LOGIC"
    assert findWordInPuzzle(puzzle2, "MINE") == False, "THERE'S AN ERROR IN YOUR LOGIC"
    assert findWordInPuzzle(puzzle3, "A") == True, "THERE'S AN ERROR IN YOUR LOGIC"
    assert findWordInPuzzle(puzzle4, "ANY") == False, "THERE'S AN ERROR IN YOUR LOGIC"
    assert findWordInPuzzle(puzzle5, "RED") == True, "THERE'S AN ERROR IN YOUR LOGIC"
        
            
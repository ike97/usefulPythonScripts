# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 13:35:20 2018

@author: ikeos
"""
from graphics import *

def main():
    win = GraphWin("Game Window", 200, 200)
    c = Image(Point(0,0), "blue_sea.gif")
    c.draw(win)
    win.getMouse()
    win.close()

main()


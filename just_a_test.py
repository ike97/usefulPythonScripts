# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 00:34:02 2018

@author: ikeos
"""

class myCars:
    def _init_(self, name, carType, carId):
        self.name = name
        self.carType = carType
        self.carId = carId
    
    def outputData(self):
        print ("Car's name = ", self.name)
        print ("Car's type = ", self.carType)
        print ("Car's id = ", self.carId)
    
myCar = myCars()
myCar.name = "HD-PAJARO"
myCar.carType = "Honda"
myCar.carId = 555

myCar.outputData()
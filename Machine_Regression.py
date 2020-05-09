# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 06:35:00 2018

@author: ikeos
"""

import pandas as pd
import quandl as qd

df = qd.get('WIKI/GOOGL')
print(df.head())

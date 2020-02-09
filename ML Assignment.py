# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 00:53:47 2020

@author: Tintin
"""

import datetime
cur = datetime.datetime.fromisoformat('2015-01-01T00:00:00')
cur2 = datetime.datetime.fromisoformat('2020-01-01T00:00:00')
import random
lst = []
lst2 = []
while(cur < cur2):
	lst.append(cur)
	x = random.randint(120, 300)
	cur = cur + datetime.timedelta(seconds = x)
	lst2.append(random.randint(1, 10))
api = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
for i in range(len(lst)):
	api[lst2[i]-1][lst[i].date().year - 2015] = api[lst2[i]-1][lst[i].date().year - 2015] + 1


import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('2015', '2016', '2017','2018', '2019')
y_pos = np.arange(len(objects))
for i in range(5):    
    performance = api[i]
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Usage')
    plt.title('API usage')
    plt.show()
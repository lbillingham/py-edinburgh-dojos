import matplotlib.pyplot as plt
import numpy as np
import random

DUMB_LIMIT = 10

class Drip(object):
    def __init__(self, start_x, start_y, start_thick, color, angle):
        self.start_x = start_x
        self.start_y = start_y
        self.start_thick = start_thick 
        self.color = color
        self.angle = angle
        self.scale = start_thick
        
    def __next__(self):
        #advance x, y by a random number
        #reduce scale by a random number
        delta_x = np.random.uniform(low=1e-8, high=1e-1, size=(1,))[0]
        delta_y = np.tan(np.radians(self.angle)) * delta_x
        self.x += delta_x
        self.y += delta_y
        self.angle += np.random.uniform(low=2, high=3, size=(1,))[0]
        self.scale -= np.random.uniform(low=0.6, high=0.9, size=(1,))[0]
#TODO reduce alpha at each iteration where all x's and y's infact    
        if abs(self.x) > DUMB_LIMIT:
            raise StopIteration  
            
        if abs(self.y) > DUMB_LIMIT:
            raise StopIteration
            
        if self.scale < 0.0001:
            raise StopIteration
        
              
        return self.x, self.y, dict(c=self.color, 
                   s=self.scale, alpha=0.5, edgecolors='none')
        
        
    def __iter__(self):
        self.x = self.start_x
        self.y = self.start_y     
        return self
       
    
colors = ['red', 'green', 'blue', 'orange', 'yellow', 'purple']
for i in range(25  0):    
    color = random.choice(colors)
    scale = np.random.uniform(low=200, high=300, size=(1,))[0]
    x = np.random.uniform(low=0, high=1, size=(1,))[0]
    y = np.random.uniform(low=0, high=1, size=(1,))[0]    
    angle = np.random.uniform(low=-180, high=180, size=(1,))[0]
    drip = Drip(x, y, scale, color, angle)
    for x, y, path_segment in drip:
        print(x, y, path_segment['s'], path_segment['c'])
        plt.scatter(x, y, **path_segment)





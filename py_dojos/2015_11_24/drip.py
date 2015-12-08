import matplotlib.pyplot as plt
import numpy as np
import itertools

DUMB_LIMIT = 30

class Drip(object):
    def __init__(self, start_x, start_y, start_thick, color, start_angle):
        self.x = start_x
        self.y = start_y
        #   self.start_thick = start_thick 
        self.color = color
        self.angle = start_angle
        self.scale = start_thick
        
    def __next__(self):
        #advance x, y by a random number
        #reduce scale by a random number
        step = np.random.uniform(low=1e-3, high=1e-1, size=(1,))[0]
        delta_x = np.cos(np.radians(self.angle)) * step
        delta_y = np.tan(np.radians(self.angle)) * delta_x
        self.x += delta_x
        self.y += delta_y
        self.angle += np.random.uniform(low=-2, high=2, size=(1,))[0]
        self.scale -= np.random.uniform(low=0.55, high=0.85, size=(1,))[0]
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
        return self
       
    
fig, ax = plt.subplots(1)
colors = itertools.cycle(['red', 'green', 'blue', 'orange', 'yellow', 'purple'])
for i in range(50):    
    color = next(colors)
    scale = np.random.uniform(low=200, high=300, size=(1,))[0]
    x = np.random.uniform(low=-30, high=30, size=(1,))[0]
    y = np.random.uniform(low=-30, high=30, size=(1,))[0] 
    angle = np.arccos(np.random.uniform(low=-1, high=1, size=(1,))[0])
    angle = np.degrees(angle)
    drip = Drip(x, y, scale, color, angle)
    for x, y, path_segment in drip:
        #print(x, y, path_segment['s'], path_segment['c'])
        ax.scatter(x, y, **path_segment)

ax.set_ylim([-(DUMB_LIMIT-1), (DUMB_LIMIT-1)])
ax.set_xlim([-(DUMB_LIMIT-1), (DUMB_LIMIT-1)])
ax.set_yticks([])
ax.set_xticks([])



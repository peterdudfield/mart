import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import numpy as np
from datetime import datetime

#colors = ['#0000ff','#ff0000','#00ff00','#ffff00','#00ffff','#ff00ff'] '#rgb
#colors = ['#000000','#333333','#666666','#888888','#aaaaaa','#cccccc'] #greyscale
#colors = ['#ffffff','#cccccc','#999999','#777777','#555555','#333333'] #greyscale start swith white
#colors = ['#ff4e50','#fc913a','#f9d62e','#8bc34a','#e2f4c7','#fd5a40'] #summer
#colors = ['#a5ccea','#96b1d0','#e7fafb','#dddddd','#68b6c1','#6b8fb0'] #winter
#colors = ['#ea8200','#bd0000','#fdcc00','#c97a00','#8b0023','#9cb329'] #autumn
# colors = ['#22cc22','#fdc010','#bb77ee','#ee7777','#09bcd3','#f1c0f6'] #spring

          
class Fractals(object):
    """
       Class with commmon functions to produce fractual images.
       Written on 20.11.17 by sw pased on pd's original 'square' and 'triangle' scripts
    """

    def __init__(self, sides, name, N_layers,season = 'summer'):
        """sides = number of sides of shape - can only be 3 or 4 currently, name = string of name of shape, N_layers - number of layers"""

        self.patches = []
        self.sides= sides
        self.name = name
        self.N_layers = N_layers
        self.season = season

        if self.sides not in range(3,5):
            ValueError
            print('You have entered an invalid number of sides, enter 3 or 4')

        if season == 'summer':
            self.colors_season = ['#ff4e50','#fc913a','#f9d62e','#8bc34a','#e2f4c7','#fd5a40'] #summer
        if season == 'winter':
            self.colors_season = ['#a5ccea','#96b1d0','#e7fafb','#dddddd','#68b6c1','#6b8fb0'] #winter



    def make_shape_from_verticie(self,p1,p2,r,overall_level,shape_level):

        x1 = p1[0]*2/3+p2[0]*1/3
        y1 = p1[1]*2/3+p2[1]*1/3
        x2 = p1[0]*1/3+p2[0]*2/3
        y2 = p1[1]*1/3+p2[1]*2/3

        #Height and rotation won't generalise to other polgons - pete need your input on that
        rotation = ((-1)**(self.sides-1))*(r + self.sides - 3)*(np.pi*2/self.sides) + np.pi*(shape_level % 2)
        
        #squares
        #rotation = -1*(r+1)*np.pi*2/4 + np.pi*(shape_level % 2)
        #print(shape_level,r,rotation/np.pi*180 % 360,x1,y1,x2,y2)
        #traingles
        #rotation = r*np.pi*2/3 + np.pi*(triangle_level % 2)
        
        height   = (6-self.sides)/(2*(3**(overall_level-1)))

        #can't figure out how to do this more elegantly - no doubt there is a better way
        if self.sides ==3:
              x3 = (x1+x2)/2+height*np.cos(np.pi/3+rotation)
              y3 = (y1+y2)/2+height*np.sin(np.pi/3+rotation)
              t = [[x1,y1],[x2,y2],[x3,y3]]

        else:
                x4 = (x1+x1)/2+height*np.cos(np.pi/2+rotation)
                y4 = (y1+y1)/2+height*np.sin(np.pi/2+rotation)
                x3 = (x2+x2)/2+height*np.cos(np.pi/2+rotation)
                y3 = (y2+y2)/2+height*np.sin(np.pi/2+rotation)
                t = [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]


        return t

    def make_shapes_verticles(self,layer_str,verticles,color,layer):
        print('Making ' + layer_str +' shape')
        plt_shape = []
        shapes =[]
        verticles_new = []
        for i in range(0,len(verticles)):

            shapes.append(self.make_shape_from_verticie(verticles[i][0],verticles[i][1],i,layer,verticles[i][2]))

            if self.sides ==4: #again - should find a neater way to do this.

                verticles_new.append([verticles[i][0],shapes[i][0],verticles[i][2]])
                verticles_new.append([shapes[i][0],shapes[i][3],verticles[i][2]+1])
                verticles_new.append([shapes[i][3],shapes[i][2],verticles[i][2]+1])
                verticles_new.append([shapes[i][2],shapes[i][1],verticles[i][2]+1])
                verticles_new.append([shapes[i][1],verticles[i][1],verticles[i][2]])

            else: #again - should find a neater way to do this.

                verticles_new.append([verticles[i][0],shapes[i][0],verticles[i][2]])
                verticles_new.append([shapes[i][0],shapes[i][2],verticles[i][2]+1])
                verticles_new.append([shapes[i][2],shapes[i][1],verticles[i][2]+1])
                verticles_new.append([shapes[i][1],verticles[i][1],verticles[i][2]])

            plt_shape.append(plt.Polygon(shapes[i],fill=True,color =color))

        return plt_shape, verticles_new

    def set_up_plot(self):

        self.fig = plt.figure(figsize=(20,20))
        #fig,ax = plt.subplots(1)
        self.ax=plt.axes()

        plt.xlim([-1,1])
        plt.ylim([-1,1])

        self.ax.set_aspect('equal')
        self.ax.spines['bottom'].set_color('white')
        self.ax.spines['top'].set_color('white')
        self.ax.spines['left'].set_color('white')
        self.ax.spines['right'].set_color('white')

        plt.xticks([])
        plt.yticks([])


        #colors
        self.colors=[]
        for color in self.colors_season:
            self.colors.append(color)

    def make_the_image(self, first_shape):

        print('Making first points')
        points = first_shape

        print('Making first verticles')
        first_verticles = []
        print('Self.sides: ', self.sides)
        for i in range(0,self.sides):
            if i < (self.sides - 1):
                ii=i+1
            else:
                ii=0
            tmp = []
            tmp.append(points[i])
            tmp.append(points[ii])
            for j in range(0,1):
                first_verticles.append([tmp[j],tmp[j+1],0])
            verticles = first_verticles

        first = plt.Polygon(first_shape,fill=True,color = self.colors_season[0])

        #second shapes;
        shapes_layer=[]
        print('self.N_layers: ', self.N_layers)
        for i in range(self.N_layers):
            shapes_tmp, verticles  = self.make_shapes_verticles(str(i+2),verticles,self.colors[i+1],i+2)
            shapes_layer.append(shapes_tmp)


        #add shapes to plot
        print('Adding shapes to plot')
        self.ax.add_patch(first)
        for i in range(self.N_layers):
            for t in shapes_layer[i]:
                self.ax.add_patch(t)


        now = datetime.now().strftime("_%Y-%m-%d_%H_%M_%S")
        filename = 'Images/' + self.name + now+'.png'
        print('Saving ' + filename)
        plt.savefig('Images/' + self.season + '_' + self.name + now + '.png')

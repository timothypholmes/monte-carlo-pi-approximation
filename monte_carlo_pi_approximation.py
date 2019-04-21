#! /usr/bin/env python3

#Import libraries
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import style
import numpy as np
import math
from random import random, randint

class monte_carlo_pi:

    def __init__(self, n_points, x_inside, y_inside, x_outside, y_outside, points_inside, points_outside):

        #self.x = x
        #self.y = y
        #self.r = r
        #self.fig = fig
        self.n_points = n_points
        self.x_inside = x_inside
        self.y_inside = y_inside
        self.x_outside = x_outside
        self.y_outside = y_outside
        self.points_inside = points_inside
        self.points_outside = points_outside 

    def monte_carlo(self, n_points):
        
        points_inside = 0
        points_outside = 0
        y = 0
        x = 0
        r = np.zeros((self.n_points))
        self.x_inside = np.zeros((self.n_points))
        self.y_inside = np.zeros((self.n_points))
        self.x_outside = np.zeros((self.n_points))
        self.y_outside = np.zeros((self.n_points))

        for i in range(1, self.n_points):
            points_outside += 1
            x = 2*random() - 1
            y = 2*random() - 1
            r = x**2 + y**2

            if r <= 1:
                points_inside = points_inside + 1
                self.x_inside[i] = x
                self.y_inside[i] = y

            elif r > 1:
                self.x_outside[i] = x
                self.y_outside[i] = y

        self.pi = 4*points_inside/self.n_points
        return self.pi


    def monte_plot(self, x_inside, y_inside, x_outside, y_outside):

        #print(str(pi))
        x_min = -1.1
        x_max = 1.1
        y_min = -1.1
        y_max = 1.1
        xlim = ((x_min, x_max))
        ylim = ((y_min, y_max))


        style.use('seaborn-dark')
        circle = plt.Circle((0, 0), radius=1, fill=False, linewidth = 0.1)
        self.fig = plt.figure(figsize=(10,5))

        ax1 = self.fig.add_subplot(121, xlim = xlim, ylim = ylim)

        title = ax1.set_title('', fontsize=20)
        ax1.legend(prop=dict(size=15), loc='lower left', shadow=True, ncol=2)
        ax1.set_xlabel('$x$', fontsize=10)
        ax1.set_ylabel('$y$', fontsize=10)
        ax1.xaxis.set_tick_params(labelsize=10)
        ax1.yaxis.set_tick_params(labelsize=10)

        ax1.set_title("Pi approximation= %f" % self.pi)
        ax1.plot(self.x_inside,self.y_inside,'b.')
        ax1.plot(self.x_outside,self.y_outside,'r.')

        self.ax2 = self.fig.add_subplot(122, xlim = xlim, ylim = ylim)

        self.inside, = self.ax2.plot([], [], c='r')
        self.outside, = self.ax2.plot([], [], c='b')
        self.ax2.add_artist(circle)

        self.title = self.ax2.set_title('', fontsize=12)
        self.ax2.legend(prop=dict(size=15), loc='lower left', shadow=True, ncol=2)
        self.ax2.set_xlabel('$x$', fontsize=10)
        self.ax2.set_ylabel('$y$', fontsize=10)
        self.ax2.xaxis.set_tick_params(labelsize=10)
        self.ax2.yaxis.set_tick_params(labelsize=10)


    def init(self):

        self.inside.set_data([], [])
        self.outside.set_data([], [])
        self.title.set_text('')
        return self.inside, self.outside,

    def update_pi(self, i):
        n_points = 100
        self.points_inside = 0
        self.points_outside = 0

        x = 2*random() - 1
        y = 2*random() - 1
        r = (x**2 + y**2)
        #plt.title("Pi approximation= %f" % (4*points_inside /float(n_points)))
        count = 0
        for i in range(1, n_points):
            if r <= 1:
                self.points_inside += 1
                count += 1
                plt.plot(x,y,'r.-')
                #x_inside = x
                #y_inside = y
                self.pi = ((4 * self.points_inside) / (i))
                return self.points_inside
                return self.pi

            else:
                self.points_outside += 1
                count += 1
                plt.plot(x,y,'b.-')
                #x_outside = x
                #y_outside = y
                self.pi = ((4 * self.points_inside) / (i))
                return self.points_outside
                return self.pi


            self.ax2.set_title("Pi approximation = {}".format(self.pi))

            #pi = ((4 * self.points_inside) / (self.points_inside + self.points_outside))
            #self.ax2.set_title("Pi approximation = {}".format(pi))
        

    def animate(self, points_inside, points_outside):

        #self.ax2.set_title("Pi approximation= %f" % (4 * (self.points_inside + 1) / ((self.points_inside + self.points_outside) + 1)))
        #pi = ((4 * self.points_inside + 1) / (self.points_inside + self.points_outside + 1))
        #self.ax2.set_title("Pi approximation = {}".format(pi))
        

        self.animate_update = plt.matplotlib.animation.FuncAnimation(self.fig, self.update_pi, init_func=self.init, frames=n_points, interval=1, repeat=False)
        #animate.save('animation.gif',writer='imagemagick', fps=60, dpi=80)
        self.animate_update.save('pi.mp4', fps=120,extra_args=['-vcodec', 'libx264'])
        plt.show()
        print('Done')

#if __name__ == '__main__':
 #   init()
 #   animate(i)

n_points = 1000
x_inside = 0
y_inside = 0
x_outside = 0
y_outside = 0
points_inside = 0
points_outside = 0
m = monte_carlo_pi(n_points, x_inside, y_inside, x_outside, y_outside, points_inside, points_outside)

m.monte_carlo(n_points)
m.monte_plot(x_inside, y_inside, x_outside, y_outside)
m.init()
m.animate(points_inside, points_outside)
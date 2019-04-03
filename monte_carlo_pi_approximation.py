#! /usr/bin/env python3

#Import libraries
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import style
import numpy as np
import math
from random import random, randint

class monte_carlo_pi:

    def __init__(self, x, y, r, fig):

        self.x = x
        self.y = y
        self.r = r
        self.fig = fig

    def monte_carlo():
        n_points = 5000
        points_inside = 0
        points_outside = 0
        y = 0
        x = 0
        r = np.zeros((n_points))
        x_inside = np.zeros((n_points))
        y_inside = np.zeros((n_points))
        x_outside = np.zeros((n_points))
        y_outside = np.zeros((n_points))

        for i in range(1, n_points):
            points_outside += 1
            x = 2*random() - 1
            y = 2*random() - 1
            r = x**2 + y**2

            if r <= 1:
                points_inside = points_inside + 1
                x_inside[i] = x
                y_inside[i] = y

            elif r > 1:
                x_outside[i] = x
                y_outside[i] = y

        pi = 4*points_inside/n_points
        return pi

    def animate_pi(self):
        print(str(pi))
        x_min = -1.1
        x_max = 1.1
        y_min = -1.1
        y_max = 1.1
        xlim = ((x_min, x_max))
        ylim = ((y_min, y_max))


        style.use('seaborn-dark')
        circle = plt.Circle((0, 0), radius=1, fill=False, linewidth = 0.1)
        self.fig = plt.figure(figsize=(10,5))

        ax1 = fig.add_subplot(121, xlim = xlim, ylim = ylim)

        title = ax1.set_title('', fontsize=20)
        ax1.legend(prop=dict(size=15), loc='lower left', shadow=True, ncol=2)
        ax1.set_xlabel('$x$', fontsize=10)
        ax1.set_ylabel('$y$', fontsize=10)
        ax1.xaxis.set_tick_params(labelsize=10)
        ax1.yaxis.set_tick_params(labelsize=10)

        #ax1.set_title("Pi approximation= %f" % pi)
        ax1.plot(x_inside,y_inside,'b.')
        ax1.plot(x_outside,y_outside,'r.')

        ax2 = fig.add_subplot(122, xlim = xlim, ylim = ylim)

        inside, = ax2.plot([], [], c='r')
        outside, = ax2.plot([], [], c='b')
        ax2.add_artist(circle)

        title = ax2.set_title('', fontsize=12)
        ax2.legend(prop=dict(size=15), loc='lower left', shadow=True, ncol=2)
        ax2.set_xlabel('$x$', fontsize=10)
        ax2.set_ylabel('$y$', fontsize=10)
        ax2.xaxis.set_tick_params(labelsize=10)
        ax2.yaxis.set_tick_params(labelsize=10)

    def init(self):
        inside.set_data([], [])
        outside.set_data([], [])
        title.set_text('')
        return inside,outside,

    def monte(self):
        n_points = 10000
        points_inside = 0
        points_outside = 0

        x = 2*random() - 1
        y = 2*random() - 1
        r = (x**2 + y**2)
        #plt.title("Pi approximation= %f" % (4*points_inside /float(n_points)))
        for i in range(1, n_points):
            if r <= 1:
                points_inside = points_inside + 1
                plt.plot(x,y,'r.-')
                #x_inside = x
                #y_inside = y
                #title.set_text("Pi approximation= %f" % (4*points_inside /n_points))
                return points_inside


            else:
                points_outside += 1
                plt.plot(x,y,'b.-')
                #x_outside = x
                #y_outside = y
                return points_inside

        title.set_text("Pi approximation= %f" % (4 * points_inside / (points_inside + points_outside)))

    animate = plt.matplotlib.animation.FuncAnimation(fig, monte, init_func=init, frames=n_points, interval=1, repeat=False)
    #animate.save('animation.gif',writer='imagemagick', fps=60, dpi=80)
    #animate.save('pi.mp4', fps=120,extra_args=['-vcodec', 'libx264'])
    plt.show()
    print('Done')

m = monte_carlo_pi()

m.monte_carlo_pi()
m.animate_pi()
m.init()
m.monte()

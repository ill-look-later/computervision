# -*- coding: utf-8 -*-
from pylab import *
from scipy.misc import imsave

xs = arange(-10.0, 10.0, 0.01)
ys = []
sigma = 2.0

for x in xs:
#    y = (1/sqrt(2*pi*sigma*sigma)) * exp(-(x*x)/(2*sigma*sigma))
    y = (x/(sqrt(2*pi)*sigma*sigma*sigma)) * exp(-(x*dx)/(2*sigma*sigma))
    ys.append(y)


plot(xs,ys)

show()

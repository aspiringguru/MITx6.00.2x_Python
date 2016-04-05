__author__ = 'MatthewWork'

import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)   #
yVals = pylab.array(yVals)   #
wVals = pylab.array(wVals)   #
xVals = xVals + xVals        #mean(xVals) > mean(yVals)
zVals = xVals + yVals        #mean(zVals) > mean(yVals) & mean(zVals) > mean(xVals)
tVals = xVals + yVals + wVals#mean(tVals) > mean(yVals) & mean(tVals) > mean(xVals) & mean(tVals) > mean(wVals)

#pylab.plot(xVals, zVals)#matches graph 5
#pylab.plot(xVals, yVals)#matches graph 4
#pylab.plot(xVals, sorted(yVals))#matches graph 3
#pylab.plot(sorted(xVals), yVals)#matches graph 2
pylab.plot(sorted(xVals), sorted(yVals))#matches graph
pylab.show()

#http://matplotlib.org/api/colors_api.html
'''
b: blue
g: green
r: red
c: cyan
m: magenta
y: yellow
k: black
w: white
'''

'''
pylab.plot(range(1000), xVals, 'ro')
pylab.plot(range(1000), zVals, 'bo')
pylab.plot(range(1000), tVals, 'g>')
pylab.plot(range(1000), yVals, 'y<')
pylab.plot(range(1000), wVals, 'cv')
pylab.show()
'''
'''
pylab.hist(xVals, 50, normed=1, facecolor='green', alpha=0.75)#looks uniform
pylab.title("xVals")
pylab.show()
pylab.hist(yVals, 50, normed=1, facecolor='green', alpha=0.75)#looks uniform
pylab.title("yVals")
pylab.show()
pylab.hist(wVals, 50, normed=1, facecolor='green', alpha=0.75)#looks uniform
pylab.title("wVals")
pylab.show()
pylab.hist(zVals, 50, normed=1, facecolor='green', alpha=0.75)#looks normal
pylab.title("zVals")
pylab.show()
pylab.hist(tVals, 50, normed=1, facecolor='green', alpha=0.75)#looks normal
pylab.title("tVals")
pylab.show()
'''
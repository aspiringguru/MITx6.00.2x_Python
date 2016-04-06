import pylab
import random
import math

class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]



#returns the actual x and y distance from the start point to the end point of a random walk.
def walkVector(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(f.getLoc(d).getX() - start.getX(),
           f.getLoc(d).getY() - start.getY())


class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name

#different variations on a drunk.

class UsualDrunk(Drunk):
    #NB: steps are in equal probability N/S/E/W
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
    def drunkType(self):
        return "UsualDrunk"

class ColdDrunk(Drunk):
    #NB: bias in steps in negative y direction 0.9 vs -1.03
    #NB: steps in x-y direction than 1.0.
    def takeStep(self):
        stepChoices =\
            [(0.0,0.9), (0.0,-1.03), (1.03, 0.0), (-1.03, 0.0)]
        return random.choice(stepChoices)
    def drunkType(self):
        return "ColdDrunk"

class EDrunk(Drunk):
    #NB: steps in random direction of random length 0.5 to 1.0
    def takeStep(self):
        ang = 2 * math.pi * random.random()
        length = 0.5 + 0.5 * random.random()
        return (length * math.sin(ang), length * math.cos(ang))
    def drunkType(self):
        return "EDrunk"

class PhotoDrunk(Drunk):
    #
    def takeStep(self):
        stepChoices =\
                    [(0.0, 0.5),(0.0, -0.5),
                     (1.5, 0.0),(-1.5, 0.0)]
        return random.choice(stepChoices)
    def drunkType(self):
        return "PhotoDrunk"

class DDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.85, 0.85), (-0.85, -0.85),
                     (-0.56, 0.56), (0.56, -0.56)]
        return random.choice(stepChoices)
    def drunkType(self):
        return "DDrunk"
#
def plotDrunkWalks(Drunktype, numTrials, numSteps):
    uDrunk = Drunktype("fred")
    drunkWalksX = []
    drunkWalksY = []
    for walk in range(1000):
        fField = Field()
        lLoc = Location(0,0)
        fField.addDrunk(uDrunk, lLoc)
        #walkVector(field, drunk, numSteps)
        temp = walkVector(fField, uDrunk, numSteps)
        #print temp, temp[0], temp[1]
        drunkWalksX.append(temp[0])
        drunkWalksY.append(temp[1])
    #print drunkWalksX
    #print drunkWalksY

    pylab.plot(drunkWalksX, drunkWalksY, 'ro')
    pylab.axis([-100, 100, -100, 100])
    pylab.grid(b=True, which='major', color='b', linestyle='-')
    #temp = "Drunk walk plot for numTrials="+str(numTrials)+" numSteps="+str(numSteps)+" Drunk type:"+uDrunk.drunkType()
    temp = "Drunk type:"+uDrunk.drunkType()
    pylab.title(temp)
    filename = uDrunk.drunkType()+"_numTrials="+str(numTrials)+"_numSteps="+str(numSteps)+".png"
    #pylab.savefig(filename, bbox_inches='tight')
    pylab.savefig(filename)
    #pylab.show()

numTrials = 100000
numSteps = 1000
print "plotting UsualDrunk"
plotDrunkWalks(UsualDrunk, numTrials, numSteps)
print "plotting ColdDrunk"
plotDrunkWalks(ColdDrunk, numTrials, numSteps)
print "plotting EDrunk"
plotDrunkWalks(EDrunk, numTrials, numSteps)
print "plotting PhotoDrunk"
plotDrunkWalks(PhotoDrunk, numTrials, numSteps)
print "plotting DDrunk"
plotDrunkWalks(DDrunk, numTrials, numSteps)
print "done"

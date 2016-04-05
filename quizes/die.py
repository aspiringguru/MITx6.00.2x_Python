import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
# Do not paste import pylab in the box.
# You should only be using the pylab.hist, pylab.title, pylab.xlabel, pylab.ylabel, pylab.show
# functions from the pylab module.
# Do not leave any debugging print statements when you paste your code in the box.

def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins=numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title is not None:
        pylab.title(title)
    pylab.show()

    # TODO
    
                    
# Implement this -- Coding Part 2 of 2
# A run of numbers counts the number of times the same dice value shows up in consecutive rolls. For example:
def longestRun(input):
    if len(input)==0:
        return 0
    runSize = 1
    maxRunSize = 1
    thisNum = input[0]
    for num in input[1:]:
        if num == thisNum:
            runSize += 1
            maxRunSize = max(runSize, maxRunSize)
        else:
            #different number found, start of new run
            thisNum = num
            runSize = 1
    return maxRunSize

#test longestRun function
# a dice roll of 1 4 3 has a longest run of 1
print longestRun([1, 4, 3])
# a dice roll of 1 3 3 2 has a longest run of 2
print longestRun([1, 3, 3, 2])
# a dice roll of 5 4 4 4 5 5 2 5 has a longest run of 3
print longestRun([5, 4, 4, 4, 5, 5, 2, 5])
print longestRun([5, 4, 4, 4, 5, 5, 2, 5, 2, 2, 2, 2, 2])#5
# When this function is called with the test case given in the file, it will return 5.312.
# Your simulation may give slightly different values.

#Restrictions:

#Do not import or use functions or methods from pylab, numpy, or matplotlib.
#Do not leave any debugging print statements when you paste your code in the box.

def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    trialsRecord = []
    for trial in range(numTrials):
        thisTrial = []
        for roll in range(numRolls):
            thisTrial.append(die.roll())
            #now test thisTrial for longest run of numbers
        trialsRecord.append(longestRun(thisTrial))
    mean, std = getMeanAndStd(trialsRecord)
    #makeHistogram(values, numBins, xLabel, yLabel, title=None):
    makeHistogram(trialsRecord, 10, 'Max run size', '# of occurances', "Run size for nominated die.")

    return mean

    # TODO
    
# One test case
print getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000)



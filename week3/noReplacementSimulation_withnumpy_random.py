#MITx: 6.00.2x Introduction to Computational Thinking and Data Science
#L5 Problem 1

import random
import numpy as np

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    # Your code here
    count = 0
    for trial in range(numTrials):
        bucket = ["r", "r", "r", "g", "g", "g"]
        selected = []
        for i in range(3):
            random.shuffle(bucket)
            selected.append(bucket.pop())
        selected = np.array(selected)
        countRed = list(selected).count("r")
        countGreen = list(selected).count("g")
        #print "trial #=", trial, "  countRed =", countRed, "countGreen=", countGreen
        if countRed==3 or countGreen==3:
            count += 1
    #print "count=", count, " numTrials=", numTrials
    return float(count)/numTrials



print "noReplacementSimulation(100)=", noReplacementSimulation(100)
print "noReplacementSimulation(1000)=", noReplacementSimulation(1000)
print "noReplacementSimulation(10000)=", noReplacementSimulation(10000)
print "noReplacementSimulation(100000)=", noReplacementSimulation(100000)


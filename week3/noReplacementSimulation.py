#MITx: 6.00.2x Introduction to Computational Thinking and Data Science
#L5 Problem 1

import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''

    match3Same=0
    for i in range(numTrials):
        bucket=['r','r','r','g','g','g']
        ballsSelected = []
        for a in range(3):
          ball=random.choice(bucket)
          bucket.remove(ball)
          ballsSelected.append(ball)
        #below tests if three balls _LEFT_IN_THE_BUCKET match.
        # Not the same as comparing balls removed from the bucket
        if ballsSelected[0]==ballsSelected[1] and ballsSelected[1]==ballsSelected[2] and ballsSelected[2]==ballsSelected[0]:
            match3Same += 1
    return float(match3Same)/numTrials


print "noReplacementSimulation(100)=", noReplacementSimulation(100)
print "noReplacementSimulation(1000)=", noReplacementSimulation(1000)
print "noReplacementSimulation(10000)=", noReplacementSimulation(10000)
print "noReplacementSimulation(100000)=", noReplacementSimulation(100000)


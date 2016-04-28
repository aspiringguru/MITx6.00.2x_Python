

import random
def noReplacementSimulation(numTrials, numRed, numGreen, numSame):
    '''
    Monte Carlo simulation
    select 3 balls from bucket containing numRed of red balls, numGreen of green balls.
    balls are not replaced after each selection.
    '''

    sameSelected=0
    for i in range(numTrials):
        #regenerate bucket & selected with each loop.
        bucket=[]
        selected=[]
        for i in range(numRed):
            bucket.append('r')
        for i in range(numGreen):
            bucket.append('g')
        for a in range(3):#NB: fixed case of 3 balls selected.
          ball=random.choice(bucket)
          selected.append(ball)
          bucket.remove(ball)
        #test if all balls selected are same colour, fixed case of 3 the same.
        #ieL if b[0]==b[1] and b[1]==b[2] and b[2]==b[0]:
        if selected[1:] == selected[:-1]:
            sameSelected=sameSelected+1
        #if selected[0]==selected[1] and selected[1]==selected[2] and selected[2]==selected[0]:

    return float(sameSelected)/numTrials


print noReplacementSimulation(100000, 3, 3, 3)
print noReplacementSimulation(100000, 4, 4, 3)

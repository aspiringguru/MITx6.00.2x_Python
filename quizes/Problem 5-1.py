#MITx: 6.00.2x Introduction to Computational Thinking and Data Science
#https://github.com/aspiringguru
#Quiz > Quiz > Problem 5
'''
You have a bucket with 4 red balls and 4 green balls.
You draw 3 balls out of the bucket.
Assume that once you draw a ball out of the bucket,
you don't replace it.
What is the probability of drawing 3 balls of the same color?
Do not import or use functions or methods from pylab, numpy, or matplotlib.
Do not leave any debugging print statements when you paste your code in the box.
'''
import random

def drawFromBucket(numRed, numGreen, numDrawnSame):
    bucket = []
    for i in range(numRed):
        bucket.append("r")
    for i in range(numGreen):
        bucket.append("g")
    #print bucket
    random.shuffle(bucket)
    #print bucket
    if bucket[0] == bucket[1] and bucket[1]== bucket[2]:
        return 1.0
    else:
        return 0.0


def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    results = 0.0
    for trial in range(numTrials):
        results += drawFromBucket(4, 4, 3)
    return results/numTrials


#print drawFromBucket(4, 4, 3)
print drawing_without_replacement_sim(100)
print drawing_without_replacement_sim(1000)
print drawing_without_replacement_sim(10000)
print drawing_without_replacement_sim(100000)
print drawing_without_replacement_sim(1000000)
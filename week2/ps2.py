# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

# For Python 2.7:
from ps2_verify_movement27 import testRobotMovement

# If you get a "Bad magic number" ImportError, you are not using 
# Python 2.7 and using most likely Python 2.6:
# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0 #NB: range is 1 to width inclusive.
        height: an integer > 0 #NB: range is 1 to height inclusive.
        """
        self.width = width
        self.height = height
        self.tilesCleaned = []
        #self.room = [[1 for x in range(width)] for x in range(height)]
        #initialises 2 dimensional array with all values set to one.
        #value of one represents dirty, zero represents clean
        #raise NotImplementedError #refer https://docs.python.org/2/library/exceptions.html

    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        #convert pos to grid reference.
        #check if grid reference is in tilesCleaned
        self.x = math.floor(pos.getX())
        self.y = math.floor(pos.getY())
        if (self.x, self.y) not in self.tilesCleaned:
            self.tilesCleaned.append((self.x, self.y))
        #self.room[pos.getX()][pos.getY()]==0 #set position to clean (array element = 0)
        #this method does not return anything.
        #raise NotImplementedError #refer https://docs.python.org/2/library/exceptions.html

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        #check if tile is in array of tilesCleaned
        return (m,n) in self.tilesCleaned
        #raise NotImplementedError  #refer https://docs.python.org/2/library/exceptions.html
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        return self.width * self.height
        """
        #raise NotImplementedError  #refer https://docs.python.org/2/library/exceptions.html
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        # length of tilesCleaned is number of tiles cleaned
        return len(self.tilesCleaned)
        #raise NotImplementedError

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """

        #random.seed(1)#for repeatable results.
        #pos[0] = random.randint(0, self.width-1) # -1 since randint Returns a random integer N such that a <= N <= b.
        #pos[1] = random.randint(0, self.height-1)# -1 since randint Returns a random integer N such that a <= N <= b.
        #above solution uses ints and returns random tile positions, not random positions.
        #NB: must use init method of Potion object
        return Position(random.random()*self.width, random.random()*self.height)
        #raise NotImplementedError   #refer https://docs.python.org/2/library/exceptions.html



    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        #note to self '&' is bitwise, 'and' is a boolean operation
        #NB: python permits the  a<b<c syntax used below, doesn't need verbose 'and' tests.
        #ie: 0 <= pos.getX() and pos.getX() <= self.width and 0 <= pos.getY() and pos.getY() <= self.height
        return 0 <= pos.getX() < self.width and 0 <= pos.getY() < self.height
        #raise NotImplementedError   #refer https://docs.python.org/2/library/exceptions.html



class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    #When a Robot is initialized, it should clean the first tile it is initialized on.
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.position = room.getRandomPosition()
        # clean position the robot is on.
        self.room.cleanTileAtPosition(self.position)
        #set random value for direction
        self.direction = random.random()*360
        self.speed = speed

        #set position to clean

        #raise NotImplementedError

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
        #raise NotImplementedError
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction
        #raise NotImplementedError

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position
        #raise NotImplementedError

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction
        #raise NotImplementedError

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        #NB: problem description specifically nominates _NOT_ to implement this.
        raise NotImplementedError # don't change this!


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        #generate new position
        newPosition = self.position.getNewPosition(self.direction, self.speed)
        #test if newPosition is in the room
        if self.room.isPositionInRoom(newPosition):
            self.room.cleanTileAtPosition(newPosition)
            self.setRobotPosition(newPosition)
        else:
            #new position is NOT in the room generate a new direction, wait until next call to updatePosition
            self.direction = random.random()*360
        #raise NotImplementedError

# Uncomment this line to see your implementation of StandardRobot in action!
#testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    trialsRecord = []
    for trail in range(num_trials):
        #VISUALIZING ROBOTS - refer course pdf note 'Optional_Visualizing Robots Problem Set 2.pdf'
        #anim = ps2_visualize.RobotVisualization(num_robots, width, height)
        #create room
        room = RectangularRoom(width, height)
        #create robots & store in array
        robots = []
        count = 0
        for i in range(num_robots):
            robots.append(robot_type(room, speed))
        #NB: how does robot_type(room, speed) create a robot object???? what magic is this???
        #while calcualted coverage is < min_coverage, update positions & repeat
        while float(room.getNumCleanedTiles()) / room.getNumTiles() < min_coverage:
            #anim.update(room, robots)
            #do more cleaning - update robot positions
            for robot in robots:
                robot.updatePositionAndClean()
            count += 1
        trialsRecord.append(count)#record number of steps to achieve min_coverage in this trial.
    #after loop, close animation
    #anim.done()
    #calculate average number of steps over trials.
    return sum(trialsRecord)/float(len(trialsRecord))
    #raise NotImplementedError

# Uncomment this line to see how much your simulation takes on average
##print  runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot)
#runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type)
#One robot takes around 150 clock ticks to completely clean a 5x5 room.
#print  runSimulation(1, 1.0, 5, 5, 1.0, 30, StandardRobot)
# One robot takes around 190 clock ticks to clean 75% of a 10x10 room.
#print  runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot)
# One robot takes around 310 clock ticks to clean 90% of a 10x10 room.
#print  runSimulation(1, 1.0, 10, 10, 0.9, 30, StandardRobot)
# One robot takes around 3322 clock ticks to completely clean a 20x20 room.
#print  runSimulation(1, 1.0, 20, 20, 1.0, 30, StandardRobot)
# Three robots take around 1105 clock ticks to completely clean a 20x20 room.
#print  runSimulation(1, 1.0, 20, 20, 1.0, 30, StandardRobot)

#print  runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot)

# === Problem 4
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    #change direction randomly after every time step, rather than just when they run into walls.
    #

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.direction = random.random()*360
        newPosition = self.position.getNewPosition(self.direction, self.speed)
        #test if newPosition is in the room
        if self.room.isPositionInRoom(newPosition):
            self.room.cleanTileAtPosition(newPosition)
            self.setRobotPosition(newPosition)
        else:
            #new position is NOT in the room generate a new direction, wait until next call to updatePosition
            self.direction = random.random()*360

        #raise NotImplementedError


def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)#10 robots.
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        #runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type)
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        #calculates time to clean 80% of room, 20 trials, 20x20 grid room, speed 1, 10 robots of type StandardRobot
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
        #calculates time to clean 80% of room, 20 trials, 20x20 grid room, speed 1, 10 robots of type RandomWalkRobot
    pylab.plot(num_robot_range, times1)
    #plots results for StandardRobot, x-axes= number of robots, y-axis = avg time taken.
    pylab.plot(num_robot_range, times2)
    #plots results for RandomWalkRobot, x-axes= number of robots, y-axis = avg time taken.
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width  #NB: total number of tiles is 300, ie: size does not change.
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        #runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        #calculates time to clean 80% of room, 200 trials, room grid =x by y, speed 1, 2 robots of type StandardRobot
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
        #calculates time to clean 80% of room, 200 trials, room grid =x by y, speed 1, 2 robots of type StandardRobot
    pylab.plot(aspect_ratios, times1)
    #plots results for StandardRobot, x-axes= aspect ratio (width/height), y-axis = avg time taken.
    pylab.plot(aspect_ratios, times2)
    #plots results for RandomWalkRobot, x-axes= aspect ratio (width/height), y-axis = avg time taken.
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

# === Problem 5
#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#showPlot1("Comparison of Robot types to achieve coverage.", "Number of Robots", "Number of Steps required")
#
#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
print "showPlot2 running"
showPlot2("Comparison of StandardRobot and RandomWalkRobot", "Room Aspect Ratio (width/height)", "Number of steps required")
#nb: program pauses here until plot closed.
print "showPlot2 finished"
#

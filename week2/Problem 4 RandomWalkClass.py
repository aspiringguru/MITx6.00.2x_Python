

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
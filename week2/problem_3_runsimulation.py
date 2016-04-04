#https://github.com/aspiringguru/MITx6.00.2x_Python
#passes tests. Need to write a test script.

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
            #do more cleaning - update robot positions
            for robot in robots:
                robot.updatePositionAndClean()
            count += 1
        trialsRecord.append(count)#record number of steps to achieve min_coverage in this trial.
    #calculate average number of steps over trials.
    return sum(trialsRecord)/float(len(trialsRecord))
    #raise NotImplementedError


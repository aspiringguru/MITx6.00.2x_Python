__author__ = 'MatthewWork'
#https://github.com/aspiringguru/MITx6.00.2x_Python
#passes tests. Need to write a test script.

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


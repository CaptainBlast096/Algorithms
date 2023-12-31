import random
import math

# Initialize the Nodes
class Node:
    #Constructor
    def __init__(self, type = 0, x=500, y=500, radius= 5, ID=0):
        self.setCoords(type, x, y, radius)
        self.setCost()
        self.__visited = False
        self.ID = ID
 
    #String representation of the Node
    def __str__(self):
        return "City: ({:4}, {:4}) \tCost: {:3} \tClass: {}".format(self.__x, self.__y, self.__cost, self.bracket())
    
    def __repr__(self):
        return "{:03}".format(self.ID)

    def __eq__(self, other):
        if (self.__x == other.getX() and self.__y == other.getY() and self.__cost == other.getCost()):
            return True
    
    #Setting the coordinates of the node wether it is random or clustered
    def setCoords(self, type=0, x=500, y=500 , radius=5):
        if (type == 0): #Randomly generated coordinates
            self.__x = random.randint(0, 1000)
            self.__y = random.randint(0, 1000)
        elif (type == 1): #Randomly generated Clustered coordinates
            self.__x = random.randint(0, radius*8) + x
            self.__y = random.randint(0, radius*8) + y

    #Setting the cost of the node based on the location
    def setCost(self):
        if (self.inRadius() == 0):
            self.__cost = random.uniform(0.1, 0.5)
        elif (self.inRadius() == 1):
            self.__cost = random.uniform(2, 5)
        elif (self.inRadius() == 2):
            self.__cost = random.uniform(5, 7)
        else:
            self.__cost = random.uniform(1, 2)
        self.__cost = round(self.__cost, 2)

    #Setting the node as visited
    def setVisited(self, value:bool = True):
        self.__visited = value

    def setID(self, ID:int):
        self.ID = ID

    #GET FUNCTIONS

    def getCost(self):
        return self.__cost

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y

    def getVisited(self):
        return self.__visited

    #Distance between two nodes
    def getDistance(self, x:int, y:int):
        return math.sqrt((self.__x - x)**2 + (self.__y - y)**2)
    
    #Checks if node is in the radius of the price points and returns the price tier
    def inRadius(self):
        xLeft = (self.__x -167.5)**2
        xQuad1 = (self.__x - 781)**2
        xQuad4 = (self.__x - 658)**2
        yTop = (self.__y - 742)**2
        yBottom = (self.__y - 200)**2
        yLeft = (self.__y - 450.6)**2
        if (xLeft + yLeft <= 20600):
            return 0
        elif (xQuad1 + yTop <= 9000):
            return 1
        elif (xQuad4 + yBottom <= 8130):
            return 2

    #Returns the price tier of the node
    def bracket(self):
        if (self.inRadius() == 0):
            return "Low Class"
        elif (self.inRadius() == 1):
            return "Middle Class"
        elif (self.inRadius() == 2):
            return "High Class"
        else:
            return "default"
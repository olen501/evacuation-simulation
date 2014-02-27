import rand
import utils

from event import Event
from agent import Agent
from vector import Vector

#for gaussian cdf
from scipy.stats import norm


class Generator:
    left = 0
    generated = 0

    def __init__(self, door, door_coords, total, consider_time):
        print 'generator created to produce',total,'agents in door', door
        self.door = door
        self.min_coord = (door_coords[0], door_coords[1])
        self.max_coord = (door_coords[0] + door_coords[2], door_coords[1] + door_coords[3])
        #self.goals = utils.sort_goals(self.min_coord, goal_coords)
        self.left = total
        self.consider_time = consider_time

    def generate(self):
        startx = rand.rand(self.min_coord[0], self.max_coord[0])
        starty = rand.rand(self.min_coord[1], self.max_coord[1])

        # The tempset and tempgoal variables are just used for storing the random number that was generated
        # so it can be printed. Other than that, they are unnecessary
        #gaussian_val = abs(rand.gaussian_rand())
        #tempset = rand.rand(0, 1) if gaussian_val <= 1.0 else rand.rand(2, 3)
        #goalset = self.goals[tempset]

        #tempgoal = rand.rand(0, 1)
        #goal = goalset[tempgoal]
        #goalx = rand.rand(goal['min'][0], goal['max'][0])
        #goaly = rand.rand(goal['min'][1], goal['max'][1])

        # get a random speed for the person. 
        rand_val = rand.gaussian_rand()
        travel_interval = int(round(norm.cdf(rand_val)*10.0)) + 1  # add 1 so we don't get a zero velocity
        #travel_interval = rand.rand(1, 10)

        #print 'Agent from Door %d, Coords: (%d, %d)'%(self.door, self.min_coord[0], self.min_coord[1])
        #print '  Goal Set: %d, Goal: %d, Coords: (%d, %d)'%(tempset, tempgoal, goalx, goaly)
        #print goal
        #print travel_interval

        #agent = Agent(chr(self.door) + '_' + chr(self.left), travel_interval, 0, Vector(startx, starty), Vector(goalx, goaly))
        agent = Agent(chr(self.door) + '_' + chr(self.left), travel_interval, self.consider_time, Vector(startx, starty))
        self.left -= 1
        return agent
	
    def next_event(self):
        if not self.left : return None
        #rand_val = self.density_function()

        # Change the *10.0 to whatever number you want to vary the range of
        # times. 10.0 will give ten queue slots, 100.0 will give one hundred
        # queue slots, etc.
        #queue_time = int(round(self.cdf(rand_val)*10.0))
        queue_time = rand.rand(0, 29)
        return Event(self, 'new_agent', queue_time)







































from vector import Vector
import struct as st

direction_vectors = [Vector(1,1),Vector(1,0),Vector(1,-1),Vector(0,-1),
					Vector(-1,-1),Vector(-1,0),Vector(-1,-1),Vector(0,1),]
class Terrain:
	terrain_set = {}
	terrain_shape = []
	width,depth = 0,0
	
	def __init__(self, filename) :
		file_handle = open(filename,'r')
		self.terrain_shape = []
		print "Initializing map"
		#Read every value of evacuation feild
		#And cover them into num stored in a simple 2D list
		for line in file_handle.readlines() :
			self.terrain_shape.append([int(num) for num in line.split()])
		self.depth = len(self.terrain_shape)
		self.width = len(self.terrain_shape[3])
		print 'map created with: width', self.width, 'depth', self.depth

	def add_agent(self, agent) :
	#Add a new agent on the map
		if not self.available(agent.coordinate) : return False
		else :
			self.terrain_set[agent.coordinate] = agent
			return True

	def remove_agent(self, agent) :
	#Remove an agent from the map
		del self.terrain_set[agent.coordinate]

	def good_to_exit(self, agent) :
	#Check whether the agent is good to leave
		if self.terrain_shape[agent.coordinate.y][agent.coordinate.x] == 0 : return True
		else : return False

	def get_available_surrounding(self, agent) :
		available_list = []
		for direction in direction_vectors :
			neighborhood = agent.coordinate + direction
			if self.available(neighborhood) : 
				delt = self.terrain_shape[agent.coordinate.y][agent.coordinate.x]-self.terrain_shape[neighborhood.y][neighborhood.x]
				available_list.append((delt,direction))
#		print 'available surrounding is'+''.join([str(vector) for vector in available_list])
		return available_list

	def valid(self, position):
		if (position.x < 0) or (position.y < 0) \
		or (position.x > self.width) or (position.y > self.depth) \
		or (self.terrain_shape[position.y][position.x] > 30000):
			return False
		else : return True
			
	def available(self, position):
		if not self.valid(position) : return False
		if self.terrain_set.get(position) : return False
		else : return True

	def move(self, agent, direction):
		del self.terrain_set[agent.coordinate] 
		self.terrain_set[agent.coordinate+direction] = agent

if __name__=='__main__' :
	terrain = Terrain("grid_bits.txt")
	for i in range(450):
		if terrain.valid(Vector(i,297)) : 
			print '%d,298' % i ,'valid'

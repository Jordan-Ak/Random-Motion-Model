from random import choice

class RandomMovement():
	"""A class to generate random movement."""
	
	def __init__(self, num_points = 10000):
		"""initialize the attributes of a walk"""
		self.num_points = num_points
		
		#All points start at (0,0)
		self.x_values = [0]
		self.y_values = [0]

	def get_point(self):
			"""Calculate the movement made in the x and y direction"""
			#Decide which direction to go and how far to go in that direction
			x_direction = choice([-1, 1])
			x_distance = choice([0, 1, 2, 3, 4])
			x_point = x_direction * x_distance
			
			y_direction = choice([1, -1])
			y_distance = choice([0, 1, 2, 3, 4])
			y_point = y_direction * y_distance
			
			return(x_point, y_point)
	
	def fill_points(self):
		"""Calculate all the points in the move."""
		
		#Keep making points till the move reaches the desired length.
		while len(self.x_values) < self.num_points:
			x_point, y_point = self.get_point()
			
			#Reject moves that go nowhere.
			if x_point == 0 and y_point == 0:
				continue
				
			#Calculate the next x and y values.
			next_x = self.x_values[-1] + x_point
			next_y = self.y_values[-1] + y_point
			
			self.x_values.append(next_x)
			self.y_values.append(next_y)
		
	

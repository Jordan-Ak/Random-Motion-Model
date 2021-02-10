import matplotlib.pyplot as plt

from random_motion_module import RandomMovement 

#Keep making new models while the program is active.


def prompt():
	"""Displays user prompt after closing the Random motion page."""
	keep_running = input("Make another walk? (y/n): ")
	
	return keep_running



active = True

while active:
	#Make random movement and plot the points.
	rm = RandomMovement(200_000)

	rm.fill_points()
	
	#Set the size of the plotting window
	plt.figure(dpi = 128, figsize =(10, 6))
	
	point_numbers = list(range(rm.num_points))
	plt.scatter(rm.x_values, rm.y_values, c = point_numbers,
			cmap = plt.cm.Greens, edgecolor = 'none', s = 0.5)

	#Emphasize the first and last points.
	plt.scatter(0, 0, color = 'blue', edgecolors = 'none', s = 10)
	plt.scatter(rm.x_values[-1], rm.y_values[-1], color = 'red',
									  edgecolors = 'none', s = 10)
	
	#Remove the axes
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	
	plt.show()

	keep_running = prompt()
	
	while True:
		
		if keep_running == 'y':
			break
	
		elif keep_running == 'n':
			active = False
			break
	
		else:
			keep_running = input('Choose between "y" or "n" ')
			

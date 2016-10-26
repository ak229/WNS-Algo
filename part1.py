import numpy as np
import math 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import networkx as nx
from scipy.spatial import cKDTree as KDTree
from scipy.spatial import distance
	
### PRNG FOR SQUARE RANDOM ###

def findEdges(vertex_array,threshold):
	boolean_list_of_vertices = [False for i in range(vertex_array.shape[0])]
	list_of_edgelists = []

	
	for x in range(0,vertex_array.shape[0]-1):
		list_x = []
		for y in range(x+1,vertex_array.shape[0]):
			print "y ka wala in y wala for "+str(y+1)
			print distance.euclidean(vertex_array[x],vertex_array[y])
			if(distance.euclidean(vertex_array[x],vertex_array[y]) < threshold):  #test and change the threshold value here
				print distance.euclidean(vertex_array[x],vertex_array[y])
				list_x.append(y+1)

		list_of_edgelists.append(list_x)


	for x in range(0,vertex_array.shape[0]-1):
		print list_of_edgelists[x]
		

def random_square(N,threshold):
	s = np.random.uniform(0,1,(N,2))
	
	xarray = [1]
	yarray = [1]

	xarray.remove(1)
	yarray.remove(1)

	for i in range(0,s.shape[0]):
		xarray.insert(i,s[i][0]);
		yarray.insert(i,s[i][1]);


	vertex_array = np.vstack((xarray,yarray)).T
	findEdges(vertex_array,threshold)

	plt.plot(xarray,yarray,'ro')
	plt.axis([-1,2,-1,2])
	plt.show()
### END OF PRNG FOR SQUARE RANDOM ###


### PRNG FOR DISK RANDOM ###
def random_disk(N,threshold):
	radius = np.random.uniform(0.0,1.0, (N,1))**(1./2.)
	theta = np.random.uniform (0.,2., (N,1))*math.pi

	x = radius * np.sin(theta)
	y = radius * np.cos(theta)

	vertex_array = np.hstack((x,y))
	findEdges(vertex_array,threshold)
	plt.plot(x,y,'ro')
	plt.axis([-1,1,-1,1])
	plt.show()

### END OF PRNG FOR DISK RANDOM ###

### PRNG FOR SPHERE RANDOM ###
def random_sphere(N,threshold):
	radius = np.random.uniform(0.0,1.0, (N,1)) 
	theta = np.random.uniform(0.,2.,(N,1))*math.pi
	phi = np.arccos(1-2*np.random.uniform(0.0,1.,(N,1)))


	for x in range(0,radius.shape[0]):
		zoop = radius[x]
		if zoop < 0:
			zoop = -(-zoop)**(1./3.)

		if zoop >= 0:
			zoop = (zoop)**(1./3.)


		radius[x] = zoop

	x = radius * np.sin( theta ) * np.cos( phi )
	y = radius * np.sin( theta ) * np.sin( phi )
	z = radius * np.cos( theta )

	vertex_array = np.hstack((x,y,z))
	findEdges(vertex_array,threshold)
	fig = plt.figure()
	ax = fig.add_subplot(111, projection = '3d')

	ax.scatter(x,y,z,'ro')

	plt.show()
### END OF PRNG FOR SPHERE RANDOM ###

def read_input(line_number):
	line_read = []
	with open("input.txt", "r") as ins:
		for line in ins:
			line_read.append(line)

	line_values = line_read[line_number-1].split()

	number_of_nodes = int(line_values[0])
	avg_degree = int(line_values[1])
	distance_threshold = float(line_values[2])
	type_of_distribution = line_values[3]
	return number_of_nodes,avg_degree,distance_threshold,type_of_distribution





test_number = int(raw_input('Enter the Benchmark test you want to run (1-10):'))
if(test_number > 10):
	print "Error"
else:	
	number_of_nodes,avg_degree,dist_thres,dist_type = read_input(test_number)
	if dist_type == 'S':
		random_square(number_of_nodes,dist_thres)
	elif dist_type == 'D':
		random_disk(number_of_nodes,dist_thres)
	elif dist_type == 'P':
		random_sphere(number_of_nodes,dist_thres)
	else:
		print("Distribution not found")



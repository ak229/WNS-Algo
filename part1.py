import numpy as np
import math 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import distance
	

def findEdges(type_dist,vertex_array,threshold):
	list_of_edgelists = []
	min_degree = 999999;
	max_degree = 0;
	total_pairs = 0;
	index_min = -1;
	index_max = -1; 



	print "Threshold is "+str(threshold)
	
	length_vertex_array = vertex_array.shape[0]
	for x in range(0,vertex_array.shape[0]-1):
		list_x = []
		
		for y in range(x+1,vertex_array.shape[0]):
			if(distance.euclidean(vertex_array[x],vertex_array[y]) < threshold):  #test and change the threshold value here
				list_x.append(y)
		
		list_of_edgelists.append(list_x)
		length_zoe = len(list_x)
		total_pairs = total_pairs + length_zoe
		if (length_zoe > max_degree):
			max_degree = length_zoe
			index_max = x

		if (length_zoe < min_degree):
			min_degree = length_zoe
			index_min = x

	avg_deg = total_pairs/vertex_array.shape[0]
	

	print "Highest degree is "+str(max_degree)
	print "Lowest degree is "+str(min_degree)
	print "Highest degree adjacency list is for "+str(vertex_array[index_max])+" and is "+str(list_of_edgelists[index_max])
	print "Lowest degree adjacency list is for "+str(vertex_array[index_min])+" and is "+str(list_of_edgelists[index_min])
	print "Average degree is "+str(avg_deg)
	print "Number of unique pairwise edges is "+str(total_pairs)	
	return length_vertex_array,total_pairs,threshold,avg_deg	
	#print list_of_edgelists	

### PRNG FOR SQUARE RANDOM ###
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

  	"""
	plt.plot(xarray,yarray,'ro')
	plt.axis([-1,2,-1,2])
	plt.show()
	"""
	return vertex_array
### END OF PRNG FOR SQUARE RANDOM ###


### PRNG FOR DISK RANDOM ###
def random_disk(N,threshold):
	radius = np.random.uniform(0.0,1.0, (N,1))**(1./2.)
	theta = np.random.uniform (0.,2., (N,1))*math.pi

	x = radius * np.sin(theta)
	y = radius * np.cos(theta)

	vertex_array = np.hstack((x,y))

	print vertex_array[0]
	print vertex_array[0][0]
	print len(vertex_array)
	"""
	plt.plot(x,y,'ro')
	plt.axis([-1,1,-1,1])
	plt.show()
	"""
	return vertex_array

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

	fig = plt.figure()
	ax = fig.add_subplot(111, projection = '3d')

	ax.scatter(x,y,z,'ro')

	plt.show()
	return vertex_array
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
		vertex_array = random_square(number_of_nodes,dist_thres)	
		findEdges(1,vertex_array,dist_thres)
	elif dist_type == 'D':
		vertex_array = random_disk(number_of_nodes,dist_thres)
		findEdges(2,vertex_array,dist_thres)
	elif dist_type == 'P':
		vertex_array = random_sphere(number_of_nodes,dist_thres)
		findEdges(3,vertex_array,dist_thres)
	else:
		print("Distribution not found")


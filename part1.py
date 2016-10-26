import numpy as np
import math 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import distance




def DegreeDist(list_degreewise_count,max_degree):
	print "Degree Distribution"
	list_degrees = []
	for x in range(0,max_degree):
		list_degrees.append(list_degreewise_count[x])
		#print list_degreewise_count[x]

	y = list_degrees
	N = len(y)
	x = range(N)
	width = 1/1.5
	plt.bar(x,y,width,color='red')

	plt.show()



def RGGDisplay(vertex_array,xarray,yarray,point_min, point_max, list_max):
	#Will show minimum point is blue, max point is yellow, neighbours of max are green
  	plt.plot(xarray,yarray,'ro')
  	plt.plot([point_min[0]],[point_min[1]],'bo')
  	plt.plot([point_max[0]],[point_max[1]],'yo')
  	#Lets plot the edges in green here
  	for x in list_max:
  		plt.plot([vertex_array[x][0]],[vertex_array[x][1]],'go')
	plt.axis([-1,2,-1,2])
	plt.show()


def findEdges(vertex_array,threshold,xarray,yarray):
	list_of_edgelists = []
	min_degree = 999999;
	max_degree = 0;
	total_pairs = 0;
	index_min = -1;
	index_max = -1;

	length_vertex_array = vertex_array.shape[0]

	list_degreewise_count = [0] * length_vertex_array

	for x in range(0,vertex_array.shape[0]-1):
		list_x = []
		
		for y in range(x+1,vertex_array.shape[0]):
			if(distance.euclidean(vertex_array[x],vertex_array[y]) < threshold):  #test and change the threshold value here
				list_x.append(y)
		
		list_of_edgelists.append(list_x)
		length_zoe = len(list_x)
		list_degreewise_count[length_zoe] = list_degreewise_count[length_zoe]+1
		total_pairs = total_pairs + length_zoe
		if (length_zoe > max_degree):
			max_degree = length_zoe
			index_max = x

		if (length_zoe < min_degree):
			min_degree = length_zoe
			index_min = x

	avg_deg = total_pairs/vertex_array.shape[0]
	

	DegreeDist(list_degreewise_count,max_degree)
	RGGDisplay(vertex_array,xarray,yarray,vertex_array[index_min],vertex_array[index_max],list_of_edgelists[index_max])	
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

  	plt.plot(xarray,yarray,'ro')
	plt.axis([-1,2,-1,2])
	plt.show()
	
	return vertex_array,xarray,yarray
### END OF PRNG FOR SQUARE RANDOM ###


### PRNG FOR DISK RANDOM ###
def random_disk(N,threshold):
	radius = np.random.uniform(0.0,1.0, (N,1))**(1./2.)
	theta = np.random.uniform (0.,2., (N,1))*math.pi

	x = radius * np.sin(theta)
	y = radius * np.cos(theta)

	vertex_array = np.hstack((x,y))

	plt.plot(x,y,'ro')
	plt.axis([-1,1,-1,1])
	plt.show()
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


list_test_cases = [1,2,3,6,7,8,9]

for x in list_test_cases:
	number_of_nodes,avg_degree,dist_thres,dist_type = read_input(x)

	if dist_type == 'S':
		vertex_array,xarray,yarray = random_square(number_of_nodes,dist_thres)
		if (x == 1 or x == 2 or x == 3):	
			N,M,R,A = findEdges(vertex_array,dist_thres,xarray,yarray)
			print "Number of sensors is "+str(N)
			print "Number of distinct pairwise sensor adjacencies is "+str(M)
			print "Distance bound for adjacency (Threshold) is "+str(R)
			print "Average Degree is "+str(A)

	if dist_type == 'D':
		vertex_array,xarray,yarray = random_disk(number_of_nodes,dist_thres)	
		

	if dist_type == 'P':
		vertex_array,xarray,yarray = random_sphere(number_of_nodes,dist_thres)	
		
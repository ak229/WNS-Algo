import numpy as np
import math 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import distance

def determine_location(number_of_rows,poitn,threshold,type_d):
	if(type_d == 'S'):
		x_value_location = math.floor(poitn[0]/threshold)
		y_value_location = math.floor(poitn[1]/threshold)
		location_value = y_value_location*number_of_rows+x_value_location+1

	if(type_d == 'D'):
		x_value_location = math.floor(poitn[0]/threshold)
		y_value_location = math.floor(poitn[1]/threshold)
		location_value = y_value_location*number_of_rows+x_value_location+1

	if(type_d == 'P'):
		x_value_location = math.floor(poitn[0]/threshold)
		y_value_location = math.floor(poitn[1]/threshold)
		z_value_location = math.floor(poitn[2]/threshold)
		location_value = y_value_location*number_of_rows+x_value_location+1

	return int(location_value)


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

#Needs Revisions
def addToDivisions(vertex_array,threshold,xarray,yarray,type_d):
	number_of_rows = int(math.ceil(1/threshold))
	number_of_columns = number_of_rows
	number_of_divs = number_of_rows * number_of_columns

	list_division_meow = [[] for i in range(number_of_divs+1)]
	for x in range(0,vertex_array.shape[0]):
		location_number = determine_location(number_of_rows,vertex_array[x],threshold,type_d)
		list_division_meow[int(location_number)].append(x)

	return list_division_meow

#Needs sphere revision
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

def bigon2Edges(vertex_array,adj_list_final,pos,threshold):
	adj_list_temporary = adj_list_final
	point = vertex_array[pos]
	
	print "Adj list leng in bigon2Edg is "+str(len(adj_list_final))
	print "initial adj list is "+str(adj_list_temporary)

	for i in range(len(adj_list_final)-1):
		print "i is "+str(i)
		if(distance.euclidean(point,vertex_array[i]) > threshold):
			print "distance is "+str(distance.euclidean(point,vertex_array[i]))+" and threshold is "+str(threshold)
			print "ADJ I is "+str(adj_list_final[i])
			adj_list_temporary.remove(adj_list_final[i])

	print "adj_lis in bigon2 is"
	print adj_list_temporary
	return 0;

#Needs Revision
def findEdges(vertex_array,point,pos,division_vertex_list,number_of_rows,threshold,type_d):
	adj_list = []

	my_location = determine_location(number_of_rows,point,threshold,type_d)
	adj_list.append(division_vertex_list[my_location])

	list_of_locations = []

	for x in range(1,number_of_rows**2 + 1):
		list_of_locations.append(x)

	if(my_location+number_of_rows-1 in list_of_locations and my_location%number_of_rows !=0):
		adj_list.append(division_vertex_list[my_location+number_of_rows-1])

	if(my_location+number_of_rows+1 in list_of_locations and my_location%number_of_rows !=1):
		adj_list.append(division_vertex_list[my_location+number_of_rows+1])

	if(my_location-number_of_rows+1 in list_of_locations and my_location%number_of_rows !=1):
		adj_list.append(division_vertex_list[my_location-number_of_rows+1])

	if(my_location-number_of_rows-1 in list_of_locations  and my_location%number_of_rows !=0):
		adj_list.append(division_vertex_list[my_location-number_of_rows-1])

	if(my_location+1 in list_of_locations and my_location%number_of_rows != 0):
		adj_list.append(division_vertex_list[my_location+1])

	if(my_location-1 in list_of_locations and my_location%number_of_rows != 1):
		adj_list.append(division_vertex_list[my_location-1])

	if(my_location+number_of_rows in list_of_locations):
		adj_list.append(division_vertex_list[my_location+number_of_rows])

	if(my_location-number_of_rows in list_of_locations):
		adj_list.append(division_vertex_list[my_location-number_of_rows])

	adj_list_final = []
	map(adj_list_final.extend,adj_list)
	#print adj_list_final

	adj_list_final.remove(pos)
	adj_list_final.sort()

	print "In find edges length of adj_list_final is "+str(len(adj_list_final))

	adj_list_cleared = bigon2Edges(vertex_array,adj_list_final,pos,threshold)

	return adj_list_final

#needs revision
def findEdgesLinear(vertex_array,threshold,xarray,yarray,type_d):
	division_vertex_list = addToDivisions(vertex_array,threshold,xarray,yarray,type_d)
	number_of_rows = int(math.ceil(1/threshold))
	adj_list_linear = []
	min_degree = 999999;
	max_degree = 0;
	total_pairs = 0;
	index_min = -1;
	index_max = -1;

	length_vertex_array = vertex_array.shape[0]

	list_degreewise_count = [0] * length_vertex_array

	for z in range(vertex_array.shape[0]):
		adj_list_inst = findEdges(vertex_array,vertex_array[z],z,division_vertex_list,number_of_rows,threshold,type_d)
		print "result of adj_list_inst for "+str(z)+" is "
		print adj_list_inst
		adj_list_linear.append(adj_list_inst)

		print adj_list_linear[z]

		length_zoe = len(adj_list_inst)
		list_degreewise_count[length_zoe] = list_degreewise_count[length_zoe]+1
		total_pairs = total_pairs + length_zoe
		if (length_zoe > max_degree):
			max_degree = length_zoe
			index_max = z

		if (length_zoe < min_degree):
			min_degree = length_zoe
			index_min = z

	avg_deg = total_pairs/vertex_array.shape[0]
	print "List_degree"
	print list_degreewise_count
	DegreeDist(list_degreewise_count,max_degree)
	print index_min
	print index_max
	print "Vertex Array min"
	print vertex_array[index_min]
	print "Vertex Array max"
	print vertex_array[index_max]
	print "Adj Lst Linear"
	print adj_list_linear[index_max]
	RGGDisplay(vertex_array,xarray,yarray,vertex_array[index_min],vertex_array[index_max],adj_list_linear[index_max])
	return length_vertex_array,total_pairs,threshold,avg_deg	


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
	return vertex_array,x,y

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
	return vertex_array,x,y,z
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


list_test_cases = [2]

for x in list_test_cases:
	number_of_nodes,avg_degree,dist_thres,dist_type = read_input(x)

	if dist_type == 'S':
		vertex_array,xarray,yarray = random_square(number_of_nodes,dist_thres)

	if dist_type == 'D':
		vertex_array,xarray,yarray = random_disk(number_of_nodes,dist_thres)	
		

	if dist_type == 'P':
		vertex_array,xarray,yarray,zarray = random_sphere(number_of_nodes,dist_thres)	


	N,M,R,A = findEdgesLinear(vertex_array,dist_thres,xarray,yarray,'S')
	print "Number of sensors is "+str(N)
	print "Number of distinct pairwise sensor adjacencies is "+str(M)
	print "Distance bound for adjacency (Threshold) is "+str(R)
	print "Average Degree is "+str(A)












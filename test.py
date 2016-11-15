def addToDivisions(vertex_array,threshold,xarray,yarray,type_d):
	number_of_rows = int(math.ceil(1/threshold))
	number_of_columns = number_of_rows
	number_of_divs = number_of_rows * number_of_columns

	list_division_meow = []

	for i in range(0,number_of_rows**2 + 1):
		list_division_meow.append([-1])

	for x in range(0,vertex_array.shape[0]):
		location_number = determine_location(number_of_rows,vertex_array[x],threshold,type_d)
		list_division_meow[int(location_number)].append(x)

	return list_division_meow

"""
Example is -

number_of_rows = 4
number_of_divs = 16
list_division_meow (final value) = [[],[1,2],[3,4,5],[9,10]]

But looks like, list_division_meow(final value) = [[-1],[-1,1,2],[-1,3,4,5],[-1],[-1],[-1],[-1],[-1],[-1,9,10]]



"""
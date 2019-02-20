# Question : 72
# Time : O(NxM)
# Space : O(NxM)
# Runtime : 200 ms

def edit_distance(str1, str2):
	len_str1 = len(str1)
	len_str2 = len(str2)
	result_matrix = prepare_matrix(len_str1+1, len_str2+1)
	for y in range(1,len_str2+1):
		for x in range(1,len_str1+1):
			if str1[x-1] == str2[y-1]:
				result_matrix[y][x] = result_matrix[y-1][x-1]
			else:
				result_matrix[y][x] = 1 + min(result_matrix[y-1][x],
									  		  result_matrix[y][x-1],
									  		  result_matrix[y-1][x-1])
	return result_matrix

def prepare_matrix(width, height):
	matrix = []
	for y in range(height):
		inner_matrix = []
		for x in range(width):
			if y == 0:
				inner_matrix.append(x)
			elif x == 0:
				inner_matrix.append(y)
			else:
				inner_matrix.append(0)
		matrix.append(inner_matrix)
	return matrix
				
			

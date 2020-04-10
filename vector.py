import math
import random

# Class Vector stores vector and matrices multiplication
class Vector:
	def __init__(self, arr):
		# Store the vector
		self.vector = arr

		# Store the shape of the vector
		self.x = len(arr)
		self.y = len(arr[0])

	def __str__(self):
		return self.__repr__()

	def __repr__(self):
		# Turn the vector into a string
		result = '-m'+str(self.vector)+'m-'
		result = result.replace('-m[', 'Vector(')
		result = result.replace(']m-', ')')
		result = result.replace(', [', '\n       [')

		return result

	# Add two vector with it's corresponding element
	def __add__(self, other):
		# Checks if the size of the 2 matrices match
		if self.x == other.x and self.y == other.y:
		
			newArr = []
			# Iterate through the row
			for x in range(self.x):
				newArr.append([])

				# Iterate through the coloumn
				for y in range(self.y):
					# Adds all the element to its corresponding element
					newArr[x].append(self.vector[x][y] + other.vector[x][y])

			return Vector(newArr)
		else:
			return "Vector magnitude doesn't match"

	# Subtract two vector from it's corresponding element
	def __sub__(self, other):
		# Checks if the size of the 2 matrices match
		if self.x == other.x and self.y == other.y:
			
			newArr = []
			# Iterate through the row
			for x in range(self.x):
				newArr.append([])
				#Iterate through the coloumn
				for y in range(self.y):
					# Subtracts all the element from its corresponding element
					newArr[x].append(self.vector[x][y] - other.vector[x][y])

			return Vector(newArr)
		else:
			return "Vector magnitude doesn't match"

	# Multiplies two vector with it's corresponding element
	def __mul__(self, other):
		# Checks if the vector is of the same size
		if self.x == other.x and self.y == other.y:
			newArr = []
			# Iterate through the row
			for x in range(self.x):
				newArr.append([])
				# Iterate through the coloumn
				for y in range(self.y):
					# Multiply all the element to its corresponding element
					newArr[x].append(self.vector[x][y] * other.vector[x][y])

			return Vector(newArr)
		else:
			return "Vector magnitude doesn't match"

	# Divides two vector from it's corresponding element
	def __truediv__(self, other):
		# Checks if the vector is of the same size
		if self.x == other.x and self.y == other.y:
			newArr = []
			# Iterate through the row
			for x in range(self.x):
				newArr.append([])
				# Iterate through the coloumn
				for y in range(self.y):
					# Multiply all the element to its corresponding element
					newArr[x].append(self.vector[x][y] / other.vector[x][y])

			return Vector(newArr)
		else:
			return "Vector magnitude doesn't match"

	# Multiply the vector by a scalar quantity. Eg - 2
	def multiply(self, n):
		# Multiply the vector by a scalar quantity
		newArr = []

		# Iterate through the row
		for x in range(self.x):
			newArr.append([])
			# Iterate through the coloumn
			for y in range(self.y):
				# Multiply each element by n
				newArr[x].append(self.vector[x][y] * n)

		return Vector(newArr)

	# Divide the vector by a scalar quantity. Eg - 2
	def divide(self, n):
		# Divide the vector by a scalar quantity
		newArr = []

		# Iterate through the row
		for x in range(self.x):
			newArr.append([])
			# Iterate through the coloumn
			for y in range(self.y):
				# Divide each element by n
				newArr[x].append(self.vector[x][y] / n)

		return Vector(newArr)



	# Transform every element in the element
	# To the derivative of the sigmoid function
	def sigmoid_derivative(self, sigmoided=False):
		newArr = []
		# If the vector already went through the sigmoid
		# Function
		if sigmoided == True:
			sigmoid_arr = self
		else:
			sigmoid_arr = self.sigmoid()


		# Iterate through each row
		for x in range(sigmoid_arr.x):
			newArr.append([])
			# Iterate through each coloumn
			for y in range(sigmoid_arr.y):
				# Calculate the sigmoid derivative and append it
				# to the new array
				newArr[x].append(sigmoid_arr.vector[x][y] * (1 - sigmoid_arr.vector[x][y]))

		return Vector(newArr)

	# Transform every element in the vector
	# between 0 and 1 by sigmoid activation function
	def sigmoid(self):
		newArr = []

		# Iterates through the rows in the matrice
		for x in range(self.x):
			newArr.append([])

			# Iterates throught the coloumn in the matrice
			for y in range(self.y):
				newArr[x].append( (1)/(1+ (math.exp(1) ** -self.vector[x][y]) ) )

		return Vector(newArr)

	# Get a specific element
	def element(self, x, y):
		return self.vector[x][y]

	# Get a specific row
	def row(self, x):
		return self.vector[x]

	# Get a specific coloumn
	def coloumn(self, y):
		newArr = []
		# Iterate through each row
		for x in range(self.x):
			# Append the required coloumn element
			newArr.append(self.vector[x][y])

		return newArr

	# So that we can iterate through the vector
	def iterable(self):
		newArr = []
		# Iterate through the row
		for x in range(self.x):
			# Iterate through the coloumn
			for y in range(self.y):
				newArr.append(self.vector[x][y])

		return newArr

	# To change the value of an element
	def changeValue(self, x, y, val):
		self.vector[x][y] = val

	# --


# Returns a random vector of size (x, y)
# Eg- randomVector(2, 2)
# returns - 
#		[w, x]
#		[y, z]
def randomVector(cx, cy):
	newArr = []

	# Iterate through the rows
	for x in range(cx):
		newArr.append([])
		# Iterate through the coloumn
		for y in range(cy):
			# Generate a random element and append on it
			newArr[x].append(round(random.uniform(-1, 1), 3))

	return Vector(newArr)

# Performs matrice multiplication
def dot(self, other):
	# x is row
	# y is coloumn
	# Checks if the coloumn of the first matrice matches with the row of the other matric
	if self.y == other.x:

		newArr = []
		# Iterates through the row of the first matrice
		for x in range(self.x):
			newArr.append([])
			# Iterates through the coloumn of the second matrice
			for other_y in range(other.y):
				statement = ''
				# Iterates through the coloumn of the first matrice, which is also equal to the
				# row of the second matrice
				for y in range(self.y):
					statement += '{} * {}+'.format(self.vector[x][y], other.vector[y][other_y])
				statement = statement[:len(statement)-1]
				newArr[x].append(eval(statement))
		return Vector(newArr)

	else:
		return "Vectors aren't applicable undergo dot operation"

# Transforms a number between 0 and 1
# With sigmoid activation function
def sigmoid(n):
	return (1)/(1+ (math.exp(1) ** -n) )



if __name__ == "__main__":
	a = Vector([[6,8],
				[2,3]])

	b = Vector([[2, 2],
				[2, 2]])

	#print(sigmoid(0))
	#print(a + b)
	#print(a - b)
	#print(a * b)
	#print(a / b)
	#print(a.multiply(2))
	#print(a.divide(2))
	#print(dot(a, b))
	#print(a.element(1,1))
	#print(a.multiply(-1))
	#print(a.sigmoid_derivative())


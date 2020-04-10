import vector
import math

class NeuralNetwork:
	def __init__(self, Input, Output, inputLayer = 2, hiddenLayer = [], outputLayer = 1):
		# Take the input matrix and rotate(invert) it
		self.input = self.invertInput(Input)
		# The expected output we from the given input
		self.expectedOutput = Output
		self.inputNodes = inputLayer
		self.hiddenLayer = hiddenLayer
		self.outputLayer = outputLayer

		self.calculations = [0, 0]

		self.weights = []
		self.weights.append(vector.randomVector(self.hiddenLayer[0], self.inputNodes))
		self.weights.append(vector.randomVector(self.outputLayer, self.hiddenLayer[0]))


	def invertInput(self, INPUT):
		newInput = []
		# Iterate through the coloumn and turn them into rows
		for y in range(INPUT.y):
			newInput.append([])
			# Iterate through the row and turn them into coloumn
			for x in range(INPUT.x):
				newInput[y].append(INPUT.element(x, y))

		# Return the array as a vector
		return vector.Vector(newInput)

	def costFunction(self, output, expectedOutput):
		cost = (output - expectedOutput)
		finalCost = cost * cost
		return finalCost

	def feedForward(self):	
		self.calculations[0] = vector.dot(self.weights[0], self.input).sigmoid()
		self.calculations[1] = vector.dot(self.weights[1], self.calculations[0]).sigmoid()
		return True

	def backPropagation(self):
		# Calculate the total cost
		cost = self.costFunction(self.calculations[1], self.expectedOutput)
		finalCost = [cost.element(0, a) for a in range(cost.y)]
		self.currentCost = sum(finalCost)

		# Calulate the derivative for each weight
		# djdw1 for first layer
		# djdw2 for second layer

		derivative2 = ( (self.calculations[1] - self.expectedOutput).multiply(2) ) * self.calculations[1].sigmoid_derivative(sigmoided=True) 
		#print("variables in djdw2-\na)\n",self.invertInput(self.calculations[0]),"\nb)\n", derivative2)
		djdw2 = vector.dot(derivative2 ,self.invertInput(self.calculations[0]))

		#print(derivative2)

		#print("variables in step 1-\na)\n",self.invertInput(derivative2),"\nb)\n", self.weights[1])
		step1 = vector.dot(self.invertInput(derivative2), self.weights[1])
		#print("step1 is success!")
		#print("variables in step2-\na)\n", self.calculations[0])
		step2 = self.calculations[0].sigmoid_derivative(sigmoided=True)
		#print("step2 is success!")
		#print("variables in step3-\na)\n",step1,"\nb)\n",self.invertInput(step2))
		step3 = self.invertInput(step1) * step2
		#print("step3 is success!")
		#print("variables in final step-\na)\n",self.invertInput(self.input),"\nb)",self.invertInput(step3))
		djdw1 = vector.dot(step3, self.invertInput(self.input) )

		# Update weights
		self.weights[0] -= djdw1.multiply(0.5)
		self.weights[1] -= djdw2.multiply(0.5)

		return True

	# Static method
	def trainModel(self, batch=3, epoch=1500):
		# Iterate through batch
		for i in range(1, batch+1):
			print("Batch {}/{}:\n".format(str(i), str(batch)))
			# Iterate through epochs
			for j in range(1, epoch+1):
				if j != epoch:
					print("\tEpochs {}/{}:".format(str(j), str(epoch)), end="\r")
				else:
					print("\tEpochs {}/{}:".format(str(j), str(epoch)))

				self.feedForward()
				self.backPropagation()
			print("\n")
			print("\tPredictions: {}\tCost:{}".format(str(self.calculations[1]), str(self.currentCost)))

		






def sigmoid_derivative(sigm):
	return sigm * (1.0 - sigm)

# myOrd() takes in a character and turns it to a number, typically 0-25
def myOrd(i):
	values = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
	values.append(' ')
	correspondence = [(a + 1) for a in range(27)]

	return correspondence[values.index(i)]


# Filters input to a limited number of nodes
# filterInput(INPUT, num) - takes in a vector of strings or ints/floats
def filterInput(INPUT, num):
	if isinstance(INPUT, vector.Vector):
		resultArr = []
		# Turn every character to a lower character then to a number
		# Iterate through every name
		for x in range(INPUT.x):
			# Iterate through colomns
			for y in range(INPUT.y):
				# Iterate through every character
				ords = [ myOrd(character.lower()) for character in INPUT.element(x, y)]
				resultArr.append(ords)



		# Make resultArr have same number of coloumns - num
		# Iterate through every name
		for x in range(INPUT.x):
			currentName = resultArr[x]

			# If len(currentName) is less than num - increase it
			# If len(currentName) is more than num - decrease it
			# If len(currentName) is equal to num - proceed
			if len(currentName) < num:
				# Get the current length of the nodes
				length = len(currentName)
				# Append the average of currentName to currentName
				# To the required amount to fill the void nodes
				for iteration in range(num - length):
					average = sum(currentName)/length
					currentName.append(math.ceil(average))
				resultArr[x] = currentName
			elif len(currentName) > num:
				# Cut off the unnecessary input nodes
				resultArr[x] = currentName[:num]


		return vector.Vector(resultArr)

	else:
		return "INPUT should be a vector"


if __name__ == "__main__":
	# Input data
	# Nodes -> 'height', 'wearsGlasses', 'favouriteCar', 'favouriteSubject'
	
	Data = {
		'Arafat': {
			'height': 'short',
			'wearsGlasses': 'True',
			'favouriteCar': 'Azera',
			'favouriteSubject': 'Accounting'
		},

		'Samir': {
			'height': 'tall',
			'wearsGlasses': 'True',
			'favouriteCar': 'Tesla ModelX',
			'favouriteSubject': 'None'
		},

		'Khalil': {
			'height': 'very tall',
			'wearsGlasses': 'True',
			'favouriteCar': 'Honda Accord',
			'favouriteSubject': 'Maths'
		},

		'Nabil': {
			'height': 'very short',
			'wearsGlasses': 'True',
			'favouriteCar': 'None',
			'favouriteSubject': 'Economics'
		},
	}

	# Combine data
	Final_Data = []
	for person in Data:
		data = person
		for attribute in Data[person]:
			data = data + Data[person][attribute]

		Final_Data.append([data])


	inputVector = vector.Vector(Final_Data)

	inputVector = filterInput(inputVector, 10)


	outputVector = vector.Vector([[1,0,0,0]])

	NN = NeuralNetwork(inputVector, outputVector, inputLayer=10, hiddenLayer=[5], outputLayer=1)

	NeuralNetwork.trainModel(NN, batch=3, epoch=2500)

	'''
	Neural Network in python 3.6.5
	Arafat - @mohammadarafatzaman

	'''

	
	for i in range(1500):
		NN.feedForward()
		NN.backPropagation()
	results = NN.calculations[1]
	print(NN.calculations[1])
	print(NN.currentCost)
	
	print("") 
	for i, person in enumerate(Data):
		straight = round(results.element(0, i) * 100, 2)
		gay = round(100 - straight, 2)
		print(f'{person} is {straight}% straight or {gay}% gay')

		

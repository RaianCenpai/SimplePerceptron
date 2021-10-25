# perceptron is the main function which initializes a Perceptron object with the appropriate parameters of threshold, adjustment rate, 
# and starting weights and calls the runTraining function with the proper parameters of the training set and number of passes.
def perceptron(threshold, adjustment, weights, train, passes):
    perceptron = Perceptron(threshold, adjustment, weights)
    perceptron.runTraining(train, passes)


class Perceptron:

    # Perceptron defines the object for a perceptron and stores the threshold, adjustment rate, and weights.
    # init initializes all of these values with the passed values.
    def __init__(self, threshold, adjustment, weights):
        self.threshold = threshold
        self.adjustment = adjustment
        self.weights = weights


    # updateWeights takes the parameters of input which is one sample, predict which is the true or false value
    # of the prediction of this perceptron for the sample, and real which is the given true or false value with the sample.
    # It then compares the predict and real and if they are identical the function does nothing.
    # Otherwise if predict is false which implies real is true, the function will add the adjustment rate to each of the weights
    # that correspond to inputs with 1's.
    # Otherwise if predict is true which implies real is false, the function will subtract the adjustment rate from each of the weights
    # that correspond to inputs with 1's.
    def updateWeights(self, input, predict, real):

        if(predict == real):
            return

        elif(predict == False):
            for i in range(len(self.weights)):
                if(input[i] == 1):
                    self.weights[i] = self.weights[i] + self.adjustment

        elif(predict == True):
            for i in range(len(self.weights)):
                if(input[i] == 1):
                    self.weights[i] = self.weights[i] - self.adjustment


    # calculateOutput takes the parameter of input which is a single sample and calculates either true or false
    # using the weights and threshold.
    def calculateOutput(self, input):
        out = 0
        for i in range(len(self.weights)):
            out = out + (self.weights[i] * input[i])

        if(self.threshold < out):
            return True
        else:
            return False


    # runSample takes the parameter of input which is a list of a boolean value and its corresponding sample.
    # The function separates the boolean value and sample and passes the sample to calculateOutput.
    # It then uses the output from calculateOutput to update the weights and then prints all the values for this sample.
    def runSample(self, input):
        real = input[0]
        inputs = input[1]
        output = self.calculateOutput(inputs)

        self.updateWeights(inputs, output, real)

        print('inputs:', inputs)
        print('prediction:', output, 'answer:', real)
        print('adjusted weights:', self.weights)


    # runPass takes the parameter of train which is an entire training set of samples.
    # The function then calls runSample on each individual sample in the training set.
    def runPass(self, train):
        for i in range(len(train)):
            self.runSample(train[i])


    # runTraining takes the parameter of train which is an entire training set of samples, and passes which is the number
    # of passes to run on.
    # The function prints the starting values, then prints the pass number and runs a pass until the number of passes requested
    # is reached.
    def runTraining(self, train, passes):
        print('Starting weights:', self.weights)
        print('Threshold:', self.threshold, 'Adjustment:', self.adjustment)
        for i in range(passes):
            print('')
            print('Pass', i+1)
            print('')
            self.runPass(train)
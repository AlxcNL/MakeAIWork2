import logging
import numpy as np

logging.basicConfig(level=logging.DEBUG)

class Perceptron:

    """
    Perceptron class to simulate a Neuron
    """

    # Constructor
    # 'dunder init'
    def __init__(self):
        self.weightVector = None
        self.bias = 0

    def initialize(self, nrOfFeatures):
        """ Initialize w and b as zero """

        # Create initial weight vector for each feature
        self.weightVector = np.zeros(nrOfFeatures)

        # Initialize bias
        self.bias = 0

    def train(self, X, y, epochs=100, learningRate=0.1):
        """
        Train the perceptron using the inputVector
        and target labels
        """
        # Initialize weights and bias
        nrOfFeatures = X.shape[1]
        self.initialize(nrOfFeatures)

        epochs = range(0, epochs)

        # for each epoch
        for epoch in epochs:
            logging.info(f"epoch : {epoch}")

            # For each inputVector
            for inputVector, label in zip(X, y):
                logging.debug(f"inputVector : {inputVector}")

                # Labeled output
                logging.debug(f"label : {label}")

                # Predict output
                prediction = self.predict(inputVector)
                logging.debug(f"prediction : {prediction}")

                # Determine error
                error = label - prediction
                logging.debug(f"error : {error}")

                # update weight and b
                deltaWeight = learningRate * error * inputVector
                self.weightVector += deltaWeight
                logging.debug(f"deltaWeight : {deltaWeight}")

                deltaBias = learningRate * error
                self.bias += deltaBias
                logging.debug(f"deltaBias : {deltaBias}")

                print()

    def predict(self, inputVector):
        """
        Create class labels for new input data
        using the step activation function of
        the logical function that has been learned
        """
        activation = np.dot(inputVector, self.weightVector) + self.bias
        logging.debug(f"activation : {activation}")

        return 1 if activation > 0 else 0




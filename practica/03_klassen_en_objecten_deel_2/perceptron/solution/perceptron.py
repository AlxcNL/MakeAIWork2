import logging
import numpy as np
import pydot

logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    filename="logs.log",
    filemode="w",
    level=logging.INFO,
    force=True,
)


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
        """Initialize w and b as zero"""

        # TODO Random initialization

        # Create initial weight vector for each feature
        self.weightVector = np.zeros(nrOfFeatures)

        # Initialize bias
        self.bias = 0

    def predict(self, inputVector):
        """
        Create class labels for new input data
        using the step activation function of
        the logical function that has been learned
        """
        activation = np.dot(inputVector, self.weightVector) + self.bias
        logging.debug(f"activation : {activation}")

        # Threshold = 0
        return 1 if activation > 0 else 0

    # TODO Learning Rate en epochs ook in slides
    # Capitals -> Matrix van nx1 (kolomvector), y -> single value
    def train(self, X, y, epochs=100, learningRate=0.1):
        """
        Train the perceptron using the inputVector
        and target labels (desired outputvalues)
        """
        # Initialize weights and bias
        # 2
        nrOfFeatures = X.shape[1]
        self.initialize(nrOfFeatures)

        # Aantal trainingen
        epochs = range(0, epochs)

        # for each epoch
        for epoch in epochs:
            logging.debug(f"epoch : {epoch}")

            # For each inputVector
            for inputVector, label in zip(X, y):
                logging.debug(f"inputVector : {inputVector}")

                # Labeled output
                logging.debug(f"label : {label}")

                # Predict output
                prediction = self.predict(inputVector)
                logging.debug(f"prediction : {prediction}")

                # Determine error
                # Difference between desired output value and actual output value
                error = label - prediction
                logging.debug(f"error : {error}")

                # Update weight and b
                deltaWeight = learningRate * error * inputVector
                self.weightVector += deltaWeight
                logging.debug(f"deltaWeight : {deltaWeight}")
                deltaBias = learningRate * error
                self.bias += deltaBias
                logging.debug(f"deltaBias : {deltaBias}")

                print()

    def display():
        graphs = pydot.graph_from_dot_file("example.dot")
        graph = graphs[0]
        graph.exp

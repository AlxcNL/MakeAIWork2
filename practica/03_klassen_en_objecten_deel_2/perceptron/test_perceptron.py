#!/usr/bin/env python

from perceptron import Perceptron
import itertools
import logging
import numpy as np

logging.basicConfig(level=logging.DEBUG)

# # TODO refactor using Itertools
# xTrain = np.array(
#     [
#         [0, 0], [0, 1], [1, 0], [1, 1]
#     ]
# )

possibleOutcomes = [0, 1]
xTrain = np.array(
    [
        element for element in itertools.product(possibleOutcomes, possibleOutcomes)
    ]
)

logging.debug(f"xTrain : {xTrain}")

yTrain = np.array([0, 0, 0, 1])

p = Perceptron()
p.train(xTrain, yTrain, epochs=100, learningRate=0.1)
testInput = np.array([1, 1])
logging.debug(f"testInput : {testInput}")

prediction = p.predict(testInput)
logging.info(f"Predicted y value : {prediction}")
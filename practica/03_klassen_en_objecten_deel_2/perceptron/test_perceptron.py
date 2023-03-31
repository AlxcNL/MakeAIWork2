#!/usr/bin/env python

from perceptron import Perceptron
import itertools
import logging
import numpy as np

logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    filename="logs.log",
    filemode="w",
    level=logging.INFO,
    force=True,
)

# Waarheidstabel invoerwaarden
possibleOutcomes = [0, 1]
xTrain = np.array(
    [element for element in itertools.product(possibleOutcomes, possibleOutcomes)]
)

logging.debug(f"xTrain : {xTrain}")

# Waarheidstabel output
yTrain = np.array([0, 0, 0, 1])

# Maak een object perceptron aan
andPerceptron = Perceptron()
# Train de perceptron met een AND functie
andPerceptron.train(xTrain, yTrain, epochs=100, learningRate=0.1)

# Test de perceptrong
testInput = np.array([1, 0])
prediction = andPerceptron.predict(testInput)
logging.info(f"Predicted y value : {prediction}")

# Test de perceptrong
# testInput = np.array([1, 1])
logging.info(f"testInput : {testInput}")
logging.info(f"Predicted y value : {prediction}")

prediction = andPerceptron.predict(testInput)
logging.info(f"testInput : {testInput}")
logging.info(f"Predicted y value : {prediction}")

# OPDRACHT
# Maak nu zelf het object orPerceptron
orPerceptron = Perceptron()

yTrain = np.array([0, 1, 1, 1])
orPerceptron.train(xTrain, yTrain, epochs=100, learningRate=0.1)
testInput = np.array([0, 0])
testInput = np.array([0, 1])
testInput = np.array([1, 0])
testInput = np.array([1, 1])

'''
====== Legal notices

Copyright (C) 2013 - 2021 GEATEC engineering

This program is free software.
You can use, redistribute and/or modify it, but only under the terms stated in the QQuickLicense.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY, without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the QQuickLicense for details.

The QQuickLicense can be accessed at: http://www.qquick.org/license.html

__________________________________________________________________________



 THIS PROGRAM IS FUNDAMENTALLY UNSUITABLE FOR CONTROLLING REAL SYSTEMS !!

__________________________________________________________________________

It is meant for training purposes only.

Removing this header ends your license.
'''

# Standard modules

import time as tm
import sys as ss
import os
import socket as sc

# 3rd party modules

import numpy as np
import sklearn.neural_network as nn
import sklearn.metrics as mt
import sklearn.preprocessing as pp

nnLibraryName = 'sklearn' if input ('SciKitLearn or Keras <s/k>: ') == 's' else 'keras'

if nnLibraryName == 'keras':
    import tensorflow as tf
    import tensorflow.keras as kr
    import tensorflow.keras.models as md
    import tensorflow.keras.layers as ly
    import tensorflow.keras.losses as ls

# Proprietary modules

ss.path +=  [os.path.abspath (relPath) for relPath in  ('..',)]

import parameters as pm
import socket_wrapper as sw

class NeuralNet:
    def __init__(self, sampleFileName):
        self.sampleFileName = sampleFileName

        with open (self.sampleFileName) as self.sampleFile:
            self.samples = np.array ([[float (word) for word in line.split ()] for line in self.sampleFile.readlines ()])
            print ('samples.shape:', self.samples.shape)
    
            self.inputDim = self.samples.shape [1] - 1
            print ('inputDim:', self.inputDim)

        self.partitionSize = int (self.samples.shape [0] / pm.nrOfPartitions)  # Rounds down, so in most cases a remainder of the samples will not be used
        print ('partitionSize:', self.partitionSize)

        self.cycle ()
        self.run ()

    def partition (self):
        testStartIndex = self.partitionIndex * self.partitionSize
        print ('testStartIndex:', testStartIndex)

        testStopIndex = testStartIndex + self.partitionSize
        print ('testStopIndex:', testStopIndex)

        if pm.nrOfPartitions > 1:
            self.trainingSamples = np.vstack ((self.samples [: testStartIndex, :], self.samples [testStopIndex:, :]))
        else:
            self.trainingSamples = self.samples

        print ('trainingSamples.shape:', self.trainingSamples.shape)

        self.trainingX = self.trainingSamples [:, :self.inputDim]
        self.trainingScalerX = pp.MinMaxScaler(feature_range = (-1, 1), copy = True, clip = False)
        self.trainingScalerX.fit (self.trainingX)
        self.scaledTrainingX = self.trainingScalerX.transform (self.trainingX)
        print ('scaledTrainingX.shape:', self.scaledTrainingX.shape)
    
        self.trainingY = self.trainingSamples [:, self.inputDim:]
        self.trainingScalerY = pp.MinMaxScaler(feature_range = (-1, 1), copy = True, clip = False)
        self.trainingScalerY.fit (self.trainingY)
        self.scaledTrainingY = self.trainingScalerY.transform (self.trainingY) .ravel ()
        print ('scaledTrainingY.shape:', self.scaledTrainingY.shape)

        if pm.nrOfPartitions > 1:
            self.testSamples = self.samples [testStartIndex:testStopIndex, :]
            print ('testSamples.shape:', self.testSamples.shape)

            self.testX = self.testSamples [:, self.inputDim]
            self.testScalerX = pp.MinMaxScaler(feature_range = (-1, 1), copy = True, clip = False)
            self.testScalerX.fit (self.testX)
            self.scaledTestX = self.testScalerX.transform (self.testX)
            print ('scaledTestX.shape:', self.scaledTestX.shape)

            self.testY = self.testSamples [:, self.inputDim:]
            self.testScalerY = pp.MinMaxScaler(feature_range = (-1, 1), copy = True, clip = False)
            self.testScalerY.fit (self.testY)
            self.scaledTestY = self.testScalerY.transform (self.testY) .ravel ()
            print ('scaledTestY.shape:', self.scaledTestY.shape)

        print ()

    def cycle (self):
        for self.partitionIndex in range (pm.nrOfPartitions):
            print ('partitionIndex:', self.partitionIndex, 'out of', list (range (pm.nrOfPartitions)))
            self.partition ()

            if nnLibraryName == 'sklearn':
                self.model = nn.MLPRegressor (hidden_layer_sizes = pm.hiddenDims, activation = 'relu', random_state = 1, max_iter = pm.nrOfEpochs)
                self.model.fit (self.scaledTrainingX, self.scaledTrainingY)
            else:
                self.model = md.Sequential ([
                    ly.Input  (self.inputDim),
                    * [ly.Dense (hiddenDim, activation = 'relu') for hiddenDim in pm.hiddenDims],
                    ly.Dense (pm.outputDim)
                ])

                self.model.compile (
                    optimizer = 'adam',
                    loss = ls.MeanSquaredError (),
                    metrics = ['accuracy']
                )

                self.model.fit (self.scaledTrainingX, self.scaledTrainingY, epochs = pm.nrOfEpochs, verbose = 2)

            self.predictedScaledTrainingY = self.model.predict (self.scaledTrainingX)
            print ('scaledTrainingY.shape', self.scaledTrainingY.shape)
            print ('predictedScaledTrainingY.shape', self.predictedScaledTrainingY.shape)
            print ('scaled training mse:', mt.mean_squared_error (self.predictedScaledTrainingY, self.scaledTrainingY))
            print ()

            if pm.nrOfPartitions > 1:
                self.predictedScaledTestY = self.model.predict (self.scaledTestX)
                print ('scaledTestY.shape', self.scaledTestY.shape)
                print ('predictedScaledTestY.shape', self.predictedScaledTestY.shape)
                print ('scaled test mse:', mt.mean_squared_error (self.predictedScaledTestY, self.scaledTestY))
                print ()

    def run (self):
        self.steeringAngle = 0

        with sc.socket (*sw.socketType) as self.clientSocket:
            self.clientSocket.connect (sw.address)
            self.socketWrapper = sw.SocketWrapper (self.clientSocket)
            self.halfApertureAngle = False

            while True:
                self.input ()
                self.sweep ()
                self.output ()
                tm.sleep (0.02)

    def input (self):
        sensors = self.socketWrapper.recv ()

        if not self.halfApertureAngle:
            self.halfApertureAngle = sensors ['halfApertureAngle']
            self.sectorAngle = 2 * self.halfApertureAngle / self.inputDim
            self.halfMiddleApertureAngle = sensors ['halfMiddleApertureAngle']

        if 'lidarDistances' in sensors:
            self.lidarDistances = sensors ['lidarDistances']
        else:
            self.sonarDistances = sensors ['sonarDistances']

        self.runX = np.array ([pm.finity for sectorIndex in range (self.inputDim)])
        self.runX = self.runX.reshape (1, self.inputDim)

    def sweep (self):
        if hasattr (self, 'lidarDistances'):
            for lidarAngle in range (-self.halfApertureAngle, self.halfApertureAngle):
                sectorIndex = round (lidarAngle / self.sectorAngle)
                self.runX [0, sectorIndex] = min (self.runX [0, sectorIndex], self.lidarDistances [lidarAngle])
        else:
            for sectorIndex in (-1, 0, 1):
                self.runX [0, sectorIndex] = min (self.runX [0, sectorIndex], self.sonarDistances [sectorIndex])

        # print ('runX:', self.runX)
        self.runX = self.trainingScalerX.transform (self.runX)
        # print ('runX:', self.runX)

        if nnLibraryName == 'sklearn':
            self.predictedRunY = self.model.predict (self.runX) .reshape (1, 1)
        else:
            self.predictedRunY = self.model (self.runX)
        # print ('predictedRunY:', self.predictedRunY)
        
        self.predictedRunY = self.trainingScalerY.inverse_transform (self.predictedRunY)
        self.steeringAngle = self.predictedRunY [0, 0]
        # print ('steeringAngle:', self.steeringAngle)

        self.targetVelocity = pm.getTargetVelocity (self.steeringAngle)

    def output (self):
        actuators = {
            'steeringAngle': self.steeringAngle,
            'targetVelocity': self.targetVelocity
        }

        self.socketWrapper.send (actuators)

neuralNet = NeuralNet (pm.sampleFileName)




#!/usr/bin/env python

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
from tensorflow.keras.models import Sequential

class NeuralModel(Sequential, learning_rate):
    
    def __init__(self):
        input_shape = (1, 1, 1, 3)
        n_classes = 4

        super().model.Sequential([
            resize_and_rescale,
            data_augmentation,
            layers.Conv2D(32, (3,3), activation='relu', input_shape=input_shape),
            layers.MaxPooling2D((2,2)),
            layers.Conv2D(64, (3,3), activation='relu'),
            layers.MaxPooling2D((2,2)),
            layers.Conv2D(64, (3,3), activation='relu'),
            layers.MaxPooling2D((2,2)),   
            layers.Dropout(0.2), 
            layers.Conv2D(128, (3,3), activation='relu'),
            layers.MaxPooling2D((2,2)),
            layers.Conv2D(128, (3,3), activation='relu'),
            layers.MaxPooling2D((2,2)),
            layers.Conv2D(258, (3,3), activation='relu'),
            layers.MaxPooling2D((2,2)),    
            layers.Flatten(),
            layers.Dense(64, activation='relu'),
            layers.Dense(n_classes, activation='softmax')          
        ])
    
    self.compile(
        optimizer = tf.keras.optimizers.Adam(learning_rate=0.0001),
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
        metrics=['accuracy']
    )
    
    def train():
        pass
    
def main(self):
    neuralModel = NeuralModel(0.001)
    neuralModel.train()
import tensorflow as tf
from tensorflow import keras
from keras.layers.models import Sequential, Dense, Flatten, Convolution2D, Dropout
import numpy as np
import matplotlib.pyplot as plt
import cv2


def training(model):
    model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(512, activation=tf.nn.relu),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Convolution2D()
        tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    ]
    )
    return

def create_model():

    return model

def predict():

    return

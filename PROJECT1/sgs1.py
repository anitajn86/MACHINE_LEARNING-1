import sklearn
import tensorflow
import keras
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.utils import shuffle

data=pd.read_csv("student-mat.csv", sep=";")

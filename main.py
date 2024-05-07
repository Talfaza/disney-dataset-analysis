import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pylab as plt
"""
ggplot : uses R ggplot style formating

""" 
plt.style.use('ggplot')


#open the data set using pandas
dataFrame = pd.read_csv('netflix.csv')


print(dataFrame.head())
#

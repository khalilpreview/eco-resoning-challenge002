import numpy as np
from PIL import Image
import pandas as pd 


# import matplotlib
# from numpy import genfromtxt
# from matplotlib import pyplot
# from matplotlib.image import imread


# my_data = genfromtxt('data/img.csv', delimiter=',')
# matplotlib.image.imsave('output.png', my_data, cmap='gray')
# image_1 = imread('output.png')
# plot raw pixel data
# pyplot.imshow(image_1)
# # show the figure
# pyplot.show()

df = pd.read_csv('database/img.csv', index_col=1, header=1, usecols=range(0, 151))

df = df.fillna(0)

print(df)




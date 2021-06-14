from matplotlib import pyplot as plt
import numpy as np
import pdb # this is for debugging your code
import pandas as pd

#Question 1
# Read the data from the file fdata.csv using read_csv() and save the data in df. 
# The reference of read_csv(): https://www.geeksforgeeks.org/python-read-csv-using-pandas-read_csv/ 
# You need to set the parameters (sep, parse_dates, index_col) in read_csv() properly
#df = pd.read_csv(XXX, sep=XXX, parse_dates=XXX, index_col=XXX)

#1. your code is here
# plot the figure
df.plot()
plt.show()

#Question 2


# Save the data in the variable "data"
# Each row is saved in a tuple 
#data = [('2016-10-03', 772.559998), ... ]

#2. your code is here



# Plot the data as a red line with round markers

#3. your code is here

# set the ticks, labels, titles, grids
#4. your code is here

# Turn on the minor TICKS, which are required for the minor GRID
plt.minorticks_on()

# Customize the major grid
#plt.grid(which=XXX, linestyle=XXX, linewidth=XXX, color=XXX)
#5. your code is here

# Customize the minor grid
#6. your code is here 

plt.show()


#Question 3

# please save assign the data in variables 
#popularity = [XXX, XXX, ...]
# 1. your code is here

# plot the bar chart 
# plt.XXX(XXX, XXX, color=XXX)
# 2. your code is here


# set ticks, labels, titles, grids
#3. your code is here


# Turn on the grid
#4. your code is here



plt.show()

#Question 4
# save the data in variables
#1. your code is here


# plot the bar chart
#2. your code is here

plt.show()

#Question 5
weight1=[67,57.2,59.6,59.64,55.8,61.2,60.45,61,56.23,56]
height1=[101.7,197.6,98.3,125.1,113.7,157.7,136,148.9,125.3,114.9]
weight2=[61.9,64,62.1,64.2,62.3,65.4,62.4,61.4,62.5,63.6]
height2=[152.8,155.3,135.1,125.2,151.3,135,182.2,195.9,165.1,125.1]
weight3=[68.2,67.2,68.4,68.7,71,71.3,70.8,70,71.1,71.7]
height3=[165.8,170.9,192.8,135.4,161.4,136.1,167.1,235.1,181.1,177.3]
# your code is here to draw the scatter plot


plt.show()


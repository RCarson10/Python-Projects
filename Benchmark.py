# Ronald Carson
# CST-305
# February, 2021
# Project 6
# In this code, the program will print a plot that has the two solutions to the system of linear DE's from part 2
# The data is graphed using pyplot
# Packages: matplotlib->pyplot, numpy, scipy->odient, time->time().time
# Import the required modules
import numpy as np
import matplotlib.pyplot as plt
# This makes the plots appear inside the notebook
# This import makes it possible to find the solution of the ODE.
from scipy.integrate import odeint

# Create an array to hold the y values from the solution of the equations
y1 = []
y2 = []
# Create the values for t
t = np.linspace(1, 100)
# Create the loop to display the functions
for i in t:
    x1 = np.exp((-1/20) * i)
    x2 = -1 * np.exp((-1/20) * i)

    # Add values into arrays
    y1.append(x1)
    y2.append(x2)

# Label x and y
plt.ylabel('The solution to the line at the value t')
plt.xlabel('T from 1 to 100')
# Set title
plt.title('Solution to IVP ')

plt.plot(t, y1)  # Plots the first graph in BLUE
plt.plot(t, y2)  # Plots the second graph in RED
plt.show()  # Plots both graphs and gives off a purple color, but you will see blue from the odeint answer
plt.rcParams.update({'font.size': 10})  # increase the font size



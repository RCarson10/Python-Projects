# Ronald Carson
# CST-305
# February 15, 2021
# Project 2
# In this code, the ODE dydt = G(t,s) was the equation modeled using Green's Functions compared with odeint
# From there it was solved using odeint and numpy. The data is graphed using pyplot
# Packages: matplotlib->pyplot, numpy, scipy->odient
# Import the required modules
import numpy as np
import matplotlib.pyplot as plt
# This makes the plots appear inside the notebook
# This import makes it possible to find the solution of the ODE.
from scipy.integrate import odeint

# Generate the list of x values for the functions
limit = 1000
ts = np.linspace(0,50,limit)

# This model solves the Second differential equation given using odeint() and plots the line
def equation2Green():
    # Array that holds the answers from odeint()
    os = []
    # Array that hold the answers from Green's Function
    ts = []
    # Step size hardcoded
    stepSize = 50/limit
    #  Initialize i
    i = 0
    #  Creates a loop that will loop until the step size is reached incrementing i by the step
    while i < 50:
        # Calculate y from the general solution from Green's method
        y = 4 - 4*np.cos(i)
        # add solutions to arrays
        ts.append(i)
        os.append(y)
        # Increment loop
        i = i + stepSize

    # Plot points for os and ts
    plt.plot(ts,os)
    # Plot labels and show graph
    plt.xlabel("Time")
    plt.ylabel("Y")
    plt.title("Green's Function of y'' + y = 4")
    plt.show()
# Solve the second ODE using odeint
def equation1_odeint(u,t):
    # Convert the ODE from second ored into two first order ODE's so odeint can work
    return [u[1], -2*u[1] - 0*u[0] + (2*t-2)]
def equation2_odeint_Model(ts):
    # intial condition
    y0 = [0, 0]

    # Solve with odeint
    us = odeint(equation2_odeint, y0, ts)
    ys = us[:,0]

    # Plot the graph along with the labels
    plt.plot(ts, ys)
    plt.xlabel("Time")
    plt.ylabel("Y")
    plt.title("ODEint() solution for y''+ y = 4")
    plt.show()
# This model solves the Second differential equation given using odeint() and plots the line
def equation1Green():
    # Array that holds the answers from odeint()
    os = []
    # Array that hold the answers from Green's Function
    ts = []
    # Step size hardcoded
    stepSize = 50/limit
    #  Initialize i
    i = 0
    #  Creates a loop that will loop until the step size is reached incrementing i by the step
    while i < 50:
        # Calculate y from the general solution from Green's method
        y = (-0.75*np.exp(-2*i)) + 0.75 + (0.5 * (i**2) - (3/2)*i)
        # add solutions to arrays
        ts.append(i)
        os.append(y)
        # Increment loop
        i = i + stepSize

    # Plot points for os and ts
    plt.plot(ts,os)
    # Plot labels and show graph
    plt.xlabel("Time")
    plt.ylabel("Y")
    plt.title("Green's Function of y'' + 2y' = 2x - 2")
    plt.show()
def equation1_odeint_Model(ts):
    # intial condition
    y0 = [0, 0]

    # Solve with odeint
    us = odeint(equation1_odeint, y0, ts)
    ys = us[:,0]

    # Plot the graph along with the labels
    plt.plot(ts, ys)
    plt.xlabel("Time")
    plt.ylabel("Y")
    plt.title("ODEint() solution for y''+ 2y' = 2x - 2")
    plt.show()

# Solves the second equation with odeint
def equation2_odeint(u, t):
    # This does the same thing as the first method did, just with the second equation
    return [u[1], -0*u[1] - 1*u[0] + 4]

# Solve the models with odeInt
equation1_odeint_Model(ts)
equation2_odeint_Model(ts)

# Call the two models that will show the Green's function outputs
equation1Green()
equation2Green()










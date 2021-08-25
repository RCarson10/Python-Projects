# Ronald Carson
# CST-305
# March, 2021
# Project 6
# In this code, the program will print plots showing the three equations in this project and then the graphs showing
# convergence
# The data is graphed using pyplot
# Packages: matplotlib->pyplot, numpy, scipy->odient, time->time().time
# Import the required modules
import numpy as np
import matplotlib.pyplot as plt
# This makes the plots appear inside the notebook
# This import makes it possible to find the solution of the ODE.
from scipy.integrate import odeint

# Equation 1 in part 1
x = np.linspace(0, 1, 1000)
x1 = np.linspace(-10,10)

def equation1_Part1(x):
    return 1 + x - 1/2*x ** 2 + 2/3*x ** 3 - 1/12*x ** 4 - 1/15*x ** 5 + 1/30*x ** 6
# Equation 2 in part 1
def equation2_Part1(x):
    return -x + 1 / 2 * x ** 2 - 1 / 6 * x ** 3 + 1 / 12 * x ** 4 - 1 / 24 * x ** 5 + 1 / 80 * x ** 6
# Equation 1 in part 2
def equation1_Part2(x):
    return 1 - 1 / 2 * x ** 2 + 1 / 6 * x ** 3 + 1 / 12 * x ** 4 - 1 / 20 * x ** 5 - 1 / 180 * x ** 6 + 1/126*x ** 7 - 1/3360 * x ** 8

# Graph for equation 1 part 1 1000 points from 0 t0 1
# Plot points for x and y
y = equation1_Part1(x)
plt.plot(x,y)
# Plot labels and show graph
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Taylor series method of y'' + 2y' - (x^2 + y^2)  = 0")
plt.show()

# Graph for equation 2 part 1 1000 points from 0 t0 1
# Plot points for x and y
y = equation2_Part1(x)
plt.plot(x,y)
# Plot labels and show graph
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Taylor series method of y'' -  e^y  = 0")
plt.show()

# Graph for equation 1 part 2 1000 points from 0 t0 1
# Plot points for x and y
y = equation1_Part2(x)
plt.plot(x,y)
# Plot labels and show graph
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Power series method of y'' + (v+1)y' + y = 0")
plt.show()
def problem_2_odeint(u, x):
    # return system of equations that makes up problem 2
    return [u[1], np.exp(u[0])]

def problem_1_odeint(U, t):
    # return the second order ode as first order system
    return [U[1], t**2 + U[0]**2 - 2*U[1]]

# Using the two previously defined DE's, plot the graph's to show convergence
y0 = [0,0]
y1 = odeint(problem_1_odeint, y0, x)
y2 = odeint(problem_2_odeint, y0, x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Odeint for convergence of Problem 1 and 2 from part 1")
plt.show()

# From the previous equations, this shows the constraints of the series in part 1
y1 = equation1_Part1(x1)
y2 = equation2_Part1(x1)
plt.plot(x1, y1)
plt.plot(x1, y2)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Convergence Constraints")
plt.show()

# Part three graph and calculation using odeint

t = np.linspace(1, 60)
y0 = 0 # the initial condition, starting from O since the clock cycle has not begun
def dy_dx(k,t):  # The ode being dy_dt
    k = 50
    dydt = k * 100 * t
    return dydt

ys = odeint(dy_dx, y0, t)  # Solve the ODE
plt.plot(t, ys)  # Plots graph
plt.ylabel('Instructions a Second')
plt.xlabel('Time in Seconds')
# Set title
plt.title('CPU Time')

plt.show()  # Shows graph from the odeint answer
plt.rcParams.update({'font.size': 10})  # increase the font size


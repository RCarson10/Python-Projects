# Ronald Carson
# CST-305
# March 13, 2021
# Project 5
# In this code, the program will calculate and display the lorenz equations to model file exhaustion through a dynamical
# system with three files, one storage.
# The data is graphed using pyplot and it's special package that implements a 3D plot.
#
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Lorenz parameters and initial conditions
sigma, beta, rho = 10, 8/3,25       # The only variable that was altered is the rho value to test for a dynamical system
u0, v0, w0 = 0.512, 0.256,0.512 # The initial values rep

# Maximum time point and total number of time points
tmax, n = 100, 10000

# Define the three lorenz equations that will be used in the program
def lorenz(X, t, sigma, beta, rho):
    """The Lorenz equations."""
    u, v, w = X
    up = -sigma * (u - v)
    vp = rho * u - v - u * w
    wp = -beta * w + u * v
    return up, vp, wp


# Integrate the Lorenz equations on the time grid t
t = np.linspace(0, tmax, n)
f = odeint(lorenz, (u0, v0, w0), t, args=(sigma, beta, rho))
x, y, z = f.T

# Plot the Lorenz attractor using a Matplotlib 3D projection
fig = plt.figure()
ax = fig.gca(projection='3d')

# Make the line multi-coloured by plotting it in segments of length s which
# change in colour across the whole time series.
s = 10
c = np.linspace(0, 1, n)
for i in range(0, n - s, s):
    ax.plot(x[i:i + s + 1], y[i:i + s + 1], z[i:i + s + 1], color=(1, c[i], 0), alpha=0.4)

# Remove all the axis clutter, leaving just the curve.
ax.set_axis_off()

# Plot X and T to show if the graph is oscillating observing the X and T plane.
plt.show()
plt.title("T and X")
plt.xlabel("T")
plt.ylabel("X")
plt.plot(t, x)
plt.show()
# Plot Y and T to show if the graph is oscillating observing the Y and T plane.
plt.title("T and Y")
plt.xlabel("T")
plt.ylabel("Y")
plt.plot(t, y)
plt.show()
# Plot Z and T to show if the graph is oscillating observing the Z and T plane.
plt.title("T and Z")
plt.xlabel("T")
plt.ylabel("Z")
plt.plot(t, z)
plt.show()
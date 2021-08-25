# Ronald Carson
# CST-305
# April 15, 2021
# Project 8
# In this code, the program will calculate and display the solutions to integrals with Reimann sums
# The data is graphed using pyplot and it's special package that implements a plot with rectangles.
# The code will also model this with downloading a  file.
import numpy as np
from scipy.integrate import simps
import scipy as sci
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from scipy import integrate

# Define the function sin(x)+ 1, plot rectangles and computer midpoints
f = lambda x: np.sin(x) + 1
a = (-1) * np.pi;
b = np.pi;
N = 4
n = 10  # Use n*N+1 points to plot the function smoothly

x = np.linspace(a, b, N + 1)
y = f(x)

X = np.linspace(a, b, n * N + 1)
Y = f(X)

plt.figure(figsize=(15, 5))


# Create the left sum graph
plt.subplot(1, 3, 1)
plt.plot(X, Y, 'b')
x_left = x[:-1]  # Left endpoints
y_left = y[:-1]
plt.plot(x_left, y_left, 'b.', markersize=10)
plt.bar(x_left - 0.75, height=y_left + 1, width=(b - a) / N, alpha=0.2, bottom=-1, align='edge', edgecolor='b')
plt.title('Left Riemann Sum of sin(x) + 1 , N = {}'.format(N))

plt.subplot(1, 3, 2)
plt.plot(X, Y, 'b')
x_mid = (x[:-1] + x[1:]) / 2  # Midpoints
y_mid = f(x_mid)
plt.plot(x_mid, y_mid, 'b.', markersize=10)
plt.bar(x_mid, y_mid + 1, width=(b - a) / N, alpha=0.2, bottom=-1, edgecolor='b')
plt.title('Midpoint Riemann Sum of sin(x) + 1, N = {}'.format(N))

plt.subplot(1, 3, 3)
plt.plot(X, Y, 'b')
x_right = x[1:]  # Right endpoints
y_right = y[1:]
plt.plot(x_right, y_right, 'b.', markersize=10)
plt.bar(x_right - 0.75, y_right + 1.5, width=(b - a) / N, alpha=0.2, bottom=-1.5, align='edge', edgecolor='b')
plt.title('Right Riemann Sum of sin(x) + 1, N = {}'.format(N))

dx = (b-a)/N
x_left = np.linspace(a,b-dx,N)
x_midpoint = np.linspace(dx/2,b - dx/2,N)
x_right = np.linspace(dx,b,N)

print("sin(x) + 1 Partition with",N,"subintervals.")
left_riemann_sum = np.sum(f(x_left) * dx)
print("Left Riemann Sum:",left_riemann_sum)

midpoint_riemann_sum = np.sum(f(x_midpoint) * dx)
print("Midpoint Riemann Sum:",midpoint_riemann_sum)

right_riemann_sum = np.sum(f(x_right) * dx)
print("Right Riemann Sum:",right_riemann_sum)
area = sci.integrate.quad(lambda x: np.sin(x) + 1,-np.pi,np.pi)[0]
print("The area under the curve is:",area,"\n")


plt.show()

# Plot 3x + 2x^2 and the area under the curve

f2 = lambda x: 3 * x + 2 * x ** 2
a = 0;
b = 1;
N = 50
n = 10  # Use n*N+1 points to plot the function smoothly

x = np.linspace(a, b, n)
y = f2(x)

X = np.linspace(a, b, n)
Y = f2(X)

a, b = 0, 1  # integral limits
x = np.linspace(0, 1)
y = f2(x)


plt.figure(figsize=(7, 7))
plt.title("Right Riemann sum of 3x + 2x^2")
plt.plot(X, Y, 'b')
x_right = x[1:]  # Right endpoints
y_right = y[1:]
plt.plot(x_right, y_right, 'b.', markersize=10)
plt.bar(x_right, y_right, width=(b - a) / N, alpha=0.2, bottom= 0, align='edge', edgecolor='b')

dx = (b-a)/N
x_left = np.linspace(a,b-dx,N)
x_midpoint = np.linspace(dx/2,b - dx/2,N)
x_right = np.linspace(dx,b,N)

print("3x + 2x^2 Partition with",N,"subintervals.")
left_riemann_sum = np.sum(f2(x_left) * dx)
print("Left Riemann Sum:",left_riemann_sum)

midpoint_riemann_sum = np.sum(f2(x_midpoint) * dx)
print("Midpoint Riemann Sum:",midpoint_riemann_sum)

right_riemann_sum = np.sum(f2(x_right) * dx)
print("Right Riemann Sum:",right_riemann_sum)
area = sci.integrate.quad(lambda x: 3 * x + 2 * x ** 2,0,1)[0]
print("The area under the curve is:", area,"\n")

plt.show()
# Plot the integral from 1 to e of the function of ln(x)

F = lambda x: np.log(x)
a = 1;
b = np.e;
N = 1000
n = 10  # Use n*N+1 points to plot the function smoothly


x2 = np.linspace(1, np.e, 100)
y2 = F(x2)

fig2, ax1 = plt.subplots()
ax1.plot(x2, y2, 'r', linewidth=2)
ax1.set_ylim(bottom=0)
plt.fill_between(x2,y2)
ax1.set_title("Integral of ln(x)")

fig2.text(0.9, 0.05, '$x$')
fig2.text(0.1, 0.9, '$y$')

dx = (b-a)/N
x_left = np.linspace(a,b-dx,N)

left_riemann_sum = np.sum(f2(x_left) * dx)
print("Left Riemann Sum of ln(x) from 1 to e:",left_riemann_sum)

area = sci.integrate.quad(lambda x: np.log(x),1,np.e)[0]
print("The area under the curve for ln(x) from 1 to e is:", area,"\n")
plt.show()

# Plot x^2-x^3 and the area under the curve
f = lambda x: x**2 - x**3
a = -1;
b = 0;
N = 100
n = 10  # Use n*N+1 points to plot the function smoothly

x = np.linspace(a, b, N + 1)
y = f(x)

X = np.linspace(a, b, n * N + 1)
Y = f(X)

plt.figure(figsize=(7, 7))

plt.plot(X, Y, 'b')
x_right = x[1:]  # Right endpoints
y_right = y[1:]
plt.plot(x_right, y_right, 'b.', markersize=10)
plt.bar(x_right - 0.01, y_right + 1, width=(b - a) / N, alpha=0.2, bottom=-1, align='edge', edgecolor='b')
plt.title('Right Riemann Sum of x^2 - x^3')

print("x^2 - x^3 Partition with",N,"subintervals.")
left_riemann_sum = np.sum(f(x_left) * dx)
print("Left Riemann Sum:",left_riemann_sum)

midpoint_riemann_sum = np.sum(f(x_midpoint) * dx)
print("Midpoint Riemann Sum:",midpoint_riemann_sum)

right_riemann_sum = np.sum(f(x_right) * dx)
print("Right Riemann Sum:",right_riemann_sum)
area = sci.integrate.quad(lambda x: x**2 - x**3,-1,0)[0]
print("The area under the curve is:",area,"\n")



plt.show()

# Part 2
xs = np.linspace(0, 30,30)
ys = [22.2,16.2,18.9,17.4,21.5,22.3,19.6,21.5,21.9,21.7,22.1,21.4,22.4,22,22,22.2,22,22.3,22,21.5
    ,21.2,21.6,21.7,21.3,21.2,21.4,21.2,21.1,21.3,21.2]

plt.plot(xs, ys, 'b.', markersize = 1)
plt.fill_between(xs, ys, alpha = 0.2, edgecolor = 'b')
plt.xlabel("Time (minutes)")
plt.ylabel("Data Download Speed (Megabits per Second)")
plt.title("Download Speed vs Time")
plt.show()

# The area under the curve/integral calculation
for i in range(len(ys)): ys[i] *= 60.0
print("\nThe integral of the data download speeds is: ", simps(ys, xs), "megabits")

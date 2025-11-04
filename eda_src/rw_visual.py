import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Calls a random walk
rw = RandomWalk()
rw.fill_walk()

# Plots the walk's steps
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_aspect('equal')
plt.show()
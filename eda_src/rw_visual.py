import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keeps creating new walks, while the program remains active
while True:
    # Calls a random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plots the walk's steps
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_aspect('equal')
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
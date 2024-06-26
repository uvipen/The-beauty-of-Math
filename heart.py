import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from math import pi, e, sqrt

# Set up the figure, axis, and plot element
fig, ax = plt.subplots()
x = np.linspace(-sqrt(pi), sqrt(pi), 1000)
plt.title(r'LOVE(x) = $x^{\frac{2}{3}} + \dfrac{e}{3}\sqrt{(\pi - x^2)}*sin(a\pi x)$', color="purple", fontsize=20)
ax.set_xlim(-2, 2)
ax.set_ylim(-1.5, 3)
points, = ax.plot([], [], 'r-')

frame_text = ax.text(0.4, 0.9, '', transform=ax.transAxes, fontsize=20, color="green")


# Initialization function
def init():
    points.set_data([], [])
    frame_text.set_text('')
    return points,


# Update function
def update(frame):
    y = np.power(x ** 2, 1 / 3) + e / 3 * (pi - x ** 2) ** 0.5 * np.sin(frame * pi * x / 10)
    points.set_data(x, y)
    frame_text.set_text("a = {}".format(frame / 10))
    return points, frame_text


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 301), init_func=init, blit=True, interval=50,
                              repeat=False)
writer = animation.FFMpegFileWriter(fps=60)
ani.save("love.gif", writer='ffmpeg')
# Display the animation
plt.show()

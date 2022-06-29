
#import webcolors
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as plta

from matplotlib.ticker import LinearLocator # used avt dernière ligne


#webcolors.rgb_to_hex((12,232,23))
fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-5, 5, 0.25)
xlen = len(X)
Y = np.arange(-5, 5, 0.25)
ylen = len(Y)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Create an empty array of strings with the same shape as the meshgrid, and
# populate it with two colors in a checkerboard pattern.
colortuple = ('c','b')
colors = np.empty(X.shape, dtype=str)
for y in range(ylen):
    for x in range(xlen):
        colors[x, y] = colortuple[(x + y) % len(colortuple)]

# Plot the surface with face colors taken from the array we made.
surf = ax.plot_surface(X, Y, Z, facecolors=colors, linewidth=0)

# Customize the z axis.
ax.set_zlim(-1, 1)
ax.w_zaxis.set_major_locator(LinearLocator(6)) # linearlocator

plt.show()

def rotate(angle):
    ax.view_init(azim=angle)

rot_animation = plta.FuncAnimation(fig, rotate, frames=np.arange(0,362,2),interval=100)

rot_animation.save('F:Cours Python/rotationgif.gif', dpi=80, writer='imagemagick')
rot_animation.save('F:Cours Python/rotationpng.png', dpi=80, writer='imagemagick')

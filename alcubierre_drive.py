#!/usr/local/bin/python
'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
##
# Yasin Khalil (www.yasinkhalil.com)
# 2FC7 638E 1926 F27 (https://keybase.io/ysnkhll)
# 02/06/2024 - Crazyvoid - Modified to work with latest python 
##

import time
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Import for 3D projection
import numpy as np

np.seterr(divide='ignore', invalid='ignore')
mpl.rcParams['toolbar'] = 'None'

def rho(y, z):
    return np.sqrt(y**2 + z**2)

def d_rs(x, rho, xs=2.5):
    return ((x - xs)**2 + rho**2)**(1/2)

def d_frs(rs, sigma=8, R=1):
    a = sigma * (np.tanh((R + rs)*sigma)**2 - 1)
    b = sigma * ((np.tanh(-(R - rs)*sigma)**2 - 1) / np.tanh(R * sigma))
    return (-1/2) * (a - b)

def theta(x, p, xs=2.5, s=8, R=1):
    vs = R
    drs = d_rs(x, p, xs)
    dfrs = d_frs(drs, s, R)
    return vs * ((x - xs) / drs) * dfrs

# Create the Figure and 3D subplot.
fig = plt.figure(dpi=96)
fig.canvas.setWindowTitle('Alcubierre Warp Drive')
ax = fig.add_subplot(111, projection='3d')  # Use add_subplot for 3D projection

# Add latex math labels.
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')

# Inputs vectors.
x = np.linspace(1.0, 8.0, num=160)
p = np.linspace(-4.0, 4.0, num=160)

# Generate coordinate matrices from coordinate vectors.
X, P = np.meshgrid(x, p)

# Set the axis limits so they aren't recalculated each frame.
ax.set_xlim(1.0, 8.0)
ax.set_ylim(-4, 4)
ax.set_zlim(-4.2, 4.2)

# Begin plotting.
frame = None
csets = []

for xs in np.linspace(1.0, 10.0, 200):

    if frame:
        frame.remove()

    if csets:
        for sets in csets:
            if sets.collections:
                for cols in sets.collections:
                    cols.remove()
                csets.remove(sets)

    # Calculate the metric tensor.
    Z = theta(X, P, xs, 8, 1)

    # Plot the Surface.
    frame = ax.plot_wireframe(
        X, P, Z, rstride=2, cstride=2, linewidth=0.5, antialiased=True)

    # Plot projections of the contours for each dimension.
    csets.append(ax.contour(X, P, Z, zdir='x', offset=1, cmap=plt.cm.coolwarm))
    csets.append(ax.contour(X, P, Z, zdir='y', offset=4, cmap=plt.cm.coolwarm))
    csets.append(ax.contour(X, P, Z, zdir='z', offset=-4.2, cmap=plt.cm.coolwarm))

    # Wait
    plt.pause(0.001)

plt.show()

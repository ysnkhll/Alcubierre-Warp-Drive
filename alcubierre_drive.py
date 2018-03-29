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
## 
import math

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

np.seterr(divide='ignore', invalid='ignore')
mpl.rcParams['toolbar'] = 'None'

def rho(y, z):
    return np.sqrt(y**2 + z**2)


def d_rs(x, rho, xs=15):
    return ((x - xs)**2 + rho**2)**(1/2)


def d_frs(rs, sigma=8, R=1):
    a = sigma * (np.tanh((R + rs)*sigma)**2 - 1)
    b = sigma * ((np.tanh(-(R - rs)*sigma)**2 - 1) / np.tanh(R * sigma))
    return (-1/2) * (a - b)


def theta(x, p, xs=15, s=8, R=1):
    vs = R
    drs = d_rs(x, p, xs)
    dfrs = d_frs(drs, s, R)

    return vs * ((x - xs) / drs) * dfrs


# Inputs vectors.
x = np.linspace(1, 4, 500)
p = np.linspace(-1.5, 1.5, 500)

# Generate coordinate matrices from coordinate vectors.
X, P = np.meshgrid(x, p)

# Calculate the metric tensor.
Z = theta(X, P, 2.5, 8, 1)

# Create the Figure.
fig = plt.figure(dpi=96)
fig.canvas.set_window_title('Alcubierre Warp Drive')
ax = fig.gca(projection='3d')

# Plot the Surface.
ax.plot_wireframe(X, P, Z)

# Tweak the limits and add latex math labels.
ax.set_zlim(0, 5)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')

# Display the plot.
plt.show()

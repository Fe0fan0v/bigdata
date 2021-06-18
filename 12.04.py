from vpython import sphere, vector, color, rotate
from math import sqrt

G = 6.667e-11
MS = 1.9885e30
ME = 5.97e24
MM = 7.348e22
RSE = 1.496e11
F_SE = G * MS * ME / (RSE ** 2)
WE = sqrt(F_SE / (ME * RSE))
REM = 384.4e6
F_EM = G * ME * MM / (REM ** 2)
WM = sqrt(F_EM / (MM * REM))


v = vector(0.5, 0, 0)
earth = sphere(pos=vector(215, 0, 0), color=color.blue, radius=0.009, make_trail=True)
sun = sphere(pos=vector(0, 0, 0), color=color.yellow, radius=1)
moon = sphere(pos=earth.pos + v, color=color.white, radius=0.0025, make_trail=True)
dt = 10
omega = 0.5
delta_e = WE * dt
delta_m = WM * dt
while dt <= 365 * 86400:
    earth.pos = rotate(earth.pos, angle=delta_e, axis=vector(0, 0, 1))
    v = rotate(v, angle=delta_m, axis=vector(0, 0, 1))
    moon.pos = earth.pos + v
    dt += 10


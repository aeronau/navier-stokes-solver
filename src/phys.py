import numpy as np

"""
sx and sy are staggered arrays
cx and cy are centered arrays
"""

def convection(u, v, sx, sy, cx, cy, N):

    convection_x = np.zeros((N + 1, N + 1))
    convection_y = np.zeros((N + 1, N + 1))

    Δx = np.diff(sx)
    Δx⁻ = Δx.pop(-1)
    Δx⁺ = Δx.pop(0)
    Δy = np.diff(sy)
    Δy⁻ = Δy.pop(-1)
    Δy⁺ = Δy.pop(0)

    for i in range(1, N)
        for j in range(1, N)

            ω_x = (cx[i + 1] - cx[i]) * (sy[j] - sy[j - 1])

            un = ( u[i, j + 1] + u[i, j] ) / 2
            ue = ( u[i + 1, j] + u[i, j] ) / 2
            us = ( u[i, j - 1] + u[i, j] ) / 2
            uw = ( u[i - 1, j] + u[i, j] ) / 2

            uFn = ( v[i, j] * Δx⁻ + v[i + 1, j] * Δx⁺ ) / 2
            uFe = ( u[i, j] * Δy + u[i + 1, j] * Δy ) / 2
            uFs = ( v[i, j - 1] * Δx⁻ + v[i + 1, j - 1] * Δx⁺ ) / 2
            uFw = ( u[i - 1, j] * Δy + u[i, j] * Δy ) / 2

            convection_x[i, j] = ( uFn*un + uFe*ue - uFs*us - uFw*uw ) / ω_x

def diffusion(u, v, sx, sy, cx, cy, N):

    diffusion_x = np.zeros((N + 1, N + 1))

    for i in range(1, N)
        for j in range(1, N)

            uGn = ( u[i, j + 1] - u[i, j] ) / ( cy[j + 1] - cy[j] )
            uGe = ( u[i + 1, j] - u[i, j] ) / ( sx[i + 1] - sx[i] )
            uGs = ( u[i, j] - u[i, j - 1] ) / ( cy[j] - cy[j - 1] )
            uGw = ( u[i, j] - u[i - 1, j] ) / ( sx[i] - sx[i - 1] )

            vGn = ( v[i, j + 1] - v[i, j] ) / ( sy[j + 1] - sy[j] )
            vGe = ( v[i + 1, j] - v[i, j] ) / ( cx[i + 1] - cx[i] )
            vGs = ( v[i, j] - v[i, j - 1] ) / ( sy[j] - sy[j - 1] )
            vGw = ( v[i, j] - v[i - 1, j] ) / ( cx[i] - cx[i - 1] )

            diffusion_x = np.zeros((N + 2, N + 2)) / ω_x
            diffusion_y = np.zeros((N + 2, N + 2)) / ω_y

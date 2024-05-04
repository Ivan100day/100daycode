"""Implementation of mandelbrot"""

MAX_ITER = 80


def mandelbrot(z, n, c):

    if abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
        return mandelbrot(z, n, c)
    return n


"""Plotting function for mandelbrot"""
from PIL import Image, ImageDraw
from mandelbrot import mandelbrot, MAX_ITER

def plot_figure():


    WIDTH = 600
    HEIGHT = 400

    START = -2
    END = 1
    START_IM = -1
    END_IM = 1

    palette = []

    im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(im)

    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            c = complex(START + (x / WIDTH) * (END - START),
                        START_IM + (y / HEIGHT) * (END_IM - START_IM))
            m = mandelbrot(0, 0, c)
            color = 255 - int(m * 255 / MAX_ITER)
            draw.point([x, y], (color, color, color))

    im.save('Mandelbrot_img.png', 'PNG')

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
import random
import numpy as np
import noise

BLACK, DARKGRAY, GRAY = ((0, 0, 0), (63, 63, 63), (127, 127, 127))
LIGHTGRAY, WHITE = ((191, 191, 191), (255, 255, 255))


class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y


class Rect(object):
    def __init__(self, x1, y1, x2, y2):
        minx, maxx = (x1, x2) if x1 < x2 else (x2, x1)
        miny, maxy = (y1, y2) if y1 < y2 else (y2, y1)
        self.min = Point(minx, miny)
        self.max = Point(maxx, maxy)

    width = property(lambda self: self.max.x - self.min.x)
    height = property(lambda self: self.max.y - self.min.y)


def gradient_color(minval, maxval, val, color_palette):
    """ Computes intermediate RGB color of a value in the range of minval
        to maxval (inclusive) based on a color_palette representing the range.
    """
    max_index = len(color_palette)-1
    delta = maxval - minval
    if delta == 0:
        delta = 1
    v = float(val-minval) / delta * max_index
    i1, i2 = int(v), min(int(v)+1, max_index)
    (r1, g1, b1), (r2, g2, b2) = color_palette[i1], color_palette[i2]
    f = v - i1
    return int(r1 + f*(r2-r1)), int(g1 + f*(g2-g1)), int(b1 + f*(b2-b1))


def horz_gradient(draw, rect, color_func, color_palette):
    minval, maxval = 1, len(color_palette)
    delta = maxval - minval
    width = float(rect.width)  # Cache.
    for x in range(rect.min.x, rect.max.x+1):
        f = (x - rect.min.x) / width
        val = minval + f * delta
        color = color_func(minval, maxval, val, color_palette)
        draw.line([(x, rect.min.y), (x, rect.max.y)], fill=color)


def vert_gradient(draw, rect, color_func, color_palette):
    minval, maxval = 1, len(color_palette)
    delta = maxval - minval
    height = float(rect.height)  # Cache.
    for y in range(rect.min.y, rect.max.y+1):
        f = (y - rect.min.y) / height
        val = minval + f * delta
        color = color_func(minval, maxval, val, color_palette)
        draw.line([(rect.min.x, y), (rect.max.x, y)], fill=color)


def gradientGenerate(direction):    # Draw a three color vertical gradient.

    colorList = [(211, 24, 83), (233, 172, 0), (0, 138, 203),
                 (212, 114, 167), (30, 42, 200), (95, 200, 108), (222, 103, 62)]
    colorChoice = random.sample(colorList, 3)

    region = Rect(0, 0, 1080, 1080)
    width, height = region.max.x+1, region.max.y+1
    image = Image.new("RGB", (width, height), WHITE)
    draw = ImageDraw.Draw(image)
    if direction == "vert":
        vert_gradient(draw, region, gradient_color, colorChoice)
    elif direction == "hori":
        horz_gradient(draw, region, gradient_color, colorChoice)
    blured = image.filter(ImageFilter.GaussianBlur(100))

    return blured


def noiseGenerate():
    # Noise Generate
    colorList = [(211, 24, 83), (233, 172, 0), (0, 138, 203),
                 (212, 114, 167), (30, 42, 200), (95, 200, 108), (222, 103, 62)]
    colorChoice = random.sample(colorList, 2)

    shape = (1080, 1080)
    scale = random.randint(400, 1200)
    base = random.randint(0, 8)
    world = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            world[i][j] = noise.pnoise2(
                i / scale, j / scale, 4, base=base)
    max = np.amax(world)
    min = np.amin(world)
    max -= min
    world -= min
    world /= max
    world *= 255

    image = Image.fromarray(world.astype('uint8'), 'L')
    image = ImageOps.colorize(
        image, white=colorChoice[0], black=colorChoice[1])
    return image

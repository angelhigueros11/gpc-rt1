from lib import *
from numpy import *
from sphere import *

class Raytracer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background_color =color(0, 0, 0)
        self.current_color = color(255, 255, 255)
        self.clear()
    
    def clear(self):
        self.framebuffer = [
            [self.background_color for x in range(self.width)]
            for y in range(self.height)
        ]
    
    def point(self, x, y, color=None):
        if y >= 0 and y < self.height and x >= 0 and x < self.width:
            self.framebuffer[y][x] = color or self.current_color

    def write(self, filename):
        writebmp(filename, self.width, self.height, self.framebuffer)
    
    def render(self):

        fov = int(pi / 2)
        ar = self.width / self.height
        tana = tan(fov / 2)

        for y in range(self.height):
            for x in range(self.width):
                i = ((2 *  (x + 0.5) / self.width) - 1) * ar * tana
                j = ( 1 - (2 *  (y + 0.5) / self.height)) * tana

                origin = V3(0, 0, 0)
                direction = V3(i, j, -1).norm()
                c = self.cast_ray(origin, direction)

                self.point(x, y, c)

    def cast_ray(self, origin, direction):

            s0 = Sphere(V3(-4, 0, -15), 0.3)
            s0 = s0.ray_intersect(origin, direction)
            s1 = Sphere(V3(-2, 0, -15), 0.3)
            s1 = s1.ray_intersect(origin, direction)
            if s0 or s1:
                return color(255, 128, 0)

            s2 = Sphere(V3(-3, 0, -16), 2)
            s2 = s2.ray_intersect(origin, direction)

            s3 = Sphere(V3(-2, 3, -10), 2)
            s3 = s3.ray_intersect(origin, direction)


            s4 = Sphere(V3(-3, 1, -15), 0.3)
            s4 = s4.ray_intersect(origin, direction)
            if s4:
                return color(255, 0, 0)

            if s2 or s3:
                return color(255, 255, 255)
            else:
                return self.background_color

# IMPLEMENTACION
r = Raytracer(800, 600)
r.render()
r.write('rt1.bmp')

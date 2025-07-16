import pygame
import sys
import math
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


def rotation_matrix_x(theta):
    return [
        [1, 0, 0],
        [0, math.cos(theta), -math.sin(theta)],
        [0, math.sin(theta),  math.cos(theta)]
    ]


def rotation_matrix_y(theta):
    return [
        [math.cos(theta), 0, math.sin(theta)],
        [0, 1, 0],
        [-math.sin(theta), 0, math.cos(theta)]
    ]


def rotation_matrix_z(theta):
    return [
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta),  math.cos(theta), 0],
        [0, 0, 1]
    ]


def multiply_matrix_vector(m, v):
    return [
        m[0][0]*v[0] + m[0][1]*v[1] + m[0][2]*v[2],
        m[1][0]*v[0] + m[1][1]*v[1] + m[1][2]*v[2],
        m[2][0]*v[0] + m[2][1]*v[1] + m[2][2]*v[2],
    ]


class objInfo:
    def __init__(self, x, y, z, rotx=0, roty=0, rotz=0):
        self.x = x
        self.y = y
        self.z = z
        self.rotx = rotx
        self.roty = roty
        self.rotz = rotz

    def addpointstodraw(self, vertices=[]):
        self.vertices = vertices

    def drawverts(self, color, screen, scale):
        self.newverts = []
        for i in range(len(self.vertices)):
            newx = ((self.vertices[i][0] * (scale + cam.z)))
            newy = ((self.vertices[i][1] * (scale + cam.z)))
            rotated = multiply_matrix_vector(rotation_matrix_x(math.radians(self.rotx)), [newx, newy, self.z])
            rotated = multiply_matrix_vector(rotation_matrix_y(math.radians(self.roty)), rotated)
            rotated = multiply_matrix_vector(rotation_matrix_z(math.radians(self.rotz)), rotated)
            newx = rotated[0] - cam.x
            newy = rotated[1] + cam.y

            self.newverts.append([newx, newy])
        pygame.draw.polygon(screen, (color), self.newverts)


cam = objInfo(0, 0, -1)  # create a cam obj
triangle = objInfo(0, 0, 1)  # simple triangle
triangle.addpointstodraw([
        [0, 1, 0], [-1, -1, 0], [1, -1, 0]
    ])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        cam.x += 5
    if keys[pygame.K_a]:
        cam.x -= 5
    if keys[pygame.K_q]:
        cam.y -= 5
    if keys[pygame.K_e]:
        cam.y += 5
    if keys[pygame.K_w]:
        cam.z += 5
    if keys[pygame.K_s]:
        cam.z -= 5

    if keys[pygame.K_RIGHT]:
        triangle.roty += 1
    if keys[pygame.K_LEFT]:
        triangle.roty -= 1

    if keys[pygame.K_UP]:
        triangle.rotx += 1
    if keys[pygame.K_DOWN]:
        triangle.rotx -= 1

    if keys[pygame.K_l]:
        triangle.rotz += 1
    if keys[pygame.K_p]:
        triangle.rotz -= 1

    screen.fill((0, 0, 0))
    triangle.drawverts((255, 0, 0), screen, 100)
    pygame.display.update()
    clock.tick(60)

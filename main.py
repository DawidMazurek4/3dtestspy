import pygame
import sys
import math
from test import *
pygame.init()
screen_dimensions = [800, 800]
screen = pygame.display.set_mode((screen_dimensions[0], screen_dimensions[1]))
clock = pygame.time.Clock()


class camra:
    def __init__(self, position, rotation, fov):
        self.position = position
        self.rotation = rotation
        self.fov = fov


class objInfo:
    def __init__(self, position, vertices, faces, rotation):
        self.position = position
        self.vertices = vertices
        self.faces = faces
        self.rotation = rotation


def changePos(object):
    points = []
    cx, cy, cz = main_cam.position
    ry = math.radians(main_cam.rotation[1])
    cos_y = math.cos(ry)
    sin_y = math.sin(ry)
    rx = math.radians(main_cam.rotation[0])
    cos_x = math.cos(rx)
    sin_x = math.sin(rx)

    for vx, vy, vz in object.vertices:
        scale = 10
        wx = (vx * scale) + object.position[0]
        wy = (-vy * scale) + object.position[1]
        wz = (vz * scale) + object.position[2]

        dx = wx - cx
        dy = wy - cy
        dz = wz - cz

        px = dx * cos_y - dz * sin_y
        pz = dx * sin_y + dz * cos_y

        py = dy * cos_x - pz * sin_x
        pz = dy * sin_x + pz * cos_x

        if pz <= 0:
            return False

        f = main_cam.fov / pz
        screen_x = px * f + screen_dimensions[0] / 2
        screen_y = py * f + screen_dimensions[1] / 2
        points.append([screen_x, screen_y])

    return points if len(points) == len(object.vertices) else False



def drawObject(pos, faces):
    if pos == False:
        return
    for i in range(len(faces)):

        pygame.draw.line(screen, (255, 255, 255), pos[faces[i][0]], pos[faces[i][1]])
        pygame.draw.line(screen, (255, 255, 255), pos[faces[i][1]], pos[faces[i][2]])
        pygame.draw.line(screen, (255, 255, 255), pos[faces[i][2]], pos[faces[i][0]])

main_cam = camra([0, 0, 1], [0, 0, 0], 500)

test_triangle = objInfo([1, 1, 1], points, triangles, [0, 0, 0])
test_triangle2 = objInfo([5, 5, 50], points2, triangles2, [0, 0, 0])
kwadrat = objInfo([0, 0, 0], kwadratp, kwadratt, [0, 0, 0])


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
    if keys[pygame.K_w]:
       main_cam.position[2] += 1
    if keys[pygame.K_s]:
        main_cam.position[2] -= 1
    if keys[pygame.K_a]:
        main_cam.position[0] -= 1
    if keys[pygame.K_d]:
        main_cam.position[0] += 1

    if keys[pygame.K_q]:
        main_cam.position[1] += 1
    if keys[pygame.K_e]:
        main_cam.position[1] -= 1
    
    if keys[pygame.K_RIGHT]:
        main_cam.rotation[1] += 1
    if keys[pygame.K_LEFT]:
        main_cam.rotation[1] -= 1
    if keys[pygame.K_UP]:
        main_cam.rotation[0] -= 1
    if keys[pygame.K_DOWN]:
        main_cam.rotation[0] += 1

    screen.fill((0, 0, 0))
    drawObject(changePos(test_triangle), test_triangle.faces)
    drawObject(changePos(test_triangle2), test_triangle2.faces)
    drawObject(changePos(kwadrat), kwadrat.faces)
    pygame.display.flip()
    clock.tick(60)

import math


def generate_sphere(radius=1.0, lat_segments=10, lon_segments=20):
    vertices = []
    triangles = []

    # Generate vertices
    for i in range(lat_segments + 1):
        theta = math.pi * i / lat_segments  # from 0 to PI
        sin_theta = math.sin(theta)
        cos_theta = math.cos(theta)

        for j in range(lon_segments + 1):
            phi = 2 * math.pi * j / lon_segments  # from 0 to 2PI
            sin_phi = math.sin(phi)
            cos_phi = math.cos(phi)

            x = radius * sin_theta * cos_phi
            y = radius * cos_theta
            z = radius * sin_theta * sin_phi
            vertices.append([x, y, z])

    # Generate triangle indices
    for i in range(lat_segments):
        for j in range(lon_segments):
            p1 = i * (lon_segments + 1) + j
            p2 = p1 + lon_segments + 1

            # two triangles per quad
            triangles.append([p1, p2, p1 + 1])
            triangles.append([p1 + 1, p2, p2 + 1])

    return vertices, triangles

# Example usage:
points, triangles = generate_sphere()
points2, triangles2 = generate_sphere(lon_segments=1, lat_segments=1)

kwadratp = [
    [-1, -1, -1],  # 0
    [ 1, -1, -1],  # 1
    [ 1,  1, -1],  # 2
    [-1,  1, -1],  # 3
    [-1, -1,  1],  # 4
    [ 1, -1,  1],  # 5
    [ 1,  1,  1],  # 6
    [-1,  1,  1],  # 7
]
kwadratt = [
    # dolna (spód)
    [0, 1, 2],
    [0, 2, 3],

    # górna
    [4, 6, 5],
    [4, 7, 6],

    # przód
    [0, 4, 5],
    [0, 5, 1],

    # tył
    [3, 2, 6],
    [3, 6, 7],

    # lewa
    [0, 3, 7],
    [0, 7, 4],

    # prawa
    [1, 5, 6],
    [1, 6, 2]
]


def takeOBJ(name):
    vertices = []
    triangles = []

    with open(name, "r") as file:
        for line in file:
            if line.startswith("v "):
                _, x, y, z = line.strip().split()
                vertices.append([float(x), float(y), float(z)])
            elif line.startswith("f "):
                parts = line.strip().split()[1:]
                indices = [int(p.split("/")[0]) - 1 for p in parts]
                if len(indices) == 3:
                    triangles.append(indices)
                elif len(indices) > 3:
                    for i in range(1, len(indices) - 1):
                        triangles.append([indices[0], indices[i], indices[i+1]])
    return vertices, triangles

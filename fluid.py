import numpy as np
import cv2
import math
import random

# =============================
# SCREEN
# =============================
WIDTH, HEIGHT = 960, 720
CENTER = np.array([WIDTH // 2, HEIGHT // 2])

# =============================
# SETTINGS
# =============================
NUM_PARTICLES = 800
PARTICLE_DAMPING = 0.98

# =============================
# PARTICLE
# =============================
class Particle:
    def __init__(self, radius):
        a = random.uniform(0, 2 * math.pi)
        r = random.uniform(0, radius * 0.9)
        self.pos = CENTER + np.array([math.cos(a) * r, math.sin(a) * r])
        self.vel = np.zeros(2)

    def update(self):
        self.pos += self.vel
        self.vel *= PARTICLE_DAMPING

# =============================
# FLUID SYSTEM
# =============================
class Fluid:
    def __init__(self):
        self.radius = 260.0
        self.angle = 0.0
        self.particles = [Particle(self.radius) for _ in range(NUM_PARTICLES)]

    # -----------------------------
    # HEX GEOMETRY
    # -----------------------------
    def hex_planes(self):
        planes = []
        for i in range(6):
            a = self.angle + i * math.pi / 3
            normal = np.array([math.cos(a), math.sin(a)])
            planes.append((normal, self.radius))
        return planes

    def constrain_inside_hex(self, p):
        for normal, dist in self.hex_planes():
            rel = p.pos - CENTER
            d = np.dot(rel, normal)

            if d > dist:
                # push particle back inside
                correction = (d - dist) * normal
                p.pos -= correction

                # reflect velocity
                vn = np.dot(p.vel, normal)
                if vn > 0:
                    p.vel -= 1.8 * vn * normal

    # -----------------------------
    # UPDATE
    # -----------------------------
    def step(self, hand):
        # Update container from gesture
        if hand is not None:
            self.radius = np.clip(hand["pinch"] * 0.8, 180, 340)
            self.angle = hand["angle"]

        for p in self.particles:

            # -----------------------------
            # HAND FORCE
            # -----------------------------
            if hand is not None:
                r = p.pos - hand["pos"]
                d = np.linalg.norm(r)

                if 0 < d < 150:
                    push = r / d
                    swirl = np.array([-push[1], push[0]])

                    p.vel += push * 1.6
                    p.vel += swirl * 2.2

            p.update()
            self.constrain_inside_hex(p)

    # -----------------------------
    # DRAW
    # -----------------------------
    def draw(self, frame):
        # Draw hexagon
        pts = []
        for i in range(6):
            a = self.angle + math.pi / 6 + i * math.pi / 3
            pts.append((
                int(CENTER[0] + math.cos(a) * self.radius),
                int(CENTER[1] + math.sin(a) * self.radius)
            ))
        cv2.polylines(frame, [np.array(pts)], True, (255, 160, 0), 3)

        # Draw particles
        for p in self.particles:
            pos = p.pos.astype(int)
            cv2.circle(frame, pos, 3, (0, 130, 255), -1)
            cv2.circle(frame, pos, 1, (255, 220, 180), -1)

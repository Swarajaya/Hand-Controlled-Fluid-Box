import numpy as np
import random
import cv2

WIDTH = 960
HEIGHT = 720
RADIUS = 2

class Particle:
    def __init__(self):
        self.pos = np.array([
            random.uniform(200, WIDTH - 200),
            random.uniform(200, HEIGHT - 200)
        ], dtype=float)
        self.vel = np.zeros(2)

    def apply_force(self, point, radius=80):
        dist = np.linalg.norm(self.pos - point)
        if dist < radius:
            direction = self.pos - point
            if dist != 0:
                direction /= dist
            strength = (radius - dist) * 0.08
            self.vel += direction * strength

    def update(self):
        self.pos += self.vel
        self.vel *= 0.98

        if self.pos[0] <= 0 or self.pos[0] >= WIDTH:
            self.vel[0] *= -0.5
        if self.pos[1] <= 0 or self.pos[1] >= HEIGHT:
            self.vel[1] *= -0.5

        self.pos[0] = np.clip(self.pos[0], 0, WIDTH)
        self.pos[1] = np.clip(self.pos[1], 0, HEIGHT)

    def draw(self, frame):
        cv2.circle(frame, self.pos.astype(int), RADIUS, (0, 165, 255), -1)

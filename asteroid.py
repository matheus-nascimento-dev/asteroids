from circleshape import *
import random
from constants import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = (255,255,255)
        pygame.draw.circle(screen, color, self.position, self.radius, 2)

    def update(self, dt):
        self.position +=  self.velocity * dt

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        diff = random.uniform(20,50)
        d1 = self.velocity.rotate(diff)
        d2 = self.velocity.rotate(-diff)
        new_radius = self.radius  - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = d1
        asteroid2.velocity = d2
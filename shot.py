from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y,velocity,radius=SHOT_RADIUS):
        super().__init__(x, y, radius)
        self.velocity = velocity
        #print("shot")

    def draw(self, screen):
        color = (255,255,255)
        pygame.draw.circle(screen, color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        


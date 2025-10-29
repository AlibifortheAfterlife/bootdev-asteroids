import pygame

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: int):
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, (200, 200, 200), self.position, self.radius, 2)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

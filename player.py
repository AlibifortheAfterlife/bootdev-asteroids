from constants import PLAYER_RADIUS, PLAYER_ROTATION_SPEED, PLAYER_THRUST
from circleshape import CircleShape
import pygame


class Player(CircleShape):
    def __init__(self, x: float, y: float, color: tuple[int, int, int]):
        super().__init__(x, y, PLAYER_RADIUS, color)
        self.rotation: float = 0.0  # in degrees

    def triangle(self):
        forward: pygame.Vector2 = pygame.Vector2(0, 1).rotate(self.rotation)
        right: pygame.Vector2 = (
            pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        )
        a: pygame.Vector2 = self.position + forward * self.radius
        b: pygame.Vector2 = self.position - forward * self.radius - right
        c: pygame.Vector2 = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def move(self, dt: float):
        forward: pygame.Vector2 = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_THRUST * dt

    def rotate(self, dt: float):
        self.rotation += PLAYER_ROTATION_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

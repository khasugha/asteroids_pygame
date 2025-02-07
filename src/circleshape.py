import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collision(self, other) :
        if (isinstance(other, CircleShape)) :
            distance = self.position.distance_to(other.position)
            radius_sum = self.radius + other.radius
            if (distance > radius_sum) :
                return False
            else :
                return True
        else :
            raise TypeError("Can only check for collission between 2 circleshapes")

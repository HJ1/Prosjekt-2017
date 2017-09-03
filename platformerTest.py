import pygame

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
# Screen dimensions
WIDTH = 800
HEIGHT = 600

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("World")
clock = pygame.time.Clock()

class Player:

    def __init__(self, color):
        self.x = 50
        self.y = 500
        self.size = 30
        self.color = color

        # Speed vector
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.gravity()
        # Move left/right
        self.x += self.change_x

        # Move up/down
        self.y += self.change_y

    def gravity(self):
        # Calculate effect of gravity
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 1

        if self.y >= platform.size - self.size and self.change_y >= 0:
            self.change_y = 0
            self.y = HEIGHT - self.size
    # Player movement
    def jump(self):
        self.y += 2
        self.y -= 2

    def go_left(self):
        self.change_x = -6

    def go_right(self):
        self.change_x = 6

    def stop(self):
        self.change_x = 0

class Platform:
    def __init__(self, color):
        self.x = 0
        self.y = 600
        self.targetX = 800
        self.size = 20
        self.color = color


def draw_environment(player, platform):
    game_display.fill(WHITE)
    pygame.draw.circle(game_display, player.color, [player.x, player.y], player.size)
    pygame.draw.line(game_display, platform.color, (platform.x, platform.y), (platform.targetX, platform.y) , platform.size)
    player.update()
    pygame.display.update()

def main():
    floor = Platform(BLACK)
    player = Player(RED)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        draw_environment(player, floor)
        clock.tick(60)
if __name__ == '__main__':
    main()

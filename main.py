import pygame
import sys

pygame.init()
# X 750 Y 560
DISPLAY = pygame.display.set_mode((750, 560))
pygame.display.set_caption("Game")
font = pygame.font.Font("assets\Montserrat-Bold.ttf", 10)
fps = pygame.time.Clock()

def fps_counter() -> int:
    frames = int(fps.get_fps())
    text = font.render(f"FPS: {frames}", True, (255, 255, 255))
    DISPLAY.blit(text.convert_alpha(), (2, 0))
    return frames

while True:
    DISPLAY.fill((0, 0, 0))
    fps_counter()
    key_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fps.tick(125)

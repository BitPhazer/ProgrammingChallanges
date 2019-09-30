import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
snake_Width = 15
snake_Height = 15
Body_margin = 3
 
x_change = snake_Width + Body_margin
y_change = 0
 
 
class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """
    def __init__(self, x, y):
        super().__init__()
 
        self.image = pygame.Surface([snake_Width, snake_Height])
        self.image.fill(WHITE)
 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
pygame.init()
 
screen = pygame.display.set_mode([800, 600])
 
pygame.display.set_caption('Hello Mine Turtle!')
 
allspriteslist = pygame.sprite.Group()
 
snake_segments = []
for i in range(15):
    x = 250 - (snake_Width + Body_margin) * i
    y = 30
    segment = Segment(x, y)
    snake_segments.append(segment)
    allspriteslist.add(segment)
 
 
clock = pygame.time.Clock()
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (snake_Width + Body_margin) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (snake_Width + Body_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (snake_Height + Body_margin) * -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (snake_Height + Body_margin)
 
    old_segment = snake_segments.pop()
    allspriteslist.remove(old_segment)
 
    x = snake_segments[0].rect.x + x_change
    y = snake_segments[0].rect.y + y_change
    segment = Segment(x, y)
 
    snake_segments.insert(0, segment)
    allspriteslist.add(segment)
 
    screen.fill(BLACK)
 
    allspriteslist.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(5)
 
pygame.quit()
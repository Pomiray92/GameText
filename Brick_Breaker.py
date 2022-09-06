import pygame

WIDTH, HEIGHT  = 800, 600

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

FPS = 60
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15

class Paddle:
    VEL = 50
    
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

def draw(win, paddle):
    win.fill("white")
    paddle.draw(win)
    pygame.display.update()

   
def main():
    clock = pygame.time.Clock()
    
    Paddle = Paddle(WIDTH/2 - PADDLE_WIDTH/2, HEIGHT - PADDLE_HEIGHT - 5, PADDLE_WIDTH, PADDLE_HEIGHT, "black")
     
    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        draw(win, Paddle)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()  
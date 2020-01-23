import pygame


class Dot:
    def __init__(self, x, y, img):
        self.x, self.y = x, y
        self.sprite = makeSprite(img)
        moveSprite(self.sprite, self.x, self.y)


pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Game")


def keyPressed(keyCheck=""):
    global keydict
    pygame.event.clear()
    keys = pygame.key.get_pressed()
    if sum(keys) > 0:
        if keyCheck == "" or keys[keydict[keyCheck.lower()]]:
            return True
        return False


run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

keys = pygame.key.get_pressed()

win.fill((0, 0, 0))
pygame.draw.rect(win, (0, 0, 255), (10, 10, 100, 100))
pygame.display.update()

pygame.quit()

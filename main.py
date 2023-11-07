from pygame import *
import sys, menu

funcionamento=menu.menu_full

screen = display.set_mode((320,352))
timer = time.Clock()

while True:
    timer.tick(16)
    for i in event.get():
        if i.type == QUIT: sys.exit()
    pressedKeys=key.get_pressed()
    # 'funcionamento' deve ser redefinida mediante input do usuário
    funcionamento(pressedKeys, screen)
    display.flip()
    screen.fill((0,0,0))

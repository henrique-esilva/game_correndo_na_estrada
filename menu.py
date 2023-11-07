from pygame import K_UP, K_DOWN as K_DN, K_RETURN, K_ESCAPE as K_ESC
from functools import partial
from time import sleep
import pygame

pygame.font.init()
arial = pygame.font.Font(size=18)

def void():
    pass

menu_instancia = {
    'selected': 0,
    'stage': 0,
    'option_tree': [
        [('-=PRESS ENTER=-', void,)],
        [('um jogador', void), ('dois jogadores', void)],
        [('iniciar', void)],
        ]
    }

def menu_back(teclas_pressionadas):
    '''funcionamento padrão do menu principal
    apresenta opções de jogo. Deve ser exibido
    ao iniciar o programa'''
    if teclas_pressionadas[K_UP]: menu_instancia['selected']-=1*int(menu_instancia['selected']>0); print('up')
    if teclas_pressionadas[K_DN]: menu_instancia['selected']+=1*int(menu_instancia['selected']<len(menu_instancia['option_tree'][menu_instancia['stage']])-1); print('down')
    if teclas_pressionadas[K_RETURN]:
        menu_instancia['option_tree'][menu_instancia['stage']][menu_instancia['selected']][1]()
        menu_instancia['stage']+=1
        menu_instancia['selected']=0
        sleep(0.15)
    elif teclas_pressionadas[K_ESC]:
        menu_instancia['stage']-=1*int(menu_instancia['stage']>0)
        menu_instancia['selected']=0
        sleep(0.15)


def menu_front(screen):
    a=pygame.surface.Surface(screen.get_size())
    pygame.draw.circle(a, (255,255,255), (5, menu_instancia['selected']*16+5), 4, 0)
    y=0
    for i in menu_instancia['option_tree'][menu_instancia['stage']]:
        renderedText=arial.render(
            i[0].upper(),
            False,
            (255,255,255),
        )
        a.blit(renderedText, dest=(16, y*16))
        y+=1
    screen.blit(a, (0,0))


def menu_full(teclas_pressionadas, screen):
    menu_back(teclas_pressionadas)
    menu_front(screen)

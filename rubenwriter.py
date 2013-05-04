import pygame
import pygame.locals
import random


X,Y = 512,384
LEN = 20
FONT_SIZE = 40
RANDOM_FONT = False
RANDOM_COLOR = True

def make_label(text, cx, cy):
    rect = text.get_rect()
    rect.centerx = cx
    rect.centery = cy
    return (text, rect)

def render(render, font, *args):
    return getattr(font, render)(*args)


pygame.display.init()
screen = pygame.display.set_mode((X,Y), (pygame.locals.NOFRAME | pygame.locals.FULLSCREEN))
colors = {
          'red': (255,32,32),
          'blue': (32,32,255),
          'green': (32,255,32),
          'yellow': (255,255,32),
          'white': (255,255,255),
          'grey': (128,128,128),
          }
all_colors = colors.keys()

pygame.font.init()
all_fonts = pygame.font.get_fonts()
fonts = {}
for font in all_fonts:
    path = pygame.font.match_font(font)
    if path:
        fonts[font] = pygame.font.Font(path, FONT_SIZE)

default_font = pygame.font.get_default_font()
default_font = (f for f in all_fonts if default_font.startswith(f)).next()

if RANDOM_FONT: next_font = lambda: random.choice(all_fonts)
else: next_font = lambda: default_font

if RANDOM_COLOR: next_color = lambda: random.choice(all_colors)
else: next_color = lambda: 'white'

quit = False
text = "RubenWriter"
font = next_font()
color = next_color()

while not quit:
    screen.fill((0,0,0))

    # draw screen
    rendered = fonts[font].render(text + '_', True, colors[color])
    screen.blit(*make_label(rendered,X/2,Y/2))

    rendered = fonts[font].render('CTRL+SHIFT+ESC to exit', True, colors[color])
    screen.blit(*make_label(rendered,X/2,Y-FONT_SIZE))
    
    pygame.display.flip()
    
    # get keyboard input
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and shift and ctrl:
                quit = True
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                try: char = event.unicode
                except: char = ''
                
                shift = event.mod&pygame.KMOD_SHIFT
                ctrl = event.mod&pygame.KMOD_CTRL
                
                if char:
                    text = text[-(LEN-1):] + char
                    font = next_font()
                    color = next_color()
            


# This file was created by Carlos Gomez
# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame video series
# Video link: https://youtu.be/OmlQ0XCvIn0
# My friend Max helped me with this code
                            
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from settings import *
from sprites import *
import math

vec = pg.math.Vector2 

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')


#This class is dedicated to the mobs or obstacles
class Obstacle(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pg.Surface((5 , 10))
        self.image = pg.image.load(os.path.join(img_folder, 'JUG.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = HEIGHT - self.rect.height
        self.speed = -5

    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0:
            self.rect.x = WIDTH
            self.game.score += 1

''' Im not sure why the code is being underlined it doesnt work without the Bell there 
and there are other instances where Bell is used just fine
'''  

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Bell Jump")
        self.clock = pg.time.Clock()
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.obstacles = pg.sprite.Group()
        self.Bell = Bell(self)
        self.all_sprites.add(self.Bell)    
        self.all_sprites.add(self.obstacles)
        self.score = 0
# this code gives you the actual score number
    def new(self):
        self.score = 0
        self.run()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

        # Spawn new obstacles at random intervals
        if random.randrange(100) < 0.8  :
            obstacle = Obstacle(self)
            self.obstacles.add(obstacle)
            self.all_sprites.add(obstacle)

        # Checks for collisions with obstacles, if collision does happen you instantly die- 
        # still need to figure out how to make it kill you and restart it just closes the tab.
        hits = pg.sprite.spritecollide(self.Bell, self.obstacles, False)
        if hits:
            self.running = False

    # This fills the screen and also displays 'Score' 
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.draw_text(f"Score: {self.score}", 22, WHITE, WIDTH / 2, 20)
        pg.display.flip()

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)



game = Game()
game.new()
pg.quit()






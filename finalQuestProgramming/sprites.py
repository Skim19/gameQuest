
# Sprite classes for platform game
# © 2019 KidsCanCode LLC / All rights reserved.
# mr cozort planted a landmine by importing Sprite directly...
import pygame as pg
from pygame.sprite import Sprite
from settings import *
import random
from random import randint
vec = pg.math.Vector2

class Player(Sprite):
    # include game parameter to pass game class as argument in main...
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(LIGHTYELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0) 
        self.hitpoints = 100
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        ghits = pg.sprite.spritecollide(self, self.game.static_platforms, False)
        self.rect.x -= 1
        if hits or ghits: 
            self.vel.y = -15
    def update(self):
        self.acc = vec(0, 0.5)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_d]:
            self.acc.x = PLAYER_ACC
            # self.acc.y = -PLAYER_ACC
        if keys[pg.K_s]:
            self.acc.y = PLAYER_ACC
        if keys[pg.K_w]:
            self.jump()

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # self.acc.y += self.vel.y * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y < 0:
            self.pos.y = HEIGHT
        if self.pos.y > HEIGHT:
            self.pos.y = 0

        self.rect.midbottom = self.pos

class Player2(Sprite):
    # include game parameter to pass game class as argument in main...
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH -10, HEIGHT / 2)
        self.pos = vec(WIDTH -350, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.hitpoints = 100
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        ghits = pg.sprite.spritecollide(self, self.game.static_platforms, False)
        self.rect.x -= 1
        if hits or ghits: 
            self.vel.y = -15
    def update(self):
        self.acc = vec(0, 0.5)
        keys = pg.key.get_pressed()
        if keys[pg.K_j]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_l]:
            self.acc.x = PLAYER_ACC
            # self.acc.y = -PLAYER_ACC
        if keys[pg.K_k]:
            self.acc.y = PLAYER_ACC
        if keys[pg.K_i]:
            self.jump()

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # self.acc.y += self.vel.y * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.y < 0:
            self.pos.y = 0
        if self.pos.y > HEIGHT:
            self.pos.y = HEIGHT

        self.rect.midbottom = self.pos

class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.w = w
        self.h = h
    def blitme(self, x, y):
        self.screen.blit(self.image, (x, y))
    def update(self):
        self.acc = vec(0, 0)
        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # self.acc.y += self.vel.y * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

class Ground(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.w = w
        self.h = h
    def blitme(self, x, y):
        self.screen.blit(self.image, (x, y))
    def update(self):
        pass
        # self.acc = vec(0, 0)
        # # apply friction
        # self.acc.x += self.vel.x * PLAYER_FRICTION
        # # self.acc.y += self.vel.y * PLAYER_FRICTION
        # # equations of motion
        # self.vel += self.acc
        # self.pos += self.vel + 0.5 * self.acc
        # self.rect.x = self.pos

class Post(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = -1
    def blitme(self, x, y):
        self.screen.blit(self.image, (x, y))
    def update(self):
        self.rect.x += self.vx
        if self.rect.x < 0:
            # self.kill()
            self.rect.x = WIDTH
            self.rect.height = random.randint(10,35)
# created a healthbar and tied it to players hitpoints
# I added it to the main.py under new, and it won't change its width
# I think I need to add a blit to update the graphic
import time
import sys
import pygame
from pygame.locals import *
from random import randint

pygame.init()
window = pygame.display.set_mode((648,604), RESIZABLE)


def initialisation(): #choice beetween play or help
  window = pygame.display.set_mode((648,604), RESIZABLE)
  window.blit(pygame.image.load("start.png").convert(), (0, 0))
  pygame.display.flip()
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          if 489 > event.pos[1]:
            mastermind()
          if 488 < event.pos[1]:
            help()
      if event.type == KEYDOWN:
        mastermind()

def help(): #display help
  window.blit(pygame.image.load("help.png").convert(), (0, 0))
  pygame.display.flip()
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == KEYDOWN:
        initialisation()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          initialisation()

def menu(): #choice beetween replay or go start
  time.sleep(1.5)
  window.blit(pygame.image.load("menu.png").convert(), (230, 200))
  pygame.display.flip()
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          if 200 < event.pos[1] < 239:
            if 230 < event.pos[0] < 364:
              initialisation()
            if 364 < event.pos[0] < 498:
              mastermind()
      if event.type == KEYDOWN:
        if event.key == K_KP0:
          initialisation()
        if event.key == K_KP1:
          mastermind()

def mastermind():
  window = pygame.display.set_mode((648, 604), RESIZABLE)
  window.blit(pygame.image.load("player.png").convert(), (0, 0))
  pygame.display.flip()
  code = 0
  code = player(12)
  window = pygame.display.set_mode((295,650), RESIZABLE)
  window.blit(pygame.image.load("plateau2.png").convert(), (0,0))
  pygame.display.flip()
  background=[0, 0, 0, 0]
  l=0
  while True:
    c=0
    val = pygame.image.load("val.png").convert()
    window.blit(val, (255,610))
    pygame.display.flip()
    fin=True
    background = codex(l, background)
    for k in background:
      if k == 0:
        c=1
    if c == 0:
      verif(background,code,l)
      l+=1
      background=[0,0,0,0]
      if l < 12:
        val = pygame.image.load("val.png").convert()
        window.blit(val, (255,610-l*50))
        pygame.display.flip()
    if l>11:
      code[0]=code[0]-1
      code[1]=code[1]-1
      code[2]=code[2]-1
      code[3]=code[3]-1
      couleur(code,12,0)
      couleur(code,12,1)
      couleur(code,12,2)
      couleur(code,12,3)
      perdu = pygame.image.load("perdu.png").convert()
      window.blit(perdu, (89,300))
      pygame.display.flip()
      time.sleep(1.5)
      menu = pygame.image.load("menu.png").convert()
      window.blit(menu, (13,200))
      pygame.display.flip()
      while True:
        for event in pygame.event.get():
          if event.type == KEYDOWN:
            if event.key == K_KP0:
              initialisation()
            if event.key == K_KP1:
              mastermind()

def player(l):
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          if event.pos[1] < 303:
            return [randint(1, 8), randint(1, 8), randint(1, 8), randint(1, 8)]
          if event.pos[1] > 303:
            return codex(l, 0)

def codex(l, background):
  if l == 12:
    background = [0, 0, 0, 0]
    window = pygame.display.set_mode((295, 650), RESIZABLE)
    window.blit(pygame.image.load("plateau2.png").convert(), (0, 0))
    window.blit(pygame.image.load("val.png").convert(), (255, 10))
    pygame.display.flip()
  fin=True
  while fin or background[0] == 0 or background[1] == 0 or background[2] == 0 or background[3] == 0:
    fin=True
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          if 610-l*50 < event.pos[1] < 610-l*50+30: #boutton valider
            if 255 < event.pos[0] < 285:
              fin=False
          if 610-l*50 < event.pos[1] < 610-l*50+30:
            if 205 < event.pos[0] < 235:
              background=couleur(background,l,3)
          if 610-l*50 < event.pos[1] < 610-l*50+30:
            if 155 < event.pos[0] < 185:
              background=couleur(background,l,2)
          if 610-l*50 < event.pos[1] < 610-l*50+30:
            if 105 < event.pos[0] < 135:
              background=couleur(background,l,1)
          if 610-l*50 < event.pos[1] < 610-l*50+30:
            if 55 < event.pos[0] < 85:
              background=couleur(background,l,0)
      if event.type == KEYDOWN:
        if event.key == K_RETURN:
          fin = False
        if event.key == K_KP1:
          background=couleur(background,l,0)
        if event.key == K_KP2:
          background=couleur(background,l,1)
        if event.key == K_KP3:
          background=couleur(background,l,2)
        if event.key == K_KP4:
          background=couleur(background,l,3)
  if l==12:
    l=0
  return background


def verif(ba,c,l):
  r=0
  bl=0
  vb=[0,0,0,0]
  vc=[0,0,0,0]
  for k in range(4):
    if ba[k] == c[k]:
      vb[k]=2
      vc[k]=2
      r+=1
  if r == 4:
    c[0]=c[0]-1
    c[1]=c[1]-1
    c[2]=c[2]-1
    c[3]=c[3]-1
    couleur(c,12,0)
    couleur(c,12,1)
    couleur(c,12,2)
    couleur(c,12,3)
    gagne = pygame.image.load("gagne.png").convert()
    window.blit(gagne, (89,300))
    pygame.display.flip()
    time.sleep(1.5)
    menu = pygame.image.load("menu.png").convert()
    window.blit(menu, (13,200))
    pygame.display.flip()
    while True:
      for event in pygame.event.get():
        if event.type == KEYDOWN:
          if event.key == K_KP0:
            initialisation()
          if event.key == K_KP1:
            mastermind()
  for j in range(4):
    if vb[j] == 0:
      for h in range(4):
        if vc[h] == 0:
          if vb[j] == 0:
            if ba[j] == c[h]:
              vb[j]=1
              vc[h]=1
              bl+=1
  if r+bl > 0:
    if r > 0:
      r-=1
      prg = pygame.image.load("prg.png").convert()
      window.blit(prg, (10,630-l*50))
    else:
      bl-=1
      pba = pygame.image.load("pba.png").convert()
      window.blit(pba, (10,630-l*50))
  if r+bl > 0:
    if r > 0:
      r-=1
      prg = pygame.image.load("prg.png").convert()
      window.blit(prg, (25,630-l*50))
    else:
      bl-=1
      pba = pygame.image.load("pba.png").convert()
      window.blit(pba, (25,630-l*50))
  if r+bl > 0:
    if r > 0:
      r-=1
      prg = pygame.image.load("prg.png").convert()
      window.blit(prg, (10,615-l*50))
    else:
      bl-=1
      pba = pygame.image.load("pba.png").convert()
      window.blit(pba, (10,615-l*50))
  if r+bl > 0:
    if r > 0:
      r-=1
      prg = pygame.image.load("prg.png").convert()
      window.blit(prg, (25,615-l*50))
    else:
      bl-=1
      pba = pygame.image.load("pba.png").convert()
      window.blit(pba, (25,615-l*50))
  pygame.display.flip()

def couleur(b,l,o):
  b[o]=(b[o]+1)%9
  if b[o] == 0:
    gr = pygame.image.load("gr.png").convert()
    window.blit(gr, (55+o*50,610-l*50))
    pygame.display.flip()
  if b[o] == 1:
    pm = pygame.image.load("pm.png").convert()
    window.blit(pm, (55+o*50,610-l*50))
    pygame.display.flip()
  if b[o] == 2:
    pj = pygame.image.load("pj.png").convert()
    window.blit(pj, (55+o*50,610-l*50))
    pygame.display.flip()
  if b[o] == 3:
    pve = pygame.image.load("pve.png").convert()
    window.blit(pve, (55+o*50,610-l*50))
    pygame.display.flip()
  if b[o] == 4:
    pbe = pygame.image.load("pbe.png").convert()
    window.blit(pbe, (55+o*50,610-l*50))
    pygame.display.flip()
  if b[o] == 5:
    po = pygame.image.load("po.png").convert()
    window.blit(po, (55+o*50,610-l*50))
    pygame.display.flip()
  if b[o] == 6:
    pg = pygame.image.load("pg.png").convert()
    window.blit(pg, (55+o*50,610-l*50))
    pygame.display.flip()
  if b[o] == 7:
    pvi = pygame.image.load("pvi.png").convert()
    window.blit(pvi, (55+o*50,610-l*50))
    pygame.display.flip()
  if b[o] == 8:
    prs = pygame.image.load("prs.png").convert()
    window.blit(prs, (55+o*50,610-l*50))
    pygame.display.flip()
  return b

# A laisser a la fin
initialisation()


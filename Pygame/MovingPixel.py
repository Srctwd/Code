import sys, pygame
import numpy as np
pygame.init()
displayW=800
displayH=600
Display = pygame.display.set_mode((800,600))
Display.fill((111,175,107))
#pygame.draw.rect(Display, (255,255,255), (100,100,6,6))
#pygame.draw.rect(Display, (255,0,0), (110,100,1,1))
pygame.display.update()
#COLORS
WHITE = (255,255,255)
RED = (255,0,0)
Grass = (111,175,107)
worldSize= 1000
slotSize= 6
class Pixel():
    def __init__(self, pilha=[]):
        self.pilha = pilha
                
    def getPixelList(self):
        npPixelList = [Pixel() for i in range(slotSize)]
        return npPixelList
       
       
class Slot(Pixel):
    def __init__(self, matrixPos=[0,0]):
        Pixel.__init__(self)
        self.matrixPos = matrixPos
        self.npPixelList = self.getPixelList()
        self.slot = np.array([self.npPixelList]*slotSize)
        
    
    def getSlotList(self):
        npSlotList = [Slot() for i in range(worldSize)]
        return npSlotList


class Matrix(Slot):
    def __init__(self):
        Slot.__init__(self)
        self.npSlotList = self.getSlotList()
        self.world = np.array([self.npSlotList]*worldSize)

       
class Unit:
    #Slot needs to be existent
    def __init__(self, slot, name="0", color=WHITE, size=(6,6)):
        self.name = name
        self.slot = slot
        self.size_x = size[0]
        self.size_y = size[1]
        self.color = color
        self.pos = self.slot.matrixPos
        
    def draw(self):
        pygame.draw.rect(Display, self.color, (self.pos[0],self.pos[1],self.size_x,self.size_y))
        
        
class Player(Unit):
    def __init__(self, unit):
        Unit.__init__(self, unit.slot)
        self.name = unit.name
        self.pos = unit.pos
        self.slot = unit.slot
        self.size_x = unit.size_x
        self.color = unit.color
        self.movementcooldown = 10
            
    def movement(self):
        events = pygame.event.get()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            player.pos[1]-=1
        if pressed[pygame.K_a]:
            player.pos[0]-=1
        if pressed[pygame.K_s]:
            player.pos[1]+=1
        if pressed[pygame.K_d]:
            player.pos[0]+=1
            
a=Matrix()
unit=Unit(a.world[0][0])
player=Player(unit)

while True:
    Display.fill((111,175,107))
    player.draw()
    player.movement()
    pygame.display.update()
    

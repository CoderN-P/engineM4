from __future__ import annotations
# This library is meant to be gray box. It is good to simply show the students what classes exist in the library, though I wouldn't get into the minutiae of HOW the objects perform their duties.
# A common mistake is that students don't have this file in the same folder as their game file

from sys import exit

import os # used for making folders

from copy import deepcopy

# double clicking on this file can be used to set up a new game folder
if __name__ == "__main__":

    from shutil import copy

    path = os.getcwd() # get current working directory

    newFolderName = input("Enter the name of your new game: ")
    newFolderName = "/"+newFolderName

    try:  
        os.mkdir(path+newFolderName)
    except OSError:  
        print ("Creation of the directory %s failed" % path+newFolderName)
    else:  
        print ("Successfully created the directory %s " % path+newFolderName)

    baseFileName = os.path.basename(__file__)
    copy(__file__, path+newFolderName+"/"+baseFileName)
    gameFile = open(path+newFolderName+"/"+newFolderName+".py", "x")
    engineNameNoExtension = baseFileName.removesuffix(".py")
    startingCode = f'''import {engineNameNoExtension} as e, math, random

gameState = "begin"

def beginState():
    pass

def playState():
    pass

def gameOverState():
    pass

while True:

    if gameState == "begin":
        beginState()

    if gameState == "play":
        playState()

    if gameState == "game over":
        gameOverState()

    e.runGame((0,0,0))'''
    
    gameFile.write(startingCode)
    gameFile.close()


#bring in the pygame module
import pygame
import math

#initiate the pygame module, this line must come before any othe pygame-dependent code
pygame.init()

# I have made a class called sprite (see below) which is used to visually represent objects.
# A sprite is useful for making characters, walls, floors, power-ups, bad guys, or anything else you might want to be seen on the videogame screen.

# This list is used to store all of the sprites in the game. In the main while loop of the game this list is iterated through to make every sprite run its update function.
spriteList = []
shapeList = []


textList = []

# These are some color vectors for quick reference.
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
red = (255, 0, 0)
orange = (255, 140, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (128, 0, 128)
violet = (238, 130, 238)

# width and height of the game window.
screenW = 800
screenH = 600

# Set up the game window.
# if running from repl use fullscreen (this is much better for repl)
if os.path.isdir("/home/runner") == True:
    gameDisplay = pygame.display.set_mode((screenW,screenH),pygame.FULLSCREEN, 32)
else:
    gameDisplay = pygame.display.set_mode((screenW,screenH))

# Set the text in the window bar.
pygame.display.set_caption('Game')

clock = pygame.time.Clock()

def playSong(givenFileName, givenTimes) -> None:
    # a parameter of -1 will make the song play on loop infinitely
    pygame.mixer.music.load(givenFileName)
    pygame.mixer.music.play(int(givenTimes))

def stopSong() -> None:
    pygame.mixer.music.stop()

def directionToPoint(primaryX, primaryY, targX, targY) -> float:
    rel_y = targY - primaryY
    rel_x = targX - primaryX
    return math.degrees(-math.atan2(rel_y, rel_x))

# Note : the parameter   self   is included as the first parameter for every object's functions. This parameter does not need to be specified.

# keyboard manager
class kbController():
    def __init__(self):
        # keys is a list of buttons that are currently held down. This list is indexed by pygame's constant values for each key.
        # E.g.   keysPressed[K_RIGHT] == True    indicates that the right key is currently held down.
        # The list of constants that represent each key can be found at https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed

        # record the keys that were down last frame
        self.previousKeysPressed = []
        self.keysPressed = pygame.key.get_pressed()

    def update(self) -> None:
        self.previousKeysPressed = self.keysPressed
        self.keysPressed = pygame.key.get_pressed()

    def singlePress(self, givenKey) -> bool:
        return self.keysPressed[givenKey] and not self.previousKeysPressed[givenKey]

    def held(self, givenKey) -> bool:
        return self.keysPressed[givenKey]
    
# A global instance so students don't have to instiate their own keyboard manager
kb = kbController()
            
class mouseController():
    def __init__(self):
        self.previouseMousePressed = []
        self.mousePressed = pygame.mouse.get_pressed()
        self.update()

    def update(self) -> None:
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]
        self.previouseMousePressed = self.mousePressed
        self.mousePressed = pygame.mouse.get_pressed()

    def mouseHover(self, givenSprite) -> bool:
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        if givenSprite.leftEdge < mouseX < givenSprite.rightEdge:
            if givenSprite.topEdge < mouseY < givenSprite.bottomEdge:
                return True

    # parameters leftclick -> 0, middleclick -> 1, or rightclick -> 2
    def globalClick(self, givenButton) -> bool:
        return self.mousePressed[givenButton] and not self.previouseMousePressed[givenButton]

    def spriteClick(self, givenSprite, givenButton) -> bool:
        return self.mouseHover(givenSprite) and self.globalClick(givenButton)
                
# A global instance so students don't have to instiate their own mouse Controller
mc = mouseController()


# A graphic game object.
class sprite():
    # sprites are constructed with a starting x and y coordinate and a string that specifies an image file such as "mario.png" .
    # The image file specified must be in the same folder as this code file.
    def __init__(self, givenX, givenY, givenImage):
        self.xStart = givenX
        self.yStart = givenY
        self.x = givenX
        self.y = givenY
        self.hspeed = 0
        self.vspeed = 0
        self.rotation = 0
        self.scale = 1
        self.visible = True
        self.baseImage = pygame.image.load(givenImage)
        # rotozoom parameters: image, degrees of rotation, scale factor
        self.rotatedImage = pygame.transform.rotozoom(self.baseImage, self.rotation, self.scale)
        self.width = self.rotatedImage.get_rect().size[0] # The width of the provided image.
        self.height = self.rotatedImage.get_rect().size[1] # The height of the provided image.
        self.alarm = []
        for i in range(0, 12):
            self.alarm.append(-1)

        # No matter how the image looks collisions are handled as a rectangle.
        # The following 4 variables are constantly updated in the runGame function so that they represent the current space that this object graphically occupies ( see   update(self) ).
        self.leftEdge = self.x
        self.rightEdge = self.x + self.width
        self.topEdge = self.y
        self.bottomEdge = self.y + self.height

        # When this object is instantiated, we also add it to the spriteList
        spriteList.append(self)


    # This function is called in runGame for every sprite in the spriteList
    def update(self) -> None:
        self.x += self.hspeed
        self.y += self.vspeed
        self.leftEdge = self.x
        self.rightEdge = self.x + self.width
        self.topEdge = self.y
        self.bottomEdge = self.y + self.height
        self.rotatedImage = pygame.transform.rotozoom(self.baseImage, self.rotation, self.scale)

        # The blit function tells the game window to render a graphic at a an (x, y) point
        if self.visible == True:
            gameDisplay.blit(self.rotatedImage,(self.x,self.y))
            
        for i in range(0, len(self.alarm)):
            if self.alarm[i] >= 0:
                self.alarm[i] -= 1

    # This function only takes one real parameter, another sprite. If this sprite ocupies any of the same space of the specified sprite, then it returns True.
    def collide(self, other) -> bool:
        if other is None:
            return False
        
        if not isinstance(other, rect):
            other = other.rotatedImage.get_rect(topleft=(other.x, other.y))

        this_rect = self.rotatedImage.get_rect(topleft=(self.x, self.y))
        
        if this_rect.colliderect(other_rect): 
            return True
        else:
            return False

    def moveForward(self, givenSpeed) -> None:
        self.x += math.cos(math.radians(self.rotation)) * givenSpeed;
        self.y -= math.sin(math.radians(self.rotation)) * givenSpeed;

    # This function removes this sprite from the spriteList and then destroys it
    def destroy(self) -> None:
        spriteList.remove(self)
        del(self)


    def clone(self):
        clone = deepcopy(self)
        spriteList.append(clone)
        return clone


# The following section can be ignored. It helps make text on the screen.
# This is from http://www.nerdparadise.com/programming/pygame/part5
############################################################
def make_font(fonts, size) -> pygame.font.Font | pygame.font.SysFont:
    available = pygame.font.get_fonts()
    # get_fonts() returns a list of lowercase spaceless font names 
    choices = map(lambda x:x.lower().replace(' ', ''), fonts)
    for choice in choices:
        if choice in available:
            return pygame.font.SysFont(choice, size)
    return pygame.font.Font(None, size)
    
_cached_fonts = {}
def get_font(font_preferences, size) -> pygame.font.Font | pygame.font.SysFont:
    global _cached_fonts
    key = str(font_preferences) + '|' + str(size)
    font = _cached_fonts.get(key, None)
    if font == None:
        font = make_font(font_preferences, size)
        _cached_fonts[key] = font
    return font

_cached_text = {}
def create_text(text, fonts, size, color):
    global _cached_text
    key = '|'.join(map(str, (fonts, size, color, text)))
    image = _cached_text.get(key, None)
    if image == None:
        font = get_font(fonts, size)
        image = font.render(text, True, color)
        _cached_text[key] = image
    return image

font_preferences = [
        "Bizarre Font Sans Serif",
        "They definitely dont have this installed Gothic",
        "Papyrus",
        "Comic Sans MS"]

############################################################


# This is the function that students should use for making text on the screen.
class text():
    def __init__(self, givenString, givenSize, givenColor, givenX, givenY):
        self.textImg = create_text(givenString, font_preferences, givenSize, givenColor)
        self.textString = givenString
        self.size = givenSize
        self.color = givenColor
        self.x = givenX
        self.y = givenY
        self.visible = True
        textList.append(self)

    def update(self) -> None:
        if self.visible == True:
            gameDisplay.blit(self.textImg, (self.x, self.y))

    def changeText(self, givenString) -> None:
        self.textImg = create_text(givenString, font_preferences, self.size, self.color)

    def destroy(self) -> None:
        textList.remove(self)
        del(self)



class rect(pygame.Rect):
    def __init__(self, x, y, w, h, color=(0, 0, 0), filled=False):
        super().__init__((x, y), (w, h))
        
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.hspeed = 0
        self.vspeed = 0
        self.rotation = 0
        self.scale = 1
        self.filled = filled
        self.yStart = y
        self.xStart = x
        self.alarm = [-1]*12
            
        self.leftEdge = self.x
        self.rightEdge = self.x + self.width
        self.topEdge = self.y
        self.bottomEdge = self.y + self.height
        self.color = color
        self.visible = True
        shapeList.append(self)
 
    def update(self) -> None:
        if 0 < self.vspeed < 1:
            self.delay = 1 - self.vspeed
        self.move_ip(self.hspeed, self.vspeed)
        self.x += self.hspeed
        self.y += self.vspeed
        self.leftEdge = self.x
        self.rightEdge = self.x + self.width
        self.topEdge = self.y
        self.bottomEdge = self.y + self.height
        for x, i in enumerate(self.alarm):
            if i >= 0:
                self.alarm[x] -= 1
        if self.visible == True:
            pygame.draw.rect(gameDisplay, self.color, self)

    def destroy(self) -> None:
        shapeList.remove(self)
        del (self)

    def collide(self, otherRect) -> bool:
        if otherRect is None:
            return False

        if not isinstance(otherRect, rect):
            otherRect = otherRect.rotatedImage.get_rect(topleft=(otherRect.x, otherRect.y))
      
        return self.colliderect(otherRect)

    def copy(self):
        clone = deepcopy(self)
        shapeList.append(clone)
        return clone

    
# This function is responsible for rendering the game window and all visible objects.
# Students should call this function inside of a while loop so that the game window is constantly updated.
def runGame(backGroundColor) -> None :

    for iterEvent in pygame.event.get():

        # allows the exit button to properly close the game
        if iterEvent.type == pygame.QUIT:
            pygame.quit()
            exit()
            break
            return


    # Listen for the current status of the mouse
    mc.update()
    
    # Listen for the current status of the keys
    kb.update()
    
    # fill the background with a specified color vector
    gameDisplay.fill(backGroundColor)


    # Render every sprite.
    for iterSprite in spriteList:
            iterSprite.update()

    # Render every text
    for iterText in textList:
        iterText.update()

    # Render every shape
    for iterShape in shapeList:
        iterShape.update()
        

    pygame.display.update()
    clock.tick(60)


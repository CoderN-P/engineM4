# Functions
There are built in functions for controlling pygame and engineM4   

`playSong(givenFileName, givenTimes)` - Play a sound file. Repeat `givenTimes` times. Use a string for `givenFileName` and int for `givenTimes`

`stopSong()` - Stop playing a sound

`directionToPoint(primaryX, primaryY, targX, targY)` - Find the direction in degrees to the target X and Y from the primary (starting) X and Y

`runGame(backGroundColor)` - Updates the screen. Should be in a while loop. `backGroundColor` is an rgb tuple

*There are some more, but those are used inside engineM4 only*
# Variables
`pygame` - module -  Access the pygame module without having to import pygame again

`spriteList` - list - *read only* - A list of all the sprites loaded in engineM4

`shapeList` - list - *read only* - A list of all the shapes (rectangles) loaded in engineM4

`black, white, gray, red, orange, yellow, green, blue, indigo, violet` - tuples - *read only* - The variables are rgb tuples of their color

`screenW` - int - *read only* - The width of the screen

`screenH` - int - *read only* - The height of the screen

`gameDisplay` - pygame display object - The game display

`mc` - mouse controller object - The [mouse controller](/docs/mouseController.md).

`kb` - keyboard controller object - The [keyboard controller](/docs/keyboardController.md).
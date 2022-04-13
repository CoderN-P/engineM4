# Sprite Class
The object used for sprites (in-game objects)
## Usage
`sprite(givenX, givenY, givenImage)`  

`givenX` - float - X coordinate of the sprite   

`givenY` - float - Y coordinate of the sprite   

`givenImage` - string - Path to the image for the sprite   
  
You should put the new sprite into a variable to be able to use it later
### Example

```python
import engineM4 as e

sprite = e.sprite(e.screenW/2-16, e.screenH-64, 'sprite.png')
```
## Attributes 
`xStart` - float - *read only* - The starting x position of the sprite    

`yStart` - float - *read only* - The starting y position of the sprite    

`x` - float - *read and write* - The current x position of the sprite. Use = operator to set the x position of the sprite   

`y` - float - *read and write* - Same as 'x' except it is the current y position of the sprite   

`hspeed` - float - *read and write* - The horizontal (x) speed of the sprite. Starts with `0` 

`vspeed` - float - *read and write* - The vertical (y) speed of the sprite. Starts with `0`  

`rotation` - float - *read and write* - The amount of degrees to rotate the sprite. Only used to create a rectangular hitbox using `pygame.rotozoom`. Default - `0`     
`scale` - float - *read and write* - Scale of the sprite (size). Default - `1`  

`visible` - boolean - *read and write* - Determines if the sprite can be seen and interacted with. Default - `True`

`leftEdge` - float - *read only* - The left edge of the sprite (x coord)   

`rightEdge` - float - *read only* - The right edge of the sprite (x coord)   

`topEdge` - float - *read only* - The top edge of the sprite (y coord)   

`bottomEdge` - float - *read only* - The bottom edge of the sprite (y coord) 

`width` - float - *read only* - How wide the sprite is  

`height` - float - *read only* - How high the sprite is

### Alarms
Using `sprite.alarm`, you can alarms that tick every time the sprite is ticked. It can be used to time events (a timer, basically).  
The `sprite.alarm` object is a list, so to set an a alarm, you will need to do `sprite.alarm[0] = 10` where 10 is the number of **ticks** (not seconds) before the alarm will go off

### Functions
`collide(other)` - Returns a boolean for whether the sprite is touch another sprite (`other`)  

`moveForward(givenSpeed)` - Moves the sprite on both the x and y axis with `givenSpeed`.

`destroy()` - Removes the sprite

`clone()` - Clones the sprite. The output is the clone.
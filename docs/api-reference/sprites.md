---
description: The object used for sprites (in-game objects)
---

# Sprite Class

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

`xStart` - float - _read only_ - The starting x position of the sprite

`yStart` - float - _read only_ - The starting y position of the sprite

`x` - float - _read and write_ - The current x position of the sprite. Use = operator to set the x position of the sprite

`y` - float - _read and write_ - Same as 'x' except it is the current y position of the sprite

`hspeed` - float - _read and write_ - The horizontal (x) speed of the sprite. Starts with `0`

`vspeed` - float - _read and write_ - The vertical (y) speed of the sprite. Starts with `0`

`rotation` - float - _read and write_ - The amount of degrees to rotate the sprite. Only used to create a rectangular hitbox using `pygame.rotozoom`. Default - `0`\
`scale` - float - _read and write_ - Scale of the sprite (size). Default - `1`

`visible` - boolean - _read and write_ - Determines if the sprite can be seen and interacted with. Default - `True`

`leftEdge` - float - _read only_ - The left edge of the sprite (x coord)

`rightEdge` - float - _read only_ - The right edge of the sprite (x coord)

`topEdge` - float - _read only_ - The top edge of the sprite (y coord)

`bottomEdge` - float - _read only_ - The bottom edge of the sprite (y coord)

`width` - float - _read only_ - How wide the sprite is

`height` - float - _read only_ - How high the sprite is

### Alarms

Using `sprite.alarm`, you can alarms that tick every time the sprite is ticked. It can be used to time events (a timer, basically).\
The `sprite.alarm` object is a list, so to set an a alarm, you will need to do `sprite.alarm[0] = 10` where 10 is the number of **ticks** (not seconds) before the alarm will go off

### Functions

`collide(other)` - Returns a boolean for whether the sprite is touch another sprite (`other`)

`moveForward(givenSpeed)` - Moves the sprite on both the x and y axis with `givenSpeed`.

`destroy()` - Removes the sprite

`clone()` - Clones the sprite. The output is the clone.

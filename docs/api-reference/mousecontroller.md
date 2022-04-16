# Mouse Controller

The mouse controller (mc) is used to register mouse clicks. For the similar object called keyboard controller (kb), see [this page](keyboardcontroller.md).

## Functions

`mouseHover(givenSprite)` - Check if the mouse is hovering over the given sprite

`globalClick(givenButton)` - Check if the mouse click anywhere on the screen. For `givenButton`, use `0` for leftclick, `1` for middleclick, and `2` for rightclick

`spriteClick(givenSprite, givenButton)` - Check is the mouse clicked on the given sprite. Again, for `givenButton`, use `0` for leftclick, `1` for middleclick, and `2` for rightclick

### Example

The built in variable `mc` is used for the mouse controller.

```python
import engineM4 as e
sprite = sprite(e.screenW/2-16, e.screenH-64, "sprite.png") # Example sprite

while True:
    if e.mc.spriteClick(sprite, 0):
        ... # Do something here
    e.runGame((0,0,0))
```

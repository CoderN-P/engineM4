# Rect Class
Rect classes are largely similar to `sprite` classes, however they are a subclass of `pygame.Rect` and are used to create rectangles on the screen.

## Usage
`
rect(givenX, givenY, w, h, color)
` 

**NOTE** - `pygame.Rect` only accepts integer x positions, y positions, heights, and widths. Any float values will be rounded to the nearest integer.

`givenX` - Initial x coordinate of the rectangle

`givenY` - Initial y coordinate of the rectangle

`w` - Width of the rectangle (px)

`h` - Height of the rectangle (px)

`color` - The color of the rectangle (RGB Tuple)

### Example

```python
import engineM4 as e

pipe = e.rect(e.screenW/2-24, e.screenH/2-64, 24, 64, (0, 255, 0))
```

This creates a green pipe, `24` pixels wide and `64` pixels tall in the center of the screen.

## Attributes

### Read-Only attributes
`xStart` - *int* - The initial x position of the rectangle

`yStart` - *int* - The initial y position of the rectangle

`leftEdge` - *int* - The x coordinate of the left side of the rectangle

`rightEdge` - *int* - The x coordinate of the right side of the rectangle

`topEdge` - *int* - The y coordinate of the top side of the rectangle

`bottomEdge` - *int* - The y coordinate of the bottom side of the recangle


### Read and Write attributes

`hspeed` - *int* - The horizontal speed of the rectangle. This value is added to the rectangles x position on every frame. **Default** - `0`

`vspeed` - *int* - The vertical speed of the rectangle. This value is added to the rectangles y position on every frame. **Default** - `0`

`visible` - *bool* - A boolean that determines if the rectangle is rendered on the screen or not. **Default** - `True`

`width` - *int* - The width of the rectangle (Can be edited after initialization)

`height` - *int* - The height of the rectangle (Can be edited after initialization)

`color` - (*int<=255*, *int<=255*, *int<=255*) - The rectangle'c olor (Can be edited after initialization)

`rotation` - *int* - The amount of degrees to rotate the rectangle. **Default** - `0`

`scale` - *int* - The amount to scale the rectangle up/down. **Default** - `0`


### Alarms

The `rect.alarm` is a list of integers that can be used for ticking events. **Default** - `[-1]*12`

The values in the alarm list are automatically decremented every frame if they are greater than `0`

#### Example Usage
```python
import engineM4 as e

pipe = e.rect(e.screenW/2-24, e.screenH/2-64, 24, 64, (0, 255, 0)) # Creates a green rectangle in the middle of the screen - 24px x 64px
pipe.alarm[0] = 10*60 #We are multiplying by 60 to get 10 seconds since the game runs at 60 fps
pipeList = [pipe]

while True:
  if pipe.alarm[0] == 0:
    pipeList.append(pipe.clone())
    pipe.alarm[0] = 10*60
    
  e.runGame((0, 0, 0))
```

This code renders a pipe in the center of the screen. Every 10 seconds, the pipe will spawn a clone of itself


### Methods/Functions

1. `rect.collide(rect|sprite)` 
    - Parameters: A rect or sprite object
    - Checks if the rectangle is colliding with another rectangle or sprite

2. `rect.update()`
    - Parameters: None
    - This method is already called by the `e.runGame` function
    - It updates and re-renders the rectangle when called

3. `rect.destroy()`
    - Parameters: None
    - Deletes the rectangle

4. `rect.clone()`
    - Paramters: None
    - Clones the rectangle and returns the clone




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

`width` - *int* - The width of the rectangle

`height` - *int* - The height of the rectangle

### Read and Write attributes

**soon**



# engineM4
This is a simple Pygame API wrapper. It was originally created by my CS teacher, Max Mcintyre. However, I have added more code and decided to use github to version control it.

## Example Usage
```python
import engineM4 as e

while True:
  ... # Your game code here
  e.runGame((0, 0, 0) # Can be any tuple representing an RGB combination
  
 ```
 
 ## Built in objects/classes
 - Sprite - (Helps for dealing with sprites)
   - Example Usage
   - ```python
     character = e.sprite(x, y, "character.png")
     ```
 - Rect - (A subclass of the pygame.Rect object. Helps for dealing with rectangles)
   - Example Usage
   - ```python
     pipe = e.rect(x, y, w, h, color)
     ```
 - kb (Keyboard controller - for managing keyboard input)
 - mc (Mouse controller - for managing mouse input)
 - Text (For rendering and managing text on the screen)



 

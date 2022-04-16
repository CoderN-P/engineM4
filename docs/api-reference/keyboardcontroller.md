---
description: The keyboard controller (kb) is used to register key presses.
---

# Keyboard Controller

## Functions

`singlePress(givenKey)` - Check is the given key was pressed once

`held(givenKey)` - Check is the given key is being held

For `givenKey`, you will have to use the pygame constant for the key you want. See the example for more info

### Example

The built-in variable `kb` contains the KeyboardController class.

```python
import engineM4 as e

while True:
    if e.kb.held(e.pygame.K_RIGHT): # K_LEFT is used for left arrow, K_UP is used for up arrow, and K_DOWN is used for down arrow
        ... # Do something here
    e.runGame((0,0,0))
```

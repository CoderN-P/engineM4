# The Keyboard Controller
The keyboard controller (kb) is used to register key presses. For the similar object called mouse controller (mc), see [this page](/docs/mouseController.md).
## Functions
`singlePress(givenKey)` - Check is the given key was pressed once

`held(givenKey)` - Check is the given key is being held

For `givenKey`, you will have to use the pygame constant for the key you want. See the example for more info
### Example
The built in variable `kb` is used for the keyboard controller.
```python
import engineM4 as e

while True:
    if e.kb.held(e.pygame.KEY_RIGHT): # KEY_LEFT is used for left arrow, KEY_UP is used for up arrow, and KEY_DOWN is used for down arrow
        ... # Do something here
    e.runGame((0,0,0))
```
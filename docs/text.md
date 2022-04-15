# Text
The `text` class is used to render text on the screen

# Usage
```python
import engineM4 as e

sampleText = e.text(givenString, givenSize, givenColor, givenX, givenY)
```
**NOTE** - The text fonts are stored in a font list inside engineM4. To edit the default fonts just edit the list.
The default fonts are:
```python
font_preferences = [
        "Bizarre Font Sans Serif",
        "They definitely dont have this installed Gothic",
        "Papyrus",
        "Comic Sans MS"]
```
```python
import engineM4 as e

e.font_preferences = [] # your fonts here
```
## Parameters
`giveString` **str** - A string containing the text to render.

`givenSize` **int** | **float** - The font size of the text.

`givenColor` **Tuple(Int)** - The color of the text (RGB Tuple).

`givenX` **int** - The x position of the rendered text.

`givenY` **int** - The y position of the rendered text.

## Attributes

### Read and Write Attributes
> **NOTE**
> If you want to change the attributes you will need to use `text.changeText(givenString)`

> #### Example
> ```python
> import engineM4 as e
>
> sampleText = e.text('Example text', 24, (255, 255, 255), e.screenW, e.screenH) # Renders 24px white text in the center of the screen
>
> sampleText.x = e.screenW/2
> sampleText.changeText(sampleText.textString) # Re-renders the text object on the screen with the updated attributes
> ```


`size` **int** | **float** The font size of the text in `px`

`color` **Tuple(int)** - The color of the text (RGB Tuple)

`x` **int** - The x position of the rendered text

`y` **int** - The y position of the rendered text

`visible` **bool** - Whether the text is rendered or not. **Default** `True`

### Read-Only attributes
`textString` **str** - A string containing the text to be rendered on screen

   > This can only be changed with the `changeText(givenString)` method as outlined above.
 


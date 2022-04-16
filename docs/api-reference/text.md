---
description: The text class is used to render text on the screen
---

# Text

## Usage

```python
import engineM4 as e

sampleText = e.text(givenString, givenSize, givenColor, givenX, givenY)
```

{% hint style="info" %}
The text fonts are stored in a font list inside engineM4. To edit the default fonts just edit the list. The default fonts are shown below
{% endhint %}

### Default Fonts

```python
font_preferences = [
        "Bizarre Font Sans Serif",
        "They definitely dont have this installed Gothic",
        "Papyrus",
        "Comic Sans MS"]
```

### Editing Default Fonts

```python
import engineM4 as e

e.font_preferences = [] # your fonts here
```

### Parameters

* `giveString` <mark style="color:purple;">**str**</mark> - A string containing the text to render.
* `givenSize` <mark style="color:purple;">**int**</mark> <mark style="color:purple;"></mark><mark style="color:purple;">|</mark> <mark style="color:purple;"></mark><mark style="color:purple;">**float**</mark> <mark style="color:purple;"></mark><mark style="color:purple;"></mark> - The font size of the text.
* `givenColor` <mark style="color:purple;">**Tuple(Int)**</mark> - The color of the text (RGB Tuple).
* `givenX` <mark style="color:purple;">**int**</mark> - The x position of the rendered text.
* `givenY` <mark style="color:purple;"></mark> <mark style="color:purple;"></mark><mark style="color:purple;">**int**</mark> - The y position of the rendered text.

### Attributes

#### Read and Write Attribute

{% hint style="warning" %}
If you want to change the attributes you will need to use `text.changeText(givenString)`
{% endhint %}

<details>

<summary>Example</summary>

```python
import engineM4 as e

sampleText = e.text('Example text', 24, (255, 255, 255), e.screenW, e.screenH) # Renders 24px white text in the center of the screen

sampleText.x = e.screenW/2
sampleText.changeText(sampleText.textString) # Re-renders the text object on the screen with the updated attributes
```

</details>

* `size` <mark style="color:purple;">**int**</mark> <mark style="color:purple;"></mark><mark style="color:purple;">|</mark> <mark style="color:purple;"></mark><mark style="color:purple;">**float**</mark> <mark style="color:purple;"></mark><mark style="color:purple;"></mark> The font size of the text in `px`
* `color` <mark style="color:purple;">**Tuple(int)**</mark> - The color of the text (RGB Tuple)
* `x` <mark style="color:purple;">**int**</mark> - The x position of the rendered text
* `y` <mark style="color:purple;">**int**</mark> - The y position of the rendered text
* `visible` <mark style="color:purple;">**bool**</mark> - Whether the text is rendered or not. **Default** `True`

#### Read-Only attributes

* `textString` <mark style="color:purple;">**str**</mark> - A string containing the text to be rendered on screen

{% hint style="warning" %}
This attribute can only be changed with the `changeText(givenString)`method as outlined above.
{% endhint %}

---
description: The mouse controller (mc) is used to register mouse clicks.
---

# Mouse Controller

## Class Methods

* `mouseHover(givenSprite)` - Check if the mouse is hovering over the given sprite
* `globalClick(givenButton)` - Check if the mouse is clicked anywhere on the screen.
* `spriteClick(givenSprite, givenButton)` - Check if the mouse was clicked on the given sprite.&#x20;
* `update()` - Updates all of the MouseController's attributes
  * This method is called with `e.runGame`

{% hint style="info" %}
&#x20;For `givenButton`, use `0` for leftclick, `1` for middleclick, and `2` for rightclick
{% endhint %}

<details>

<summary>Example</summary>

The built in variable `mc` stores the MouseController class

```python
import engineM4 as e
sprite = sprite(e.screenW/2-16, e.screenH-64, "sprite.png") # Example sprite

while True:
    if e.mc.spriteClick(sprite, 0):
        ... # Do something here
    e.runGame((0,0,0))
```

</details>

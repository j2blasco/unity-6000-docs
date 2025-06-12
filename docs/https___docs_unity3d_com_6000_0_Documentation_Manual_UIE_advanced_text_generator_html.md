* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-advanced-text-generator.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Work with text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-work-with-text.html)
  * Advanced Text Generator


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-color-emojis.html)
Color emojis
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-text-setting-asset.html)
UITK Text Settings assets
# Advanced Text Generator
Advanced Text Generator is a text rendering module that employs [Harfbuzz](https://harfbuzz.github.io/), [ICU](https://icu.unicode.org/), and [FreeType](https://freetype.org/) to deliver comprehensive Unicode support and text shaping capabilities.
With Advanced Text Generator, you can use a wide array of languages and **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts), such as right-to-left (RTL) languages like Arabic and Hebrew.
## Enable Advanced Text Generator
  1. From the menu, select **Edit** > **Project Settings** > **UI Toolkit**.
  2. Select the **Enable Advanced Text Generator** checkbox.


## Use Advanced Text Generator
To use Advanced Text Generator, you must use a font asset that supports the language you want to use. For example, if you want to use Arabic, you must use a font asset that supports Arabic. Advanced Text Generator only supports dynamic font assets. Before using Advanced Text Generator in your project, you must import the font into your project and [create a dynamic font asset](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-get-started-with-text.html#create-a-dynamic-font-asset) from it.
### In UI Builder
To use Advanced Text Generator in UI Builder, do the following:
  1. Select the **visual element** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement) that you want to apply to.
  2. In the **Inspector** panel, select **Inlined Styles** > **Text**.
  3. From the **Text Generator Type** dropdown, select **Advanced**.


### In USS
To use Advanced Text Generator in USS, set `-unity-text-generator` to `advanced`. For example:
```
.labelText {
    -unity-text-generator: advanced;
}

```

### In C# scripts
To use Advanced Text Generator in C# scripts, set [`TextGeneratorType`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGeneratorType.html) to `Advanced`. For example:
```
textElement.style.unityTextGenerator = new StyleEnum<TextGeneratorType>(TextGeneratorType.Advanced);

```

## Language Direction
The Language Direction is a global UXML attribute that corresponds to the to the [dir](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dir) property in HTML. This attribute sets the default text direction for any VisualElement and cascades to child elements. 
The Language Direction also impacts the ellipsis position, punctuation placement and, once support for the [:dir()](https://developer.mozilla.org/en-US/docs/Web/CSS/:dir) pseudo-state is added, allows to apply styles conditionally based on the text direction.
### Values
  * Inherited (default): The element inherits the text direction from its parent.
  * LTR (Left-to-Right): Forces the text within the element to flow from left to right.
  * RTL (Right-to-Left): Forces the text within the element to flow from right to left.


We also plan to support the `auto` value in future releases. The `auto` value dynamically determines the text direction by analyzing the Unicode characters in the text block. It counts the number of strong directional characters (LTR or RTL) and sets the direction based on the higher count.
## Cursor Movement
This section explains how cursor movement behaves in Unity’s Input Fields when handling **bidirectional text** (BIDI text).
### Logical Cursor Movement
Unity currently follows a `Logical Cursor Movement` approach. This means the cursor moves through bidirectional text based on the direction of the segment of text. For example, using the left arrow key in a sentence with Arabic and English text, it moves right-to-left through Arabic, then jumps at the leftmost character in the English segment and continues left-to-right until it reaches the end of the segment.
![Logical Cursor Movement Example](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/font/UIE-CursorMovement.gif) Logical Cursor Movement Example
### Visual Cursor Movement
Some application follow a `Visual Cursor Movement` approach. This means the cursor moves to the next visual character regardless of the direction of the text, which can sometimes feel more intuitive for users. We plan to make the cursor movement mode an option in future releases.
## Limitations
Advanced Text Generator has the following limitations:
  * Supports only dynamic font assets.
  * Customization of glyph metrics is not available. The recommended best practice is using font editing tools to adjust metrics or trim the font as needed.


Some features are not yet supported but are planned for future releases:
  * Certain Rich Text tags, including `<sprite>`, `<size>`, `<font>`, `<space>`, `<mark>`, and a few others.
  * Spacing properties such as character, word, and paragraph spacing.


When you use Advanced Text Generator, your project includes an `icudt73l` file that has a significant memory footprint of `4.8MB`. This will be improved in future releases.
## Additional resources
  * [Get started with text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-get-started-with-text.html)
  * [Font assets](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset-landing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-color-emojis.html)
Color emojis
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-text-setting-asset.html)
UITK Text Settings assets

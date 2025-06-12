* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-style-sheet.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Work with text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-work-with-text.html)
  * Style sheets


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-text-effects.html)
Text effects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite.html)
Include sprites in text
# Style sheets
If you want to reuse a style, create a custom style sheet for it, and apply it to text through the [`<style>` rich text tag](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-supported-tags.html#style).
A custom style can include opening and closing rich text tags, and leading and trailing text.
For example, you might want headings in your text to be big, red, bold, with an asterisk to either side and a line break at the end.
Instead of typing this for every heading:
`<font-weight=700><size=2em><color=#FF0000>*Heading*</color></size></font-weight><br>`
You can create a style, called `H1` that includes all of that formatting, and then apply the style to your headings. 
For instructions on how to create a custom style sheet, see [Style-with-style-sheets in Get started with text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-get-started-with-text.html#style-with-style-sheets)
To use a custom style sheet in the rich text tag, reference the style sheet asset name and the style name: `<style="assetName" name="styleName">`.
For runtime UI, if you have set a style sheet as the default style sheet in the [UITK Text Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-text-setting-asset.html), you can omit the asset name: `<style="styleName">`. For example: `<style="H1">This is heading 1</style>`.
## Additional resources
  * [Rich text tags](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-rich-text-tags.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-text-effects.html)
Text effects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite.html)
Include sprites in text

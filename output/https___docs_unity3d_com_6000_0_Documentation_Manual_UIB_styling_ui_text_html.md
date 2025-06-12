* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-styling-ui-text.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Work with text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-work-with-text.html)
  * Style text with USS


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-get-started-with-text.html)
Get started with text 
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-rich-text-tags.html)
Style text with rich text tags
# Style text with USS
You can style text with USS text properties inline in [UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UXML.html), a [USS](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS.html) file, or directly in [UI Builder](https://docs.unity3d.com/6000.0/Documentation/Manual/UIBuilder.html). To learn more about USS text properties, refer to [Text properties](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-SupportedProperties.html#unity-text).
## Style text in USS and UXML
[Text properties](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-SupportedProperties.html#unity-text) are regular USS style properties. You can set text style properties on any element. Unlike most USS style properties, text style properties propagate to child elements. 
The following USS example styles the `Label` text to bold and italic, and has a font size of `39px`:
```
Label {
    -unity-font-style: bold-and-italic; 
    font-size: 39px;
}

```

The following UXML inline style example applies the same style to the `Label` text:
```
<ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
    <ui:VisualElement>
        <ui:Label text="Label" style="-unity-font-style: bold-and-italic; font-size: 39px;" />
    </ui:VisualElement>
</ui:UXML>

```

## Style text in UI builder
To style text in UI Builder, you can use the **Text** section in a UI control’s **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window to style text.
If the UI control is a text element that inherits from [TextElement](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TextElement.html), such as [Label](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Label.html) or [Button](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Button.html), you can also set the following text styles directly in the **Canvas** on selected text elements:
  * Horizontal text align
  * Vertical text align
  * Text wrap

![Text styles are exposed as toggles in the Canvas on selected elements](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/UIBuilder/CanvasTextToggles.png) Text styles are exposed as toggles in the Canvas on selected elements
## Additional resources
  * [Get started with text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-get-started-with-text.html)
  * [Text effects](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-text-effects.html)
  * [Font assets](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-font-asset.html)
  * [Rich text tags](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-rich-text-tags.html)
  * [Style sheet assets](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-style-sheet.html)
  * [Include sprites in text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-sprite.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-get-started-with-text.html)
Get started with text 
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-rich-text-tags.html)
Style text with rich text tags

* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TextElement.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * TextElement


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TagField.html)
TagField
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TextField.html)
TextField
# TextElement
The TextElement displays text in a UI. If you create a [custom control](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-custom-controls.html) for displaying text, you can inherit it from a [TextElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextElement.html).
## Create a TextElement
You can create a TextElement with UXML or C#. The following C# example creates a TextElement with a text value and some styles:
```
var textElement = new TextElement()
{
    text = "Hello World",
    style =
    {
        fontSize = 14,
        unityFontStyleAndWeight = FontStyle.Bold,
        unityTextAlign = TextAnchor.MiddleCenter,
        color = Color.red,
        unityFontDefinition = new FontDefinition() 
        { 
            fontAsset = m_RobotoMonoRegular 
        }
    }
}

```

## C# base class and namespace
**C# class** : [`TextElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextElement.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : [`BindableElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindableElement.html)
## Member UXML attributes
This element has the following member attributes:
**Name** | **Type** | **Description**  
---|---|---  
`display-tooltip-when-elided` | `boolean` | When true, a tooltip displays the full version of elided text, and also if a tooltip had been previously provided, it will be overwritten.  
`emoji-fallback-support` | `boolean` | Specifies the order in which the system should look for Emoji characters when rendering text. If this setting is enabled, the global Emoji Fallback list will be searched first for characters defined as Emoji in the Unicode 14.0 standard.  
`enable-rich-text` | `boolean` | When false, rich text tags will not be parsed.  
`parse-escape-sequences` | `boolean` | Specifies whether escape sequences are displayed as is or if they are replaced by the character they represent.  
`text` | `string` | The text to be displayed.  
  
Changing this value will implicitly invoke the `INotifyValueChanged_1.value` setter, which will raise a `ChangeEvent_1` of type string.  
## Inherited UXML attributes
This element inherits the following attributes from its base class:
**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`focusable` | `boolean` | True if the element can be focused.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
This element also inherits the following attributes from [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-VisualElement.html):
**Name** | **Type** | **Description**  
---|---|---  
`content-container` | `string` | Child elements are added to it, usually this is the same as the element itself.  
`data-source` | `Object` | Assigns a data source to this VisualElement which overrides any inherited data source. This data source is inherited by all children.  
`data-source-path` | `string` | Path from the data source to the value.  
`data-source-type` | `System.Type` | The possible type of data source assignable to this VisualElement.  
  
This information is only used by the UI Builder as a hint to provide some completion to the data source path field when the effective data source cannot be specified at design time.  
`language-direction` | [`UIElements.LanguageDirection`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LanguageDirection.html) | Indicates the directionality of the element’s text. The value will propagate to the element’s children.  
  
Setting the languageDirection to RTL adds basic support for right-to-left (RTL) by reversing the text and handling linebreaking and word wrapping appropriately. However, it does not provide comprehensive RTL support, as this would require text shaping, which includes the reordering of characters, and OpenType font feature support. Comprehensive RTL support is planned for future updates, which will involve additional APIs to handle language, script, and font feature specifications.  
  
To enhance the RTL functionality of this property, users can explore available third-party plugins in the Unity Asset Store and make use of `ITextElementExperimentalFeatures.renderedText`  
`name` | `string` | The name of this VisualElement.  
  
Use this property to write USS selectors that target a specific element. The standard practice is to give an element a unique name.  
`picking-mode` | [`UIElements.PickingMode`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PickingMode.html) | Determines if this element can be pick during mouseEvents or `IPanel.Pick` queries.  
`style` | `string` | Sets the `VisualElement` style values.  
`tooltip` | `string` | Text to display inside an information box after the user hovers the element for a small amount of time. This is only supported in the Editor UI.  
`usage-hints` | [`UIElements.UsageHints`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UsageHints.html) | A combination of hint values that specify high-level intended usage patterns for the `VisualElement`. This property can only be set when the `VisualElement` is not yet part of a `Panel`. Once part of a `Panel`, this property becomes effectively read-only, and attempts to change it will throw an exception. The specification of proper `UsageHints` drives the system to make better decisions on how to process or accelerate certain operations based on the anticipated usage pattern. Note that those hints do not affect behavioral or visual results, but only affect the overall performance of the panel and the elements within. It’s advised to always consider specifying the proper `UsageHints`, but keep in mind that some `UsageHints` might be internally ignored under certain conditions (e.g. due to hardware limitations on the target platform).  
`view-data-key` | `string` | Used for view data persistence, such as tree expanded states, scroll position, or zoom level.  
  
This key is used to save and load the view data from the view data store. If you don’t set this key, the persistence is disabled for the associated `VisualElement`. For more information, refer to [View data persistence](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ViewData.html).  
## USS classes
The following table lists all the C# public property names and their related USS selector.
**C# property** | **USS selector** | **Description**  
---|---|---  
`ussClassName` | `.unity-text-element` | USS class name of elements of this type.  
`selectableUssClassName` | `.unity-text-element__selectable` | USS class name of selectable text elements.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
You can also use the [Matching Selectors section in the Inspector or the UI Toolkit Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-testing-ui.html#matching-selectors) to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.
## Additional resources
  * [Work with text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-work-with-text.html)
  * [TextField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TextField.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TagField.html)
TagField
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TextField.html)
TextField

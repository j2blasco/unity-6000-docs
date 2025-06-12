* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Hash128Field.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * Hash128Field


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-GroupBox.html)
GroupBox
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-HelpBox.html)
HelpBox
# Hash128Field
The Hash128Field lets users enter a [Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) value in a UI.
**Note** : To align an element with other fields in an **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, simply apply the `.unity-base-field__aligned` USS class to it. For more information, refer to [`BaseField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1.html).
## Create a Hash128Field
You can create a Hash128Field with UI Builder, UXML, or C#. The following C# example creates a Hash128Field with a Hash128 value:
```
var hash128Field = new Hash128Field();
hash128Field.label = "Label text:";
hash128Field.value = new Hash128(0x8f14e45f, 0xceea167a, 0x5a36dedd, 0x4bea2543);

```

## C# class and namespace
**C# class** : [`Hash128Field`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Hash128Field.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : [`TextInputBaseField_1`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1.html)
## Inherited UXML attributes
This element inherits the following attributes from its base class:
**Name** | **Type** | **Description**  
---|---|---  
`auto-correction` | `boolean` | Determines if the touch screen keyboard auto correction is turned on or off.  
`binding-path` | `string` | Path of the target property to be bound.  
`emoji-fallback-support` | `boolean` | Specifies the order in which the system should look for Emoji characters when rendering text. If this setting is enabled, the global Emoji Fallback list will be searched first for characters defined as Emoji in the Unicode 14.0 standard.  
`focusable` | `boolean` | True if the element can be focused.  
`hide-mobile-input` | `boolean` | Hides or shows the mobile input field.  
`is-delayed` | `boolean` | If set to true, the value property isn’t updated until either the user presses Enter or the text field loses focus.  
`keyboard-type` | `TouchScreenKeyboardType` | The type of mobile keyboard that will be used.  
`label` | `string` | The string representing the label that will appear beside the field.  
`max-length` | `int` | Maximum number of characters for the field.  
`select-all-on-focus` | `boolean` | Controls whether the element’s content is selected upon receiving focus.  
`select-all-on-mouse-up` | `boolean` | Controls whether the element’s content is selected when you mouse up for the first time.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
`value` | `Hash128` | The value associated with the field.  
`vertical-scroller-visibility` | [`UIElements.ScrollerVisibility`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollerVisibility.html) | Option for controlling the visibility of the vertical scroll bar in the `TextInputBaseField_1`.  
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
`ussClassName` | `.unity-hash128-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-hash128-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-hash128-field__input` | USS class name of input elements in elements of this type.  
`ussClassName` | `.unity-base-text-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-base-text-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-base-text-field__input` | USS class name of input elements in elements of this type.  
`singleLineInputUssClassName` | `.unity-base-text-field__input--single-line` | USS class name of single line input elements in elements of this type.  
`multilineInputUssClassName` | `.unity-base-text-field__input--multiline` | USS class name of multiline input elements in elements of this type.  
`placeholderUssClassName` | `.unity-base-text-field__input--placeholder` | USS class name of input elements when placeholder text is shown  
`ussClassName` | `.unity-base-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-base-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-base-field__input` | USS class name of input elements in elements of this type.  
`noLabelVariantUssClassName` | `.unity-base-field--no-label` | USS class name of elements of this type, when there is no label.  
`labelDraggerVariantUssClassName` | `.unity-base-field__label--with-dragger` | USS class name of labels in elements of this type, when there is a dragger attached on them.  
`mixedValueLabelUssClassName` | `.unity-base-field__label--mixed-value` | USS class name of elements that show mixed values  
`alignedFieldUssClassName` | `.unity-base-field__aligned` | USS class name of elements that are aligned in a inspector element  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
You can also use the [Matching Selectors section in the Inspector or the UI Toolkit Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-testing-ui.html#matching-selectors) to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.
## Additional resources
  * [Vector2Field](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Vector2Field.html)
  * [Vector3Field](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Vector3Field.html)
  * [Vector4Field](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Vector4Field.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-GroupBox.html)
GroupBox
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-HelpBox.html)
HelpBox

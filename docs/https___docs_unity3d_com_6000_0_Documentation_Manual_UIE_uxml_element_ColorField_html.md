* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ColorField.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * ColorField


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Button.html)
Button
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-CurveField.html)
CurveField
# ColorField
A ColorField is an [Editor-only](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-interface-overview.html#enable-editor-extension-authoring-for-ui-documents-uxml) control that lets users select a color from a color picker. It supports alpha channel and [HDR colors](https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-color-picker-reference.html). An alpha channel is an extra channel to represent the transparency level of a color. **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) colors are high-dynamic range colors that can represent a wider range of colors than standard colors.
![A ColorField control example](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uxml/color-picker.png) A ColorField control example
**Note** : To align an element with other fields in an **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, simply apply the `.unity-base-field__aligned` USS class to it. For more information, refer to [`BaseField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1.html).
## Create a ColorField
You can create a ColorField with UI Builder, UXML, or C#. The following C# example creates a ColorField with a default color and enables the alpha channel, eye dropper, and treats the color as an HDR value.
```
using UnityEditor.UIElements;
...
var colorField = new ColorField();
colorField.value = new Color(0.5f, 0.5f, 0.5f, 1.0f);
colorField.showAlpha = true;
colorField.showEyeDropper = true;
colorField.hdr = true;

```

## Example
The following UXML example creates a ColorField:
```
<UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
    <uie:ColorField label="UXML Field" name="the-uxml-field" />
</UXML>

```

The following C# example illustrates some of the customizable functionalities of the ColorField:
```
/// <sample>
// Get a reference to the field from UXML and assign a value to it.
var uxmlField = container.Q<ColorField>("the-uxml-field");
uxmlField.value = Color.red;

// Create a new field, disable it, and give it a style class.
var csharpField = new ColorField("C# Field");
csharpField.SetEnabled(false);
csharpField.AddToClassList("some-styled-field");
csharpField.value = uxmlField.value;
container.Add(csharpField);

// Mirror the value of the UXML field into the C# field.
uxmlField.RegisterCallback<ChangeEvent<Color>>((evt) =>
{
    csharpField.value = evt.newValue;
});
/// </sample>

```

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**.
## C# base class and namespace
**C# class** : [`ColorField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ColorField.html)  
**Namespace** : `UnityEditor.UIElements`  
**Base class** : [`BaseField_1`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1.html)
## Member UXML attributes
This element has the following member attributes:
**Name** | **Type** | **Description**  
---|---|---  
`hdr` | `boolean` | If true, treats the color as an HDR value. If false, treats the color as a standard LDR value.  
`show-alpha` | `boolean` | If true, allows the user to set an alpha value for the color. If false, hides the alpha component.  
`show-eye-dropper` | `boolean` | If true, the color picker will show the eyedropper control. If false, the color picker won’t show the eyedropper control.  
## Inherited UXML attributes
This element inherits the following attributes from its base class:
**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`focusable` | `boolean` | True if the element can be focused.  
`label` | `string` | The string representing the label that will appear beside the field.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
`value` | `Color` | The value associated with the field.  
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
`ussClassName` | `.unity-color-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-color-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-color-field__input` | USS class name of input elements in elements of this type.  
`colorContainerUssClassName` | `.unity-color-field__color-container` | USS class name of color container elements in elements of this type.  
`colorUssClassName` | `.unity-color-field__color` | USS class name of color elements in elements of this type.  
`mixedValueColorUssClassName` | `.unity-color-field__color--mixed-value` | USS class name of color elements in elements of this type when showing mixed values.  
`eyeDropperUssClassName` | `.unity-color-field__eyedropper` | USS class name of eyedropper elements in elements of this type.  
`hdrLabelUssClassName` | `.unity-color-field__hdr` | USS class name of hdr label elements in elements of this type.  
`gradientContainerUssClassName` | `.unity-color-field__gradient-container` | USS class name of gradient container elements in elements of this type.  
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
  * [HDR Color Picker reference](https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-color-picker-reference.html)
  * [High dynamic range](https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-landing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Button.html)
Button
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-CurveField.html)
CurveField

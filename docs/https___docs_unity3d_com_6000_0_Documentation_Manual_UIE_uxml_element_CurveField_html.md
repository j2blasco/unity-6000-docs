* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-CurveField.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * CurveField


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ColorField.html)
ColorField
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-DoubleField.html)
DoubleField
# CurveField
A CurveField is an [Editor-only](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-interface-overview.html#enable-editor-extension-authoring-for-ui-documents-uxml) control that lets users select a curve from a curve editor. You can use a CurveField to display a curve to visualize its properties or create and adjust curves for animatable properties in an **Animation Clip** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip), providing precise control over how these properties change over time.
![An example CurveField control](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uxml/curve-field.png) An example CurveField control
**Note** : To align an element with other fields in an **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, simply apply the `.unity-base-field__aligned` USS class to it. For more information, refer to [`BaseField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1.html).
## Create a CurveField
You can create a CurveField with UI Builder, UXML, or C#. The following C# example creates a CurveField with a default curve:
```
using UnityEditor.UIElements;
...
// Create a CurveField
var curveField = new CurveField();
// Set the curve
curveField.value = new AnimationCurve(new Keyframe(0, 0), new Keyframe(1, 1), new Keyframe(2, 2), new Keyframe(3, 3));
// Set the width and height of the curve editor
curveField.style.width = 300;
curveField.style.height = 400;

```

## Example
The following UXML example creates a CurveField:
```
<UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
    <uie:CurveField label="UXML Field" name="the-uxml-field" />
</UXML>

```

The following C# example illustrates some of the customizable functionalities of the CurveField:
```
/// <sample>
// Get a reference to the field from UXML and assign a value to it.
var uxmlField = container.Q<CurveField>("the-uxml-field");
uxmlField.value = new AnimationCurve(new Keyframe[]
    { new Keyframe(0, 0), new Keyframe(5, 8), new Keyframe(10, 4) });

// Create a new field, disable it, and give it a style class.
var csharpField = new CurveField("C# Field");
csharpField.SetEnabled(false);
csharpField.AddToClassList("some-styled-field");
csharpField.value = uxmlField.value;
container.Add(csharpField);

// Mirror the value of the UXML field into the C# field.
uxmlField.RegisterCallback<ChangeEvent<AnimationCurve>>((evt) =>
{
    csharpField.value = evt.newValue;
});
/// </sample>

```

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**.
## C# base class and namespace
**C# class** : [`CurveField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CurveField.html)  
**Namespace** : `UnityEditor.UIElements`  
**Base class** : [`BaseField_1`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1.html)
## Inherited UXML attributes
This element inherits the following attributes from its base class:
**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`focusable` | `boolean` | True if the element can be focused.  
`label` | `string` | The string representing the label that will appear beside the field.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
`value` | `AnimationCurve` | The value associated with the field.  
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
`ussClassName` | `.unity-curve-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-curve-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-curve-field__input` | USS class name of input elements in elements of this type.  
`contentUssClassName` | `.unity-curve-field__content` | USS class name of content elements in elements of this type.  
`borderUssClassName` | `.unity-curve-field__border` | USS class name of border elements in elements of this type.  
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
  * [AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ColorField.html)
ColorField
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-DoubleField.html)
DoubleField

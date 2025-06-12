* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-MinMaxSlider.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * MinMaxSlider


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-MaskField.html)
MaskField
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-MultiColumnListView.html)
MultiColumnListView
# MinMaxSlider
The MinMaxSlider element is a slider that lets users select a range of values within a specified minimum and maximum range. You can use it to set a range of values for various parameters, such as volume levels, character stats, or other numerical values in your UI. To use it, define the minimum and maximum values, and then slide the handle to select the range you want. 
![An example MinMaxSlider control](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uxml/min-max-slider.png) An example MinMaxSlider control
## Create a MinMaxSlider
You can create a MinMaxSlider with UI Builder, UXML, or C#. The following C# example creates a MinMaxSlider with a default value, low limit, and high limit:
```
var minMaxSlider = new MinMaxSlider();
minMaxSlider.value = new Vector2(0.25f, 0.75f);
minMaxSlider.lowLimit = 0;
minMaxSlider.highLimit = 1;

```

**Note** : To align an element with other fields in an **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, simply apply the `.unity-base-field__aligned` USS class to it. For more information, refer to [`BaseField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1.html).
## Example
The following UXML example creates a MinMaxSlider:
```
<UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
    <MinMaxSlider
        label="UXML Field"
        name="the-uxml-field"
        min-value="0"
        max-value="20"
        low-limit="-10"
        high-limit="40" />
</UXML>

```

The following C# example illustrates some of the customizable functionalities of the MinMaxSlider:
```
/// <sample>
// Get a reference to the field from UXML and assign a value to it.
var uxmlField = container.Q<MinMaxSlider>("the-uxml-field");
uxmlField.value = new Vector2(10, 12);

// Create a new field, disable it, and give it a style class.
var csharpField = new MinMaxSlider("C# Field", 0, 20, -10, 40);
csharpField.SetEnabled(false);
csharpField.AddToClassList("some-styled-field");
csharpField.value = uxmlField.value;
container.Add(csharpField);

// Mirror the value of the UXML field into the C# field.
uxmlField.RegisterCallback<ChangeEvent<Vector2>>((evt) =>
{
    csharpField.value = evt.newValue;
});
/// </sample>

```

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**.
## C# base class and namespace
**C# class** : [`MinMaxSlider`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MinMaxSlider.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : [`BaseField_1`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1.html)
## Member UXML attributes
This element has the following member attributes:
**Name** | **Type** | **Description**  
---|---|---  
`high-limit` | `float` | This is the high limit of the slider.  
`low-limit` | `float` | This is the low limit of the slider.  
`value` | `Vector2` | This is the value of the slider. This is a `Vector2` where the x is the lower bound and the y is the higher bound.  
## Inherited UXML attributes
This element inherits the following attributes from its base class:
**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`focusable` | `boolean` | True if the element can be focused.  
`label` | `string` | The string representing the label that will appear beside the field.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
`value` | `Vector2` | The value associated with the field.  
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
`ussClassName` | `.unity-min-max-slider` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-min-max-slider__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-min-max-slider__input` | USS class name of input elements in elements of this type.  
`trackerUssClassName` | `.unity-min-max-slider__tracker` | USS class name of tracker elements in elements of this type.  
`draggerUssClassName` | `.unity-min-max-slider__dragger` | USS class name of dragger elements in elements of this type.  
`minThumbUssClassName` | `.unity-min-max-slider__min-thumb` | USS class name of the minimum thumb elements in elements of this type.  
`maxThumbUssClassName` | `.unity-min-max-slider__max-thumb` | USS class name of the maximum thumb elements in elements of this type.  
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
  * [Slider](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Slider.html)
  * [SliderInt](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-SliderInt.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-MaskField.html)
MaskField
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-MultiColumnListView.html)
MultiColumnListView

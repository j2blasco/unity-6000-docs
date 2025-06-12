* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Slider.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * Slider


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Scroller.html)
Scroller
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-SliderInt.html)
SliderInt
# Slider
A Slider lets users select a floating-point value from a range of values. You can use a Slider to adjust a value, such as the volume of a sound or the brightness of a light. To set the value, you drag a thumb along a track, or click the track itself. A slider can also include a **text input field** A field that allows the user to input a Text string [More info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-InputField.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextInputField), where you can modify the value directly.
**Note** : To align an element with other fields in an **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, simply apply the `.unity-base-field__aligned` USS class to it. For more information, refer to [`BaseField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1.html).
## Create a Slider
You can create a Slider with UI Builder, UXML, or C#. The following C# example creates a Slider with a default value, low value, and high value, and sets the direction of the slider:
```
var slider = new Slider();
slider.value = 0.5f;
slider.lowValue = 0;
slider.highValue = 100;
slider.direction = SliderDirection.Horizontal;

```

## Set page size
The Slider control has a page-size property that controls how much the thumb moves, and how much the value changes, when you click the track to either side of the thumb.
If the page size value is `0`, clicking the track moves the thumb to the cursor or pointer position, and updates the value accordingly.
If the page size value is greater than `0`, clicking the track moves the thumb toward the cursor or pointer position by a specific amount. Slider controls treat page-size as a percentage of the total range.
For example, if the total range is `200`, and the page size is `20`, then the page size amount is `20%` of `200`, or `40`. Each time you click the track, the thumb moves, and the value increases or decreases by `40`.
## Keyboard Shortcuts
You can use keyboard shortcuts to navigate and adjust the Slider control. The following table lists the keyboard shortcuts: 
**Shortcut** | **Action**  
---|---  
**Arrow Keys** | Move by `1/100` of the entire range.  
**Arrow Keys + Shift** | Move by `1/10` of the entire range.  
**Home** | Jump to the start of the slider.  
**End** | Jump to the end of the slider.  
**Page Up** | Move up by `(1/100 of the range) × page size`.  
**Page Down** | Move down by `(1/100 of the range) × page size`.  
## Example
The following UXML example creates a Slider:
```
<UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
    <Slider
        label="UXML Slider"
        name="the-uxml-slider"
        low-value="0"
        high-value="100"
        page-size="1"
        value="42.2" />
</UXML>

```

The following C# example illustrates some of the customizable functionalities of the Slider:
```
/// <sample>
// Get a reference to the slider from UXML and assign it its value.
var uxmlSlider = container.Q<Slider>("the-uxml-slider");
uxmlSlider.value = 42.2f;

// Create a new slider, disable it, and give it a style class.
var csharpSlider = new Slider("C# Slider", 0, 100);
csharpSlider.SetEnabled(false);
csharpSlider.AddToClassList("some-styled-slider");
csharpSlider.value = uxmlSlider.value;
container.Add(csharpSlider);

// Mirror value of uxml slider into the C# field.
uxmlSlider.RegisterCallback<ChangeEvent<float>>((evt) =>
{
    csharpSlider.value = evt.newValue;
});
/// </sample>

```

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**.
## C# base class and namespace
**C# class** : [`Slider`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : [`BaseSlider_1`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseSlider_1.html)
## Inherited UXML attributes
This element inherits the following attributes from its base class:
**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`direction` | [`UIElements.SliderDirection`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SliderDirection.html) | This is the actual property to contain the direction of the slider.  
`fill` | `boolean` | Enables fill to set the color and shape of a slider.  
`focusable` | `boolean` | True if the element can be focused.  
`high-value` | `float` | This is the maximum value that the slider encodes.  
`inverted` | `boolean` | This indicates whether or not this slider is inverted. For an inverted horizontal slider, high value is located to the left, low value is located to the right For an inverted vertical slider, high value is located to the bottom, low value is located to the top.  
`label` | `string` | The string representing the label that will appear beside the field.  
`low-value` | `float` | This is the minimum value that the slider encodes.  
`page-size` | `float` | Represents the value that should be applied to the calculated scroll offset while scrolling the slider, such as when clicking within the track or clicking the slider arrows.  
`show-input-field` | `boolean` | The visibility of the optional field inside the slider control.  
  
Set this property to true to display a numerical text field that provides another way to edit the slider value.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
`value` | `float` | The actual value of the slider.  
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
`ussClassName` | `.unity-slider` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-slider__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-slider__input` | USS class name of input elements in elements of this type.  
`ussClassName` | `.unity-base-slider` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-base-slider__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-base-slider__input` | USS class name of input elements in elements of this type.  
`horizontalVariantUssClassName` | `.unity-base-slider--horizontal` | USS class name of elements of this type, when they are displayed horizontally.  
`verticalVariantUssClassName` | `.unity-base-slider--vertical` | USS class name of elements of this type, when they are displayed vertically.  
`dragContainerUssClassName` | `.unity-base-slider__drag-container` | USS class name of container elements in elements of this type.  
`trackerUssClassName` | `.unity-base-slider__tracker` | USS class name of tracker elements in elements of this type.  
`draggerUssClassName` | `.unity-base-slider__dragger` | USS class name of dragger elements in elements of this type.  
`draggerBorderUssClassName` | `.unity-base-slider__dragger-border` | USS class name of the dragger border element in elements of this type.  
`fillUssClassName` | `.unity-base-slider__fill` | USS class name of fill element in elements of this type.  
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
  * [SliderInt](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-SliderInt.html)
  * [MinMaxSlider](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-MinMaxSlider.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Scroller.html)
Scroller
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-SliderInt.html)
SliderInt

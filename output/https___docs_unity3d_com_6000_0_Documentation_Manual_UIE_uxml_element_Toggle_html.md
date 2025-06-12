* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Toggle.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * Toggle


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TemplateContainer.html)
TemplateContainer
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ToggleButtonGroup.html)
ToggleButtonGroup
# Toggle
A Toggle includes an image and a label. Just like other standard UI Toolkit controls, such as a [Button](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Button.html), a Toggle has a Clickable manipulator attached to it that registers to [`MouseUpEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseUpEvent.html) and [`PointerUpEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerUpEvent.html). When one of those events triggers the manipulator, the Toggle’s value changes from `true` to `false` or from `false` to `true`. You can read or set the current values of a Toggle. You can also bind a Toggle to a `Boolean` variable.
You can display or hide elements based on other conditions, such as a selection from a drop-down, or an enabled option. An example of a conditional UI is the Unity **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector). It displays additional options when you activate **Physical Camera** mode.
**Note** : To align an element with other fields in an Inspector window, simply apply the `.unity-base-field__aligned` USS class to it. For more information, refer to [`BaseField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1.html).
## Create a Toggle
You can create a Toggle with UI Builder, UXML, or C#.
The following C# example creates a [Toggle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) with a specific label:
```
Toggle myToggle = new Toggle("Click me");

```

## Style a Toggle
By default, a Toggle control appears as a checkbox. You can apply styles to make it look like a typical toggle switch.
To style the checkbox of a toggle, use the `.unity-toggle__input` and `.unity-toggle__checkmark` style properties. For example, if you have applied a class named `className` to the Toggle. The following USS changes the background images of the checkbox when you select or clear the toggle:
```
/* Set the background image when the checkbox is selected. */
.className:checked > .unity-toggle__input > .unity-toggle__checkmark {
    background-image: url("path/to/image-file");
}

/* Set the background image When the checkbox is not selected. */
.className > .unity-toggle__input > .unity-toggle__checkmark {
    background-image: url("path/to/image-file"); 
}

```

## Examples
The following UXML example creates a Toggle:
```
<UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
    <Toggle label="UXML Field" name="the-uxml-field" />
</UXML>

```

The following C# example illustrates some of the customizable functionalities of the Toggle:
```
/// <sample>
// Get a reference to the field from UXML and assign a value to it.
var uxmlField = container.Q<Toggle>("the-uxml-field");
uxmlField.value = true;

// Create a new field, disable it, and give it a style class.
var csharpField = new Toggle("C# Field");
csharpField.value = false;
csharpField.SetEnabled(false);
csharpField.AddToClassList("some-styled-field");
csharpField.value = uxmlField.value;
container.Add(csharpField);

// Mirror the value of the UXML field into the C# field.
uxmlField.RegisterCallback<ChangeEvent<bool>>((evt) =>
{
    csharpField.value = evt.newValue;
});
/// </sample>

```

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**.
For more examples, refer to the following:
  * [Create a conditional UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-conditional-ui.html).


## C# base class and namespace
**C# class** : [`Toggle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : [`BaseBoolField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseBoolField.html)
## Inherited UXML attributes
This element inherits the following attributes from its base class:
**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`focusable` | `boolean` | True if the element can be focused.  
`label` | `string` | The string representing the label that will appear beside the field.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
`text` | `string` | Optional text that appears after the BaseBoolField.  
  
Unity creates a `Label` automatically if one does not exist.  
`toggle-on-label-click` | `boolean` | Whether to activate the toggle when the user clicks the label.  
`value` | `boolean` | The value associated with the field.  
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
`ussClassName` | `.unity-toggle` | USS class name for Toggle elements.  
  
Unity adds this USS class to every instance of the Toggle element. Any styling applied to this class affects every Toggle located beside, or below the stylesheet in the visual tree.  
`labelUssClassName` | `.unity-toggle__label` | USS class name for Labels in Toggle elements.  
  
Unity adds this USS class to the `Label` sub-element of the `Toggle` if the Toggle has a Label.  
`inputUssClassName` | `.unity-toggle__input` | USS class name of input elements in Toggle elements.  
  
Unity adds this USS class to the input sub-element of the `Toggle`. The input sub-element provides responses to the manipulator.  
`noTextVariantUssClassName` | `.unity-toggle--no-text` | USS class name of Toggle elements that have no text.  
  
Unity adds this USS class to the `Toggle` if the Toggle does not have a label.  
`checkmarkUssClassName` | `.unity-toggle__checkmark` | USS class name of Images in Toggle elements.  
  
Unity adds this USS class to the Image sub-element of the `Toggle` that contains the checkmark image.  
`textUssClassName` | `.unity-toggle__text` | USS class name of Text elements in Toggle elements.  
  
Unity adds this USS class to Text sub-elements of the `Toggle`.  
`mixedValuesUssClassName` | `.unity-toggle__mixed-values` | USS class name of Toggle elements that have mixed values  
  
Unity adds this USS class to checkmark of the `Toggle` when it has mixed values.  
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
  * [Foldout](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Foldout.html)
  * [Pseudo-classes](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-Selectors-Pseudo-Classes.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TemplateContainer.html)
TemplateContainer
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ToggleButtonGroup.html)
ToggleButtonGroup

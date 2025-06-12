* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-DropdownField.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * DropdownField


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-DoubleField.html)
DoubleField
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-EnumField.html)
EnumField
# DropdownField
A DropdownField lets users choose a value from a list. When clicking on the control, it opens a drawer that presents multiple options, allowing users to select one. If you want to always display all the choices, use [RadioButtonGroup](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-RadioButtonGroup.html).
**Note** : To align an element with other fields in an **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, simply apply the `.unity-base-field__aligned` USS class to it. For more information, refer to [`BaseField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1.html).
## Create a DropdownField
You can create a DropdownField with UI Builder, UXML, or C#. 
**UI Builder**
To add options for a DropdownField in UI Builder, in the Inspector panel of the DropdownField, set the options in the **Choices** field. 
To set the default value, in the Inspector of the DropdownField, enter the numbering sequence of the option in **Index** , starting at `0`. 
**C#**
The following C# example create a DropdownField with three options. The DropdownField selects the first option by default:
```
var dropdown = new DropdownField("Options", new List<string> { "Option 1", "Option 2", "Option 3" }, 0);

//Add another option
dropdown.choices.Add("Option 4");

// To return int value instead of string
dropdown.index = 1; // Option 2
dropdown.value = "Option3";
Assert.IsTrue(myDropdown.index == 2);

// Register to the value changed callback
dropdown.RegisterValueChangedCallback(evt => Debug.Log(evt.newValue));

```

## Change styles for a DropdownField
You can override the default Panel Settings fields in a USS file to change the styles of a DropdownField:
  1. In the **Hierarchy** window, select your UI Document (.uxml).
  2. Set **Panel Settings** as your [Panel Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Runtime-Panel-Settings.html) asset. If you don’t have an existing Panel Settings asset, follow the instructions in the dialog to create one.
  3. In your **Panel Settings** asset, [assign a Theme Style Sheet](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-tss.html#apply-a-tss).
  4. In the **Project** window, select your TSS file.
  5. Go to **Style Sheets** and select the **Add** (**+**) button.
  6. Set your **Style Sheet** as your [USS file](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-about-uss.html).


## Examples
The following UXML example creates a DropdownField:
```
<UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
    <DropdownField label="UXML Field" name="the-uxml-field" />
</UXML>

```

The following C# example illustrates some of the customizable functionalities of the DropdownField:
```
/// <sample>
// You can provide the list of choices by code, or by comma separated values in UXML
// <DropdownField .... choices="Option 1,Option 2,Option 3" .... />
var choices = new List<string> { "Option 1", "Option 2", "Option 3" };

// Get a reference to the dropdown field from UXML and assign a value to it.
var uxmlField = container.Q<DropdownField>("the-uxml-field");
uxmlField.choices = choices;
uxmlField.value = choices[0];

// Create a new dropdown with the same choices, disable it, and give it a style class.
var csharpField = new DropdownField("C# Field", choices, 0);
csharpField.SetEnabled(false);
csharpField.AddToClassList("some-styled-field");
container.Add(csharpField);

// Mirror the value of the UXML field into the C# field.
uxmlField.RegisterCallback<ChangeEvent<string>>((evt) =>
{
    csharpField.value = evt.newValue;
});
/// </sample>

```

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**.
## C# base class and namespace
**C# class** : [`DropdownField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownField.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : [`PopupField_1`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PopupField_1.html)
## Inherited UXML attributes
This element inherits the following attributes from its base class:
**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`choices` | `IList` | The list of choices to display in the popup menu.  
`focusable` | `boolean` | True if the element can be focused.  
`index` | `int` | The currently selected index in the popup menu. Setting the index will update the ::ref::value field and send a property change notification.  
`label` | `string` | The string representing the label that will appear beside the field.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
`value` | `int` | The currently selected value in the popup menu.  
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
`ussClassName` | `.unity-popup-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-popup-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-popup-field__input` | USS class name of input elements in elements of this type.  
`ussClassName` | `.unity-base-popup-field` | USS class name of elements of this type.  
`textUssClassName` | `.unity-base-popup-field__text` | USS class name of text elements in elements of this type.  
`arrowUssClassName` | `.unity-base-popup-field__arrow` | USS class name of arrow indicators in elements of this type.  
`labelUssClassName` | `.unity-base-popup-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-base-popup-field__input` | USS class name of input elements in elements of this type.  
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
  * [RadioButtonGroup](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-RadioButtonGroup.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-DoubleField.html)
DoubleField
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-EnumField.html)
EnumField

* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-RadioButton.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * RadioButton


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-PropertyField.html)
PropertyField
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-RadioButtonGroup.html)
RadioButtonGroup
# RadioButton
A RadioButton lets users select a single choice when used along with other RadioButtons in a group. You can use a [GroupBox](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-GroupBox.html) to group RadioButtons. Otherwise, the [panel](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-panels.html) acts as the default group.
**Note** : To align an element with other fields in an **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, simply apply the `.unity-base-field__aligned` USS class to it. For more information, refer to [`BaseField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1.html).
## Create a RadioButton
You can create a RadioButton with UI Builder, UXML, or C#. The following C# example creates two new radio buttons in the same container and logically groups them together in the panel.
```
var choice1 = new RadioButton() { text = "Choice 1" };
choice1.RegisterValueChangedCallback(v => Debug.Log("Choice 1 is : " + v.newValue));
var choice2 = new RadioButton() { text = "Choice 2" };
choice2.RegisterValueChangedCallback(v => Debug.Log("Choice 2 is : " + v.newValue));
container.Add(choice1);
container.Add(choice2);

```

## Examples
The following UXML example creates a RadioButton:
```
<UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
    <GroupBox>
        <RadioButton label="UXML Field 1" name="the-uxml-field1" />
        <RadioButton label="UXML Field 2" name="the-uxml-field2" />
    </GroupBox>
</UXML>

```

The following C# example illustrates some of the customizable functionalities of the RadioButton:
```
/// <sample>
// Note: See also RadioButtonGroup in the ChoiceField section of UI Toolkit Samples

// Get a reference to the first radio button from UXML and assign a value to it.
var uxmlField1 = container.Q<RadioButton>("the-uxml-field1");
var uxmlField2 = container.Q<RadioButton>("the-uxml-field2");
uxmlField1.value = true;

// Create two RadioButtons in a separate group, disable them, and give them a style class.
var groupBox = new GroupBox();
container.Add(groupBox);

var csharpField1 = new RadioButton("C# Field 1");
csharpField1.SetEnabled(false);
csharpField1.AddToClassList("some-styled-field");
groupBox.Add(csharpField1);

var csharpField2 = new RadioButton("C# Field 2");
csharpField2.SetEnabled(false);
csharpField2.AddToClassList("some-styled-field");
groupBox.Add(csharpField2);

csharpField1.value = uxmlField1.value;

// Mirror the value of the UXML field into the C# field.
uxmlField1.RegisterCallback<ChangeEvent<bool>>((evt) =>
{
    csharpField1.value = evt.newValue;
});
uxmlField2.RegisterCallback<ChangeEvent<bool>>((evt) =>
{
    csharpField2.value = evt.newValue;
});
/// </sample>

```

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**.
## C# class and namespace
**C# class** : [`RadioButton`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RadioButton.html)  
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
`ussClassName` | `.unity-radio-button` | USS class name for RadioButton elements.  
  
Unity adds this USS class to every instance of the RadioButton element. Any styling applied to this class affects every RadioButton located beside, or below the stylesheet in the visual tree.  
`labelUssClassName` | `.unity-radio-button__label` | USS class name for Labels in RadioButton elements.  
  
Unity adds this USS class to the `Label` sub-element of the `RadioButton` if the RadioButton has a Label.  
`inputUssClassName` | `.unity-radio-button__input` | USS class name of input elements in RadioButton elements.  
  
Unity adds this USS class to the input sub-element of the `RadioButton`. The input sub-element provides responses to the manipulator.  
`checkmarkBackgroundUssClassName` | `.unity-radio-button__checkmark-background` | USS class name of checkmark background in RadioButton elements.  
  
Unity adds this USS class to the checkmark background sub-element of the `RadioButton`.  
`checkmarkUssClassName` | `.unity-radio-button__checkmark` | USS class name of checkmark in RadioButton elements.  
  
Unity adds this USS class to the checkmark sub-element of the `RadioButton`.  
`textUssClassName` | `.unity-radio-button__text` | USS class name of Text elements in RadioButton elements.  
  
Unity adds this USS class to Text sub-elements of the `RadioButton`.  
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
  * [GroupBox](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-GroupBox.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-PropertyField.html)
PropertyField
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-RadioButtonGroup.html)
RadioButtonGroup

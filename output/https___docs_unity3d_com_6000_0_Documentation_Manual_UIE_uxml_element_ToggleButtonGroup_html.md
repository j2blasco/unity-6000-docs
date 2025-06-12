* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ToggleButtonGroup.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * ToggleButtonGroup


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Toggle.html)
Toggle
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Toolbar.html)
Toolbar
# ToggleButtonGroup
Use ToggleButtonGroup to enable single or multiple selections from a logical group of [Button](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Button.html) elements. The ToggleButtonGroup consists of a label and a set of interactable Button elements.
**Note** : To align an element with other fields in an **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, simply apply the `.unity-base-field__aligned` USS class to it. For more information, refer to [`BaseField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1.html).
## Create a ToggleButtonGroup
You can create a ToggleButtonGroup with UI Builder, UXML, and C#.
**UI Builder**
To create a ToggleButtonGroup in UI Builder:
  1. Drag **ToggleButtonGroup** from the **Library** panel into the **Hierarchy** panel.
  2. Add a set of **Button** elements to the **ToggleButtonGroup** element as its child elements.


To create a ToggleButtonGroup in UXML, add a ToggleButtonGroup element to a UXML document and add a set of Button elements as its child elements. For example:
**C#**
To create a ToggleButtonGroup in C#, create a new instance of a [ToggleButtonGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroup.html) object and add a set of [Buttons](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html). For example:
```
ToggleButtonGroup myElement = new ToggleButtonGroup("Label text");
myElement.Add(new Button("Button 1"));
myElement.Add(new Button("Button 2"));
myElement.Add(new Button("Button 3"));

```

By default, you can select one button at a time. To enable multiple selections, set the `is-multiple-selection` to `true`.
To enable empty selection, set the `allow-empty-selection` to `true`.
## Example
The following UXML example creates a ToggleButtonGroup with Buttons:
```
<UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
    <ToggleButtonGroup label="UXML Toggle Button Group">
        <Button text="A"/>
        <Button text="B"/>
        <Button text="C"/>
        <Button text="D"/>
        <Button text="E"/>
    </ToggleButtonGroup>
</UXML>

```

The following C# example illustrates some of the customizable functionalities of the ToggleButtonGroup and its Buttons:
```
/// <sample>
// Create custom buttons with Text value only.
var csharpToggleButtonGroupWithButtonTextOnly = new ToggleButtonGroup("C# Toggle Button Group Buttons with Text");
csharpToggleButtonGroupWithButtonTextOnly.Add(new Button() { text = "one", tooltip = "custom button one" });
csharpToggleButtonGroupWithButtonTextOnly.Add(new Button() { text = "two", tooltip = "custom button two" });
container.Add(csharpToggleButtonGroupWithButtonTextOnly);

// Create custom buttons with IconImage value only.
var csharpToggleButtonGroupWithButtonIconOnly = new ToggleButtonGroup("C# Toggle Button Group Buttons with Icons");
csharpToggleButtonGroupWithButtonIconOnly.Add(new Button() { iconImage = EditorGUIUtility.FindTexture("d_PlayButton"), tooltip = "Play" });
csharpToggleButtonGroupWithButtonIconOnly.Add(new Button() { iconImage = EditorGUIUtility.FindTexture("d_PauseButton"), tooltip = "Pause" });
csharpToggleButtonGroupWithButtonIconOnly.Add(new Button() { iconImage = EditorGUIUtility.FindTexture("d_StepButton"), tooltip = "Step" });
container.Add(csharpToggleButtonGroupWithButtonIconOnly);

// Create custom buttons with IconImage and Text.
var csharpToggleButtonGroupWithButtonIconAndText = new ToggleButtonGroup("C# Toggle Button Group Buttons with Icons and Text");
csharpToggleButtonGroupWithButtonIconAndText.Add(new Button() { iconImage = EditorGUIUtility.FindTexture("d_PlayButton"), text = "Play", tooltip = "Play" });
csharpToggleButtonGroupWithButtonIconAndText.Add(new Button() { iconImage = EditorGUIUtility.FindTexture("d_PauseButton"), text = "Pause", tooltip = "Pause" });
csharpToggleButtonGroupWithButtonIconAndText.Add(new Button() { iconImage = EditorGUIUtility.FindTexture("d_StepButton"), text = "Step", tooltip = "Step" });
container.Add(csharpToggleButtonGroupWithButtonIconAndText);

// Create custom buttons with IconImage, Text and AllowEmptySelection.
var csharpToggleButtonGroupSingleSelectionAndAllowEmptySelection = new ToggleButtonGroup("C# Toggle Button Group Buttons with Allow Empty Selection") { allowEmptySelection = true };
csharpToggleButtonGroupSingleSelectionAndAllowEmptySelection.Add(new Button() { iconImage = EditorGUIUtility.FindTexture("d_PlayButton"), text = "Play", tooltip = "Play" });
csharpToggleButtonGroupSingleSelectionAndAllowEmptySelection.Add(new Button() { iconImage = EditorGUIUtility.FindTexture("d_PauseButton"), text = "Pause", tooltip = "Pause" });
csharpToggleButtonGroupSingleSelectionAndAllowEmptySelection.Add(new Button() { iconImage = EditorGUIUtility.FindTexture("d_StepButton"), text = "Step", tooltip = "Step" });
container.Add(csharpToggleButtonGroupSingleSelectionAndAllowEmptySelection);

// Create a ToggleButtonGroup that allows multiple active selections.
var csharpToggleButtonGroupAllowMultiSelect = new ToggleButtonGroup("C# Toggle Button Group with Multiple Selection Enabled") { isMultipleSelection = true };
csharpToggleButtonGroupAllowMultiSelect.Add(new Button() { text = "X", tooltip = "tooltip text for X" });
csharpToggleButtonGroupAllowMultiSelect.Add(new Button() { text = "Y", tooltip = "tooltip text for Y" });
csharpToggleButtonGroupAllowMultiSelect.Add(new Button() { text = "Z", tooltip = "tooltip text for Z" });
container.Add(csharpToggleButtonGroupAllowMultiSelect);

// Create a ToggleButtonGroup that allows multiple active selections and allow empty selection.
var csharpToggleButtonGroupAllowMultiSelectWithAllowEmptySelection = new ToggleButtonGroup("C# Toggle Button Group with Multiple Selection and Allow Empty Selection") { isMultipleSelection = true, allowEmptySelection = true };
csharpToggleButtonGroupAllowMultiSelectWithAllowEmptySelection.Add(new Button() { text = "X", tooltip = "tooltip text for X" });
csharpToggleButtonGroupAllowMultiSelectWithAllowEmptySelection.Add(new Button() { text = "Y", tooltip = "tooltip text for Y" });
csharpToggleButtonGroupAllowMultiSelectWithAllowEmptySelection.Add(new Button() { text = "Z", tooltip = "tooltip text for Z" });
container.Add(csharpToggleButtonGroupAllowMultiSelectWithAllowEmptySelection);

// Create ToggleButtonGroup with a custom class that sets the text's font style to Bold.
var csharpToggleButtonGroupWithCustomClass = new ToggleButtonGroup("C# Toggle Button Group with a Custom Class");
csharpToggleButtonGroupWithCustomClass.AddToClassList("my-custom-style");
csharpToggleButtonGroupWithCustomClass.Add(new Button() { text = "Button A", tooltip = "Bolded font Button A" });
csharpToggleButtonGroupWithCustomClass.Add(new Button() { text = "Button B", tooltip = "Bolded font Button B" });
container.Add(csharpToggleButtonGroupWithCustomClass);
/// </sample>

```

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**.
## C# base class and namespace
**C# class** : [`ToggleButtonGroup`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroup.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : [`BaseField_1`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1.html)
## Member UXML attributes
This element has the following member attributes:
**Name** | **Type** | **Description**  
---|---|---  
`allow-empty-selection` | `boolean` | Allows having all buttons to be unchecked when set to true.  
  
When the property value is false, the control will automatically set the first available button to checked.  
`is-multiple-selection` | `boolean` | Whether all buttons can be selected.  
## Inherited UXML attributes
This element inherits the following attributes from its base class:
**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`focusable` | `boolean` | True if the element can be focused.  
`label` | `string` | The string representing the label that will appear beside the field.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
`value` | [`UIElements.ToggleButtonGroupState`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState.html) | The value associated with the field.  
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
`ussClassName` | `.unity-toggle-button-group` | USS class name of elements for this type.  
`containerUssClassName` | `.unity-toggle-button-group__container` | USS class name of container element of this type.  
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
  * [Button](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Button.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Toggle.html)
Toggle
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Toolbar.html)
Toolbar

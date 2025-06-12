* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-FloatField.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * FloatField


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-EnumFlagsField.html)
EnumFlagsField
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Foldout.html)
Foldout
# FloatField
A FloatField lets users input a numerical float value into an application. It accepts and displays text input. You can set placeholder text to provide hints or instructions to the user on what to enter. You can also add validation functions to ensure that the entered data meets certain requirements.
**Note** : To align a FloatField with other fields in an **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, simply apply the `.unity-base-field__aligned` USS class to it. For more information, refer to [`BaseField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1.html).
## Create a FloatField
You can create a FloatField with UI Builder, UXML, and C#. The following C# example creates a FloatField with a value change callback:
```
FloatField myElement = new FloatField("Label text");

// Align the float field with the other fields.
myElement.AddToClassList("unity-base-field__aligned");
myElement.value = 0.5f;

// To delay the value change callback until the user has finished editing the value, set the isDelayed property to true.
myElement.isDelayed = true;
myElement.RegisterValueChangedCallback(evt => Debug.Log("New value: " + evt.newValue));

```

## Set a placeholder text
You can set a placeholder text for the element. You can also hide the placeholder text on focus. 
**Note** : The placeholder text won’t display if you set a value for the element. To unset a value in UI Builder, right-click the **Value** field in the element’s Inspector tab and select **Unset**.
In C#, use the [`placeholder`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ITextEdition-placeholder.html) and the [`hidePlaceholderOnFocus`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ITextEdition-hidePlaceholderOnFocus.html) properties through [`textEdition`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-textEdition.html):
```
myElement.textEdition.placeholder = "Enter your value here";
myElement.textEdition.hidePlaceholderOnFocus = true;

```

To style the placeholder text, use the `.unity-base-text-field__input--placeholder` USS selector.
## Customize the input text selection
Input text is selectable by default. You can customize the selection behaviors such as [`selectAllOnMouseUP`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ITextSelection-selectAllOnMouseUp.html) and [`selectAllOnFocus`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ITextSelection-selectAllOnFocus.html).
In C#, set them through [`textSelection`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-textSelection.html):
```
myElement.textSelection.selectAllOnMouseUp = false;
myElement.textSelection.selectAllOnFocus = false;

```

## Example
The following UXML example creates a FloatField with a placeholder:
```
<UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
    <FloatField label="UXML Field" name="the-uxml-field" />
</UXML>

```

The following C# example illustrates some of the customizable functionalities of the FloatField:
```
/// <sample>
// Get a reference to the field from UXML and assign a value to it.
var uxmlField = container.Q<FloatField>("the-uxml-field");
uxmlField.value = 42.4f;

// Create a new field, disable it, and give it a style class.
var csharpField = new FloatField("C# Field");
csharpField.SetEnabled(false);
csharpField.AddToClassList("some-styled-field");
csharpField.value = uxmlField.value;
container.Add(csharpField);

// Mirror the value of the UXML field into the C# field.
uxmlField.RegisterCallback<ChangeEvent<float>>((evt) =>
{
    csharpField.value = evt.newValue;
});
/// </sample>

```

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**.
## C# base class and namespace
**C# class** : [`FloatField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FloatField.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : [`TextValueField_1`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextValueField_1.html)
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
`value` | `float` | The value associated with the field.  
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
`ussClassName` | `.unity-float-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-float-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-float-field__input` | USS class name of input elements in elements of this type.  
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
  * [Label](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Label.html)
  * [TextField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TextField.html)
  * [IntegerField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-IntegerField.html)
  * [DoubleField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-DoubleField.html)
  * [LongField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-LongField.html)
  * [PropertyField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-PropertyField.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-EnumFlagsField.html)
EnumFlagsField
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Foldout.html)
Foldout

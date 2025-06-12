* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TextField.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * TextField


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TextElement.html)
TextElement
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TemplateContainer.html)
TemplateContainer
# TextField
A TextField lets users input text data into an application. It accepts and displays text input. You can set placeholder text to provide hints or instructions to the user on what to enter. You can also add validation functions to ensure that the entered data meets certain requirements.
**Note** : To align a TextField with other fields in an **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, simply apply the `.unity-base-field__aligned` USS class to it. For more information, refer to [`BaseField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1.html).
## Create a TextField
You can create a TextField with UI Builder, UXML, and C#. The following C# example creates a TextField that allows multiple lines text input:
```
var textField = new TextField();
textField.label = "Enter your text here:";
textField.multiline = true;
textField.maxLength = 140;
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

You can also style the selected text using the `--unity-selection-color` USS custom property. For example, the following USS sets the color of the selected input text to yellow: 
```
.unity-base-text-field__input {
    --unity-selection-color: yellow;
}

```

## Enable a vertical scrollbar
If you have enabled multiline text on the TextField, you can display a vertical scrollbar for the **text input field** A field that allows the user to input a Text string [More info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-InputField.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextInputField).
In C#, set the [`verticalScrollerVisibility`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-verticalScrollerVisibility.html) property to [`ScrollerVisibility.Auto`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollerVisibility.Auto.html) or [`ScrollerVisibility.AlwaysVisible`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollerVisibility.AlwaysVisible.html):
```
// Set the multiline property to true to enable multiple lines of text
textField.multiline = true;

// Set the vertical scrollbar visibility to AlwaysVisible
textField.verticalScrollerVisibility = ScrollerVisibility.AlwaysVisible;

```

## Control the behavior of the input text
You can use [events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events.html) to control the behavior of the input text. The following example uses event callback functions to handle navigation and submission events for a text field. The example registers [navigation events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Navigation-Events.html) to the [TrickleDown](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Dispatching.html) phase before they’re handled by the `TextElement` base class:
```
// A callback function that executes submit logic to handle user input submission. 
// It stops the propagation of the event to prevent it from reaching other event handlers.
myField.RegisterCallback<NavigationSubmitEvent>((evt) => {

    // Submit logic
    evt.StopPropagation();
}, TrickleDown.TrickleDown);

// A callback function that executes focus logic to handle navigation between different UI elements. 
// If the navigation direction is up, down, left, or right, it stops the propagation of the event and instructs 
// the focusController to ignore the event.
myField.RegisterCallback<NavigationMoveEvent>((evt) => {

    if (evt.direction == NavigationMoveEvent.Direction.Up || evt.direction == NavigationMoveEvent.Direction.Down || evt.direction == NavigationMoveEvent.Direction.Left || evt.direction == NavigationMoveEvent.Direction.Right)
    {
        // Focus logic
        evt.StopPropagation();
        focusController.IgnoreEvent(evt);
    }

}, TrickleDown.TrickleDown);

```

## Example
The following UXML example creates a TextField:
```
<UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
    <TextField label="UXML Field" name="the-uxml-field" value="It's snowing outside." />
</UXML>

```

The following C# example illustrates some of the customizable functionalities of the TextField:
```
/// <sample>
// Get a reference to the field from UXML and append a value to it.
var uxmlField = container.Q<TextField>("the-uxml-field");
uxmlField.value += "..";

// Create a new field, disable it, and give it a style class.
var csharpField = new TextField("C# Field");
csharpField.value = "It's snowing outside...";
csharpField.SetEnabled(false);
csharpField.AddToClassList("some-styled-field");
csharpField.value = uxmlField.value;
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
**C# class** : [`TextField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextField.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : [`TextInputBaseField_1`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1.html)
## Member UXML attributes
This element has the following member attributes:
**Name** | **Type** | **Description**  
---|---|---  
`multiline` | `boolean` | Set this to true to allow multiple lines in the textfield and false if otherwise.  
`value` | `string` | The string currently being exposed by the field.  
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
`value` | `string` | The value associated with the field.  
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
`ussClassName` | `.unity-text-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-text-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-text-field__input` | USS class name of input elements in elements of this type.  
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
## USS custom properties
The following table outlines the custom properties that are available exclusively for the TextField element in USS:
Property | Type | Description  
---|---|---  
`--unity-cursor-color` | string | The color code of the text caret.  
`--unity-selection-color` | string | The color code of the selected text.  
## Additional resources
  * [Work with text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-work-with-text.html)
  * [Label](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Label.html)
  * [DoubleField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-DoubleField.html)
  * [LongField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-LongField.html)
  * [FloatField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-FloatField.html)
  * [IntegerField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-IntegerField.html)
  * [PropertyField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-PropertyField.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TextElement.html)
TextElement
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TemplateContainer.html)
TemplateContainer

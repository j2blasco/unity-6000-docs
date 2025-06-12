* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Foldout.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * Foldout


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-FloatField.html)
FloatField
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-GradientField.html)
GradientField
# Foldout
A Foldout is a collapsible section of a UI. The Foldout hides or reveals the elements it contains when you click its header.
![Foldout](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uxml/foldout.gif) Foldout
## Create a Foldout
A Foldout has the following elements:
  * **Label** : A label you can use as the name of the Foldout.
  * **Toggle** : Click the toggle to expand or collapse the container sub-element. It is styled to look like an arrow rather than the default checkbox. When the container is collapsed, the arrow points right. When the container is expanded, the arrow points down.
  * **Container** : A container contains the **visual elements** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement) that you want to show or hide when you toggle the Foldout.


You can add elements to a Foldout’s container, and the show-or-hide function works automatically. 
The following UI Document creates a Foldout with two buttons in its container. The two buttons show or hide when you toggle the Foldout.
```
<ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements" xsi="http://www.w3.org/2001/XMLSchema-instance" engine="UnityEngine.UIElements" editor="UnityEditor.UIElements" noNamespaceSchemaLocation="../../UIElementsSchema/UIElements.xsd" editor-extension-mode="False">
    <ui:Foldout text="Foldout" name="MyFoldout" value="true">
        <ui:Button text="First item" />
        <ui:Button text="Second item" />
    </ui:Foldout>
</ui:UXML>

```

## Respond to user actions
A Foldout and its Toggle sub-element respond to [Change events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Change-Events.html). The Toggle hides or shows the Foldout container.
You can bind a Foldout to a Boolean variable or access its value through the [`INotifyValueChanged<bool>`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.INotifyValueChanged_1.html) interface.
## Examples
The following C# code snippet creates a Foldout and checks whether the foldout is expanded:
```
// Create a new foldout, add two elements to it and add it to the container
var cSharpFoldout = new Foldout {text = "Elements"};
cSharpFoldout.Add(new Label("Indented Label"));
cSharpFoldout.Add(new Slider("Indented Slider", 0, 100));
container.Add(cSharpFoldout);

cSharpFoldout.RegisterValueChangedCallback(e =>
{
    // Check whether the foldout is expanded
    if (cSharpFoldout.value)
    {
        Debug.Log("Foldout is expanded");
    }
    else
    {
        Debug.Log("Foldout is collapsed");
    }
});

```

## C# base class and namespace
**C# class** : [`Foldout`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Foldout.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : [`BindableElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindableElement.html)
## Member UXML attributes
This element has the following member attributes:
**Name** | **Type** | **Description**  
---|---|---  
`text` | `string` | The label text for the toggle.  
`toggle-on-label-click` | `boolean` | Whether to toggle the foldout state when the user clicks the label.  
`value` | `boolean` | This is the state of the Foldout’s toggle. It is true if the `Foldout` is open and its contents are visible, and false if the Foldout is closed, and its contents are hidden.  
## Inherited UXML attributes
This element inherits the following attributes from its base class:
**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`focusable` | `boolean` | True if the element can be focused.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
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
`ussClassName` | `.unity-foldout` | The USS class name for Foldout elements.  
  
Unity adds this USS class to every instance of a `Foldout`. Any styling applied to this class affects every Foldout located beside, or below the stylesheet in the visual tree.  
`toggleUssClassName` | `.unity-foldout__toggle` | The USS class name of Toggle sub-elements in Foldout elements.  
  
Unity adds this USS class to the `Toggle` sub-element of every `Foldout`. Any styling applied to this class affects every Toggle sub-element located beside, or below the stylesheet in the visual tree.  
`contentUssClassName` | `.unity-foldout__content` | The USS class name for the content element in a Foldout.  
  
Unity adds this USS class to the `VisualElement` that contains the elements to be shown or hidden. Any styling applied to this class affects every foldout container located beside, or below the stylesheet in the visual tree.  
`inputUssClassName` | `.unity-foldout__input` | The USS class name for the Label element in a Foldout.  
  
Unity adds this USS class to the `VisualElement` that contains the `Toggle` input elements. Any styling applied to this class affects every foldout container located beside, or below the stylesheet in the visual tree.  
`checkmarkUssClassName` | `.unity-foldout__checkmark` | The USS class name for the Label element in a Foldout.  
  
Unity adds this USS class to the `VisualElement` that represents the checkmark of the `Toggle` sub-element of every `Foldout`. Any styling applied to this class affects every foldout container located beside, or below the stylesheet in the visual tree.  
`textUssClassName` | `.unity-foldout__text` | The USS class name for the Label element in a Foldout.  
  
Unity adds this USS class to the `Label` in the `Toggle` sub-element of every `Foldout`. Any styling applied to this class affects every foldout container located beside, or below the stylesheet in the visual tree.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
You can also use the [Matching Selectors section in the Inspector or the UI Toolkit Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-testing-ui.html#matching-selectors) to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.
## Additional resource
  * [Change events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Change-Events.html)
  * [Toggle](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Toggle.html)A checkbox that allows the user to switch an option on or off. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Toggle.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toggle)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-FloatField.html)
FloatField
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-GradientField.html)
GradientField

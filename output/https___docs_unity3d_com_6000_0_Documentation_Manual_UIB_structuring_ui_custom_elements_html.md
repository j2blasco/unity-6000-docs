* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-structuring-ui-custom-elements.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Structure UI examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-examples.html)
  * Create a custom control with two attributes


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-conditional-ui.html)
Use Toggle to create a conditional UI
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-slide-toggle.html)
Create a slide toggle custom control
# Create a custom control with two attributes
**Version** : 2023.2+
This example demonstrates how to create a simple custom control with two attributes.
## Example overview
This example creates a custom control called `MyElement` with two attributes and exposes it to UXML and UI Builder. This example also shows how to add a custom control to a UI in the UI Builder.
You can find the completed files that this example creates in this [GitHub repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples/tree/2023.2/create-custom-control-with-custom-attributes).
## Prerequisites
This guide is for developers who are familiar with Unity, UI Toolkit, and C# scripting. Before you start, get familiar with the following:
  * [UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UXML.html)
  * [UI Builder](https://docs.unity3d.com/6000.0/Documentation/Manual/UIBuilder.html)


## Create the example
To create a new custom control class in C#, inherit it from the `VisualElement` class. This allows you to create and use this element in C#, but won’t automatically expose it in UXML and UI Builder. To expose it, add the [`UxmlElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlElementAttribute.html) attribute. To expose the attributes, add the [`UxmlAttribute`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlAttributeAttribute.html) attribute to each property that you want to be visible in UXML and the UI Builder.
  1. Create a Unity project with any template.
  2. In the `Assets` folder, create a C# script named `MyElement.cs` with the following content:

```
using UnityEngine.UIElements;

[UxmlElement]
partial class MyElement : VisualElement
{
    [UxmlAttribute]
    public string myString { get; set; } = "default_value";

    [UxmlAttribute]
    public int myInt { get; set; } = 2;
}

```

## Create a UXML to see the attribute
  1. Create a UXML file with any name you want.
  2. Double-click the UXML file to open it in the UI Builder.
  3. In the **Library** section of the UI Builder, select **Project** > **Custom Controls (C#)** > **MyElement**.
  4. Drag **MyElement** to the Hierarchy window.
  5. To see the custom attributes for **MyElement** , go to the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** tab of **MyElement** :

![Custom attributes for a custom control](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/UIBuilder/CustomElementAttributes.png) Custom attributes for a custom control
## Additional resources
  * [Create custom controls](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-custom-controls.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-conditional-ui.html)
Use Toggle to create a conditional UI
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-slide-toggle.html)
Create a slide toggle custom control

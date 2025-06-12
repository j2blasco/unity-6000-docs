* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/custom-control-attributes-built-in-types.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Custom controls](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-custom-controls.html)
  * Define UXML attributes for built-in types


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/custom-control-customize-uxml-tag-names.html)
Customize the custom control UXML tag name
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/custom-control-attributes-complex-data-types.html)
Define custom control attributes for complex data types
# Define UXML attributes for built-in types
To define UXML attributes for a custom control, add the [`UxmlAttribute`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlAttributeAttribute.html) attribute to the properties that you want to expose in UXML and UI Builder. 
`UxmlAttribute` links fields or properties to UXML attributes. Unity automatically handles the conversion of values to and from UXML attribute strings as needed. Unity provides a set of [built-in converters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlAttributeConverter_1.html) for common types, such as `int`, `float`, `bool`, `string`, and `Vector2`.
By default, UI Toolkit resolves the C# Camel case or Pascal case attribute names into lowercase words connected by hyphens. For example, a property named `MyFloat` or `myFloat` in C# becomes `my-float` in UXML and UI Builder. You can also [customize the UXML attribute names](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/custom-control-customize-uxml-attributes.html#rename-the-uxml-attributes).
The following example creates a custom control with multiple custom attributes:
```
using System;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UIElements;

[UxmlElement]
public partial class ExampleVisualElement : VisualElement
{
    [UxmlAttribute]
    public string myStringValue { get; set; }

    [UxmlAttribute]
    public int myIntValue { get; set; }

    [UxmlAttribute]
    public float myFloatValue { get; set; }

    [UxmlAttribute]
    public List<int> myListOfInts { get; set; }

    [UxmlAttribute, UxmlTypeReference(typeof(VisualElement))]
    public Type myType { get; set; }

    [UxmlAttribute]
    public Texture2D myTexture { get; set; }

    [UxmlAttribute]
    public Color myColor { get; set; }
}


```

The following example UXML document uses the custom control:
```
<ui:UXML xmlns:ui="UnityEngine.UIElements">
    <ExampleElement my-string-value="Hello World" my-int-value="123" />
    <ExampleElement my-float-value="3.14" my-list-of-ints="1,2,3" />
    <ExampleElement my-string-value="Hello World" my-int-value="123" />
    <ExampleElement my-texture="project://database/Assets/MyTexture.png" />
    <ExampleElement my-color="#FF0000FF" />
    <ExampleElement my-type="UnityEngine.UIElements.Button, UnityEngine.UIElementsModule" />
</ui:UXML>

```

## Additional resources
  * [Define UXML attributes for complex data types](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/custom-control-attributes-complex-data-types.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/custom-control-customize-uxml-tag-names.html)
Customize the custom control UXML tag name
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/custom-control-attributes-complex-data-types.html)
Define custom control attributes for complex data types

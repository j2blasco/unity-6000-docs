* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/custom-control-customize-uxml-tag-names.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Custom controls](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-custom-controls.html)
  * Customize the custom control UXML tag name


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-custom-controls.html)
Create a custom control
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/custom-control-attributes-built-in-types.html)
Define UXML attributes for built-in types
# Customize the custom control UXML tag name
By default, the tag name in UXML for your custom control is the C# class name. While it’s not recommended to use a different tag name, you can customize it if needed.
To customize a UXML tag name, add a [`name`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlElementAttribute-name.html) argument to the [`UxmlElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlElementAttribute.html) attribute.
**Note** : The tag name must be unique and you must reference the classes’ namespace in UXML.
For example, if you create the following custom button:
```
using UnityEngine.UIElements;

[UxmlElement("MyButton")]
public partial class CustomButtonElement : Button
{
}

```

You can then reference the custom button in UXML with the custom name or the C# class name:
```
<ui:UXML xmlns:ui="UnityEngine.UIElements">
    <MyButton />
    <CustomButtonElement />
</ui:UXML>

```

## Additional resources
  * [Create custom controls](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-custom-controls.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-custom-controls.html)
Create a custom control
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/custom-control-attributes-built-in-types.html)
Define UXML attributes for built-in types

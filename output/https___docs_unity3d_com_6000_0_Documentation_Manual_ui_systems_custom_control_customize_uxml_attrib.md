* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/custom-control-customize-uxml-attributes.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Custom controls](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-custom-controls.html)
  * Customize UXML attributes


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/custom-control-attributes-complex-data-types.html)
Define custom control attributes for complex data types
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-custom-control-to-data.html)
Bind custom controls to data
# Customize UXML attributes
You can customize the UXML attribute names, the behavior of the attributes, and add decorators and custom **property drawers** A Unity feature that allows you to customize the look of certain controls in the Inspector window by using attributes on your scripts, or by controlling how a specific Serializable class should look [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/editor-PropertyDrawers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PropertyDrawer) in UI Builder.
## Rename the UXML attributes
You can rename a custom control’s attributes through the `name` argument of the [`UxmlAttribute`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlAttributeAttribute.html) attribute.
The following shows an example of a custom control with renamed attributes:
```
using UnityEngine.UIElements;

[UxmlElement]
public partial class CustomAttributeNameExample : VisualElement
{
    [UxmlAttribute("character-name")]
    public string myStringValue { get; set; }

    [UxmlAttribute("credits")]
    public float myFloatValue { get; set; }

    [UxmlAttribute("level")]
    public int myIntValue { get; set; }

    [UxmlAttribute("usage")]
    public UsageHints myEnumValue { get; set; }
}

```

The following shows an example UXML document with the renamed attributes: 
```
<ui:UXML xmlns:ui="UnityEngine.UIElements">
    <CustomAttributeNameExample character-name="Karl" credits="1.23" level="1" usage="DynamicColor" />
</ui:UXML>

```

If you rename an attribute and want UXML files with the old name to remain compatible, add the [`obsoleteNames`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlAttributeAttribute-obsoleteNames.html) argument to the `UxmlAttribute` attribute.
The following example shows how to use the `obsoleteNames` argument:
```
using UnityEngine.UIElements;

[UxmlElement]
public partial class CharacterDetails : VisualElement
{
    [UxmlAttribute("character-name", "npc-name")]
    public string npcName { get; set; }

    [UxmlAttribute("character-health", "health")]
    public float health { get; set; }
}

```

The following shows an example usage in UXML:
```
<ui:UXML xmlns:ui="UnityEngine.UIElements">
    <CharacterDetails npc-name="Haydee" health="100" />
</ui:UXML>

```

## Override the behavior of the UXML attributes
You override the get and set behavior for a UXML attribute of a custom control. This replaces the original attribute with your overridden version in the UI Builder attributes view. To override an attribute, define the new attribute and reference the original one using `[UxmlAttribute("original-attribute-name"), new-attribute]`.
You can use this attribute override to customize attributes inherited from child classes. For example, to enforce value limits in an **IntegerField** , override the value attribute and apply the [Range](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RangeAttribute.html) attribute like this:
```
using UnityEngine;
using UnityEngine.UIElements;

[UxmlElement]
public partial class MyCustomIntField : IntegerField
{
    [UxmlAttribute("value"), Range(0, 100)]
    private int valueOverride
    {
        get => this.value;
        set => this.value = value;
    }
}

```

In this example, the **MyCustomIntField** class inherits from **IntegerField** and overrides the **value** attribute. The **Range** attribute restricts the value to a range between `0` and `100`.
When you add the **MyCustomIntField** in the UI Builder, the overridden version replaces the **value** attribute. This allows you to set the value within the specified range.
## Add attribute decorators in UI Builder
You can add the following decorator attributes on the UXML attribute fields. When you add a decorator attribute, the corresponding UI controls, such as a slider for [`Range`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RangeAttribute.html), are displayed in the UI Builder’s **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) panel:
  * [`TextArea`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAreaAttribute.html)
  * [`Tooltip`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TooltipAttribute.html)
  * [`Range`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RangeAttribute.html)
  * [`Header`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HeaderAttribute.html)
  * [`Min`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MinAttribute.html)
  * [`Multiline`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MultilineAttribute.html)
  * [`Space`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpaceAttribute.html)
  * [`Delayed`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DelayedAttribute.html)


The following example creates a custom control with decorators on its attribute fields:
```
using UnityEngine.UIElements;
using UnityEngine;

[UxmlElement]
public partial class ExampleText : VisualElement
{
    [TextArea, UxmlAttribute]
    public string myText;

    [Header("My Header")]
    [Range(0, 100)]
    [UxmlAttribute]
    public int rangedInt;

    [Tooltip("My custom tooltip")]
    [Min(10)]
    [UxmlAttribute]
    public int minValue = 100;
}

```

The UI Builder displays the attributes with the decorators:
![Attributes with the decorators](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/UIB-decorators.png) Attributes with the decorators
## Add custom property drawer in UI Builder
You can add [custom property drawers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.html) on fields in the UI Builder.
The following example creates a custom control with a custom property drawer:
```
using UnityEngine;
using UnityEngine.UIElements;

public class MyDrawerAttribute : PropertyAttribute { }

[UxmlElement]
public partial class MyDrawerExample : Button
{
    [UxmlAttribute]
    public Color myColor;

    [MyDrawer, UxmlAttribute]
    public string myText;
}

```

To access other serialized properties, prepend the name with `serializedData`. The following code example uses `serializedData.myColor` to find the `myColor` attribute:
```
using UnityEditor;
using UnityEditor.UIElements;
using UnityEngine.UIElements;

[CustomPropertyDrawer(typeof(MyDrawerAttribute))]
public class MyDrawerAttributePropertyDrawer : PropertyDrawer
{
    public override VisualElement CreatePropertyGUI(SerializedProperty property)
    {
        var row = new VisualElement { style = { flexDirection = FlexDirection.Row } };
        var textField = new TextField("My Text") { style = { flexGrow = 1 } };
        var button = new Button { text = ":" };
        button.clicked += () => textField.value = "RESET";

        // Get the parent property
        var parentPropertyPath = property.propertyPath.Substring(0, property.propertyPath.LastIndexOf('.'));
        var parent = property.serializedObject.FindProperty(parentPropertyPath);

        var colorProp = parent.FindPropertyRelative("myColor");
        textField.TrackPropertyValue(colorProp, p =>
        {
            row.style.backgroundColor = p.colorValue;
        });

        row.style.backgroundColor = colorProp.colorValue;
        row.Add(textField);
        row.Add(button);
        textField.BindProperty(property);

        return row;
    }
}

```

The custom property drawer looks like the following:
![Custom property drawer with a color picker](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/UIB-propertydrawer.gif) Custom property drawer with a color picker
## Additional resources
  * [create a custom inventory property drawer](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/example-create-custom-inventory-property-drawer.html)
  * [`PropertyDrawer`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.html)
  * [`DecoratorDrawer`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DecoratorDrawer.html)
  * [`UxmlObjectReferenceAttribute`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlObjectReferenceAttribute.html)
  * [Troubleshooting custom control library compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-troubleshooting-custom-control-library-compilation.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/custom-control-attributes-complex-data-types.html)
Define custom control attributes for complex data types
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-custom-control-to-data.html)
Bind custom controls to data

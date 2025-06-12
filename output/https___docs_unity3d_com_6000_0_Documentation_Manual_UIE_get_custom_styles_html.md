* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-get-custom-styles.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Style UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS.html)
  * [USS custom properties (variables)](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-variables.html)
  * Get custom styles in C# scripts


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uss-built-in-variable-reference.html)
USS built-in variable references
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-apply-styles-with-csharp.html)
Apply styles in C# scripts
# Get custom styles in C# scripts
You can use the [`VisualElement.customStyle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-customStyle.html) property to get the value of a [custom style property (variables)](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-CustomProperties.html) applied to an element. However, you can’t directly query it as you would with [`VisualElement.style`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-style.html) or [`VisualElement.resolvedStyle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-resolvedStyle.html). Instead, do the following:
  1. Register to the [`CustomStyleResolvedEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CustomStyleResolvedEvent.html) event.
  2. Call the [`TryGetValues`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ICustomStyle.TryGetValue.html) method to query the returned object of the `element.customStyle` property.


Assume you have defined a custom style property `--my-custom-color` in USS like this:
```
.my-selector
{
    --my-custom-color: red;
}

```

The following example class shows how to get the value of `--my-custom-color` applied to an element:
```
public class HasCustomStyleElement : VisualElement
{
    // Custom style property definition from code indicating the type and the name of the property.
    private static readonly CustomStyleProperty<Color> s_CustomColor = new ("--my-custom-color");

    private Color customColor { get; set; }

    public HasCustomStyleElement()
    {
        RegisterCallback<CustomStyleResolvedEvent>(OnCustomStyleResolved);
    }

    private void OnCustomStyleResolved(CustomStyleResolvedEvent evt)
    {
        // If the custom style property is resolved for this element, you can query its value through the `customStyle` accessor.
        if (evt.customStyle.TryGetValue(s_CustomColor, out var value))
        {
            customColor = value;
        }
        // Otherwise, put some default value.
        else
        {
            customColor = new Color();
        }
    }
}

```

## Additional resources
  * [Manage UI asset references from C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-manage-asset-reference.html)
  * [Apply styles with C#](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-apply-styles-with-csharp.html)
  * [`customStyle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-customStyle.html)
  * [`CustomStyleResolvedEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CustomStyleResolvedEvent.html)
  * [`TryGetValues`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ICustomStyle.TryGetValue.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uss-built-in-variable-reference.html)
USS built-in variable references
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-apply-styles-with-csharp.html)
Apply styles in C# scripts

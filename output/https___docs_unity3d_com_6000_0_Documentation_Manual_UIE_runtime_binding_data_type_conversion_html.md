* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-data-type-conversion.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-data-binding.html)
  * [Runtime data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding.html)
  * Convert data types


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-mode-update.html)
Define binding mode and update trigger
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-logging-levels.html)
Define logging levels
# Convert data types
You can use type converters to convert data types between the data source and the UI. This allows you to:
  * Bind data types that are different from the UI, such as binding to a `Texture2D` property from an `int` value.
  * Convert data types that are the same as the UI when you want a different representation of the data, such as displaying an angle in degrees instead of radians.


There are two categories of type converters: global converters and per-binding converters. 
## Global converters
Global converters are statically registered and are available to all binding instances, regardless of the binding modes. The binding system provides several pre-registered global converters for convenience, such as converters between style values and their underlying data representation. You can use them to bind a regular `float` or a `StyleKeyword` to a `StyleFloat` property, instead of using `StyleFloat` in the data source.
To register a global converter, use the [`ConverterGroups.RegisterGlobalConverter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroups.RegisterGlobalConverter.html) method. This method requires a delegate to convert a source type to a destination type. The delegate must be a `ref` delegate to enable bidirectional usage. Upon registration, global converters automatically apply to any binding instances requiring that specific type of conversion, without any additional configuration.
The following example registers a global converter that converts between a `Texture2D` and a `TextureHandle`:
```
public struct TextureHandle
{
    public static Texture2D ResolveTexture(TextureHandle handle)
    {
        return /* Actual texture */; 
    } 
    
   public static TextureHandle FromTexture(Texture2D texture)
   {
        return new TextureHandle { handle = /* Compute handle */ }; 
   }

    public int handle;
}

// Registers the global converter
ConverterGroups.RegisterGlobalConverter((ref TextureHandle handle) => TextureHandle.ResolveTexture(handle));
ConverterGroups.RegisterGlobalConverter((ref Texture2D texture) => TextureHandle.FromTexture(texture));

```

## Per-binding converters
Per-binding converters apply to a specific binding instance. You can register an individual or a group of per-binding converters.
### Individual converter
To register an individual converter, use the [`DataBinding.sourceToUiConverters.AddConverter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding-sourceToUiConverters.html) or [`DataBinding.uiToSourceConverters.AddConverter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding-uiToSourceConverters.html) method. These methods require a delegate to convert a source type to a destination type. The delegate must be a `ref` delegate to enable bidirectional usage.
The following example registers and applies individual converters to convert between radians and degrees for a binding instance:
```
var binding = new DataBinding();
binding.sourceToUiConverters.AddConverter((ref float radian) => Mathf.RadToDeg * radian);
binding.uiToSourceConverters.AddConverter((ref float degree) => Mathf.DegToRad * degree);

```

### Group converter
To register a group of converters and apply them to a `DataBinding` instance, use the [`ConverterGroup`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroup.html) class.
The following example shows how to register a group of converters:
```
// Create a converter group
var group = new ConverterGroup("Inverters");

// Add converters to the converter group
group.AddConverter((ref int v) => -v);
group.AddConverter((ref float v) => -v);
group.AddConverter((ref double v) => -v);
// Register the converter group
ConverterGroups.RegisterConverterGroup(group);


// Add a converter to an existing converter group
if (ConverterGroups.TryGetConverterGroup("Inverters", out var group))
{
    group.AddConverter((ref short v) => -v);
}

```

### Apply a converter group
After you have registered a converter group, you can apply it to a binding instance. You can apply a converter group to a binding instance in C#, UI Builder, or UXML.
To apply a converter group in C#, use the [`DataBinding.ApplyConverterGroupToUI`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding.ApplyConverterGroupToUI.html) or [`DataBinding.ApplyConverterGroupToSource`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding.ApplyConverterGroupToSource.html) method. These methods take a converter group name as a parameter. 
The following example applies the converter group `Inverters` to a binding instance in C#:
```
var binding = new DataBinding();
if (ConverterGroups.TryGetConverterGroup("Inverters", out var group))
{
    binding.ApplyConverterGroupToUI(group);
    binding.ApplyConverterGroupToSource(group);
}

```

**Note** : When you apply a converter group onto another one, it operates in a “fire-and-forget” manner. This means that when you apply the converter group, it independently performs its intended function without additional ongoing monitoring or management from you. 
The following example applies the converter group `Inverters` to a binding in UXML:
```
<ui:DataBinding source-to-ui-converters="Inverters" ui-to-source-converters="Inverters" />

```

For details about how to apply a converter group in UI Builder, refer to [Get started with runtime binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-get-started-runtime-binding.html).
## Best practices
Follow these tips and best practices to optimize performance:
  * **Minimize memory allocation** : Whenever possible, avoid writing conversion delegates that allocate memory, particularly when dealing with `enum` types. Allocating memory during conversions can introduce unnecessary overhead and impact performance. Instead, opt for efficient and memory-friendly conversion approaches.
  * **Keep converters efficient** : It’s important to keep converters focused on performing quick and efficient type conversions. Avoid performing extensive tasks or complex operations within converters, as this can lead to decreased performance and potentially introduce unnecessary complexity.
  * **Integrate type conversion in the data source** : Instead of relying solely on per-binding conversions, consider incorporating the type conversion directly into your data source. By handling the conversion within the data source itself, you can streamline the process and potentially improve overall performance. This approach can also reduce the complexity associated with managing conversions on a per-binding basis.


## Known limitations
Source and destination types must match perfectly unless they’re of type `UnityEngine.Object`. For example, you can’t convert an `int` to a `float`, or a `float` to an `int`. This can be inconvenient, especially with `enum` types. This limitation will be addressed in a future release.
## Additional resources
  * [Runtime data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding.html)
  * [Get started with runtime binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-get-started-runtime-binding.html)
  * [Create runtime data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-types.html)
  * [Create custom binding types](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-custom-types.html)
  * [Define a data source](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-define-data-source.html)
  * [Define logging levels](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-logging-levels.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-mode-update.html)
Define binding mode and update trigger
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-logging-levels.html)
Define logging levels

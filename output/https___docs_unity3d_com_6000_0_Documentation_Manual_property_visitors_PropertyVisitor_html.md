* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors-propertyvisitor.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * [Adding functionality to objects at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/properties.html)
  * Use PropertyVisitor to create a property visitor


[](https://docs.unity3d.com/6000.0/Documentation/Manual/property-paths.html)
Property paths
[](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors-low-level-api.html)
Use low-level APIs to create a property visitor
# Use PropertyVisitor to create a property visitor
This example demonstrates how to use the [`PropertyVisitor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.html) base class to create a property visitor. For an equivalent example that uses the [`IPropertyBagVisitor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.IPropertyBagVisitor.html) and [`IPropertyVisitor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.IPropertyVisitor.html) interfaces, refer to [Use low-level APIs to create a property visitor](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors-low-level-api.html).
## Example overview
This example includes step-by-step instructions to create a property visitor that prints the current state of an object to the console. 
Assume you have the following type:
```
public class Data
{
    public string Name = "Henry";
    public Vector2 Vec2 = Vector2.one;
    public List<Color> Colors = new List<Color> { Color.green, Color.red };
    public Dictionary<int, string> Dict = new Dictionary<int, string> {{5, "zero"}};
}

```

Create a utility method `DebugUtilities` like this:
```
public static class DebugUtilities
{
    public static void PrintObjectDump<T>(T value)
    {
        // Magic goes here.
    }
}

```

Call the `PrintObjectDump` method with the `Data` object like this:
```
DebugUtilities.PrintObjectDump(new Data());

```

Would print the following to the console:
```
- Name {string} = Henry
- Vec2 {Vector2} = (1.00, 1.00)
- Colors {List<Color>}
  - [0] = {Color} RGBA(0.000, 1.000, 0.000, 1.000)
  - [1] = {Color} RGBA(1.000, 0.000, 0.000, 1.000)
- Dict {Dictionary<int, string>}
  - [5] {KeyValuePair<int, string>}
    - Key {int} = 5
    - Value {string} = five

```

## Create the visitor
First, create a `DumpObjectVisitor` class. Inside the class, use a [StringBuilder](https://learn.microsoft.com/en-us/dotnet/api/system.text.stringbuilder?view=net-7.0) to build a string that represents the current state of an object.
  1. Create a `DumpObjectVisitor` class that inherits from [`PropertyVisitor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.html).
  2. Add a `StringBuilder` field to the class.
  3. Add a `Reset` method that clears the `StringBuilder` and resets the indent level.
  4. Add a `GetDump` method that returns the string representation of the current state of an object.
Your finished class looks like this:
```
// `PropertyVisitor` is an abstract class that you must subclass from it. 
public class DumpObjectVisitor: PropertyVisitor
{
    private const int k_InitialIndent = 0;
    private readonly StringBuilder m_Builder = new StringBuilder();
        
    private int m_IndentLevel = k_InitialIndent;
        
    private string Indent => new (' ', m_IndentLevel * 2);
        
    public void Reset()
    {
        m_Builder.Clear();
        m_IndentLevel = k_InitialIndent;
    }

    public string GetDump()
    {
        return m_Builder.ToString();
    }
}

```



## Get the top-level properties
Inside the `DumpObjectVisitor` class, override the [`VisitProperty`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.VisitProperty.html) method to visit each property of an object and log the property name. The [`PropertyVisitor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.html) doesn’t require any members to implement and by default, it simply visits every property and performs no action.
  1. Inside the `DumpObjectVisitor` class, add the following override `VisitProperty` method:
```
protected override void VisitProperty<TContainer, TValue>(Property<TContainer, TValue> property, ref TContainer container, ref TValue value)
{
    m_Builder.AppendLine($"- {property.Name}");
}

```

  2. Now that you have a minimal visitor, you can implement the utility method. Update the `PrintObjectDump` method in the `DebugUtilities` class to create a new `DumpObjectVisitor` instance and use it to visit the properties of the given object:
```
public static class DebugUtilities
{
    private static readonly DumpObjectVisitor s_Visitor = new ();
        
    public static void PrintObjectDump<T>(T value)
    {
        s_Visitor.Reset();
            
        // This is the main entry point to run a visitor.
        PropertyContainer.Accept(s_Visitor, ref value);
        Debug.Log(s_Visitor.GetDump());
    }
}

```

This gets the following output:
```
- Name
- Vec2
- Colors
- Dict

```



## Get the sub-properties
The output from the previous section indicates that when you override the [`VisitProperty`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.VisitProperty.html) method, it doesn’t automatically visit the sub-properties of an object. To get the sub-properties, use the [`PropertyContainer.Accept`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyContainer.Accept.html) method to apply the visitor on each of the values recursively.
  * Inside the `DebugUtilities` class, update the `VisitProperty` method to apply the visitor recursively on the value to nest in:
```
protected override void VisitProperty<TContainer, TValue>(Property<TContainer, TValue> property, ref TContainer container, ref TValue value)
{
    m_Builder.AppendLine($"{Indent}- {property.Name}");
        
    ++m_IdentLevel;
    // Apply this visitor recursively on the value to nest in.
    if (null != value)
        PropertyContainer.Accept(this, ref value);
    --m_IdentLevel;
}

```

This gets the following output:
```
- Name
- Vec2
- x
- y
- Colors
- 0
    - r
    - g
    - b
    - a
- 1
    - r
    - g
    - b
    - a 
- Dict
- 5
    - Key
    - Value

```



## Display more details about each property
Next, let’s get the property name of collection items, and the type and value of each property.
Certain properties have special names, especially when dealing with collection items. Here are the conventions for property names:
  * For list items, the name corresponds to the index.
  * For dictionaries, the name is derived from the string version of the key value.
  * For sets, the name is based on the string version of the value.


To make this distinction more explicit, encase the property name with square brackets.
  1. Inside the `DumpObjectVisitor` class, add the following method:
```
private static string GetPropertyName(IProperty property)
{
    return property switch
    {
        // You can also treat `IListElementProperty`, `IDictionaryElementProperty`, and `ISetElementProperty` separately.
        ICollectionElementProperty => $"[{property.Name}]",
        _ => property.Name
    };
}

```

  2. Update the `VisitProperty` method to use [`TypeUtility.GetTypeDisplayName`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.TypeUtility.GetTypeDisplayName.html) to retrieve the display name of a given type. 
```
protected override void VisitProperty<TContainer, TValue>(Property<TContainer, TValue> property, ref TContainer container, ref TValue value)
{
    var propertyName = GetPropertyName(property);
        
    // Get the concrete type of the property or its declared type if value is null.
    var typeName = TypeUtility.GetTypeDisplayName(value?.GetType() ?? property.DeclaredValueType());
        
    m_Builder.AppendLine($"{Indent}- {propertyName} = {{{typeName}}} {value}");
        
    ++m_IndentLevel;
    if (null != value)
        PropertyContainer.Accept(this, ref value);
    --m_IndentLevel;
}

```

This gets the following output:
```
- Name = {string} Henry
- Vec2 = {Vector2} (1.00, 1.00)
- x = {float} 1
- y = {float} 1
- Colors = {List<Color>} System.Collections.Generic.List`1[UnityEngine.Color]
- [1] = {Color} RGBA(0.000, 1.000, 0.000, 1.000)
    - r = {float} 0
    - g = {float} 1
    - b = {float} 0
    - a = {float} 1
- [1] = {Color} RGBA(1.000, 0.000, 0.000, 1.000)
    - r = {float} 1
    - g = {float} 0
    - b = {float} 0
    - a = {float} 1
- Dict = {Dictionary<int, string>} System.Collections.Generic.Dictionary`2[System.Int32,System.String]
- [5] = {KeyValuePair<int, string>} [5, five]
    - Key = {int} 5
    - Value = {string} five

```



## Reduce the amount of information displayed for collection types
Because `List<T>` doesn’t override the `ToString()` method, the list value is displayed as `System.Collections.Generic.List1[UnityEngine.Color]`. To reduce the amount of information displayed, update the `VisitProperty` to use the [`TypeTraits.IsContainer`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.TypeTraits.IsContainer.html) utility method to only display the value for types that don’t contain sub-properties, such as primitives, enums and strings.
Inside the `DumpObjectVisitor` class, update the `VisitProperty` method to use [`TypeTraits.IsContainer`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.TypeTraits.IsContainer.html) to determine whether the value is a container type. If it is, display the type name without the value. Otherwise, display the type name and the value.
```
protected override void VisitProperty<TContainer, TValue>(Property<TContainer, TValue> property, ref TContainer container, ref TValue value)
{
    var propertyName = GetPropertyName(property);

    var type = value?.GetType() ?? property.DeclaredValueType();
    var typeName = TypeUtility.GetTypeDisplayName(type);
    
    // Only display the values for primitives, enums and strings.
    if (TypeTraits.IsContainer(type))
        m_Builder.AppendLine($"{Indent}- {propertyName} {{{typeName}}}");
    else
        m_Builder.AppendLine($"{Indent}- {propertyName} = {{{typeName}}} {value}");
    
    ++m_IndentLevel;
    if (null != value)
        PropertyContainer.Accept(this, ref value);
    --m_IndentLevel;
}

```

This gets the following output:
```
- Name = {string} Henry
- Vec2 {Vector2}
- x = {float} 1
- y = {float} 1
- Colors {List<Color>}
- [0] {Color}
    - r = {float} 0
    - g = {float} 1
    - b = {float} 0
    - a = {float} 1
- [1] {Color}
    - r = {float} 1
    - g = {float} 0
    - b = {float} 0
    - a = {float} 1
- Dict {Dictionary<int, string>}
- [5] {KeyValuePair<int, string>}
    - Key = {int} 5
    - Value = {string} five

```

**Tip** :
To reduce the amount of information displayed, you can also use the following methods to override a `Visit` specialization for the collection types:
```
protected override void VisitCollection<TContainer, TCollection, TElement>(Property<TContainer, TCollection> property, ref TContainer container, ref TCollection value) {}
protected override void VisitList<TContainer, TList, TElement>(Property<TContainer, TList> property, ref TContainer container, ref TList value) {}
protected override void VisitDictionary<TContainer, TDictionary, TKey, TValue>(Property<TContainer, TDictionary> property, ref TContainer container, ref TDictionary value) {}
protected override void VisitSet<TContainer, TSet, TValue>(Property<TContainer, TSet> property, ref TContainer container, ref TSet value) {}

```

These are similar to the [`VisitProperty`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.VisitProperty.html) method, but they expose the generic parameters of their respective collections types.
## Add per-type overrides
Lastly, add per-type overrides to display [`Vector2`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.Vector2.html) and [`Color`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.Color.html) types in a more compact manner. 
Use [`PropertyVisitor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.html) along with [`IVisitPropertyAdapter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.IVisitPropertyAdapter.html). Whenever an adapter is registered for a given type, if the targeted type is encountered during the visitation, the adapter is called instead of the [`VisitProperty`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.VisitProperty.html) method:
Inside the `DumpObjectVisitor` class, add the `IVisitPropertyAdapter` for `Vector2` and `Color`:
```
public class DumpObjectVisitor
    : PropertyVisitor
    , IVisitPropertyAdapter<Vector2>
    , IVisitPropertyAdapter<Color>
{
    public DumpObjectVisitor()
    {
        AddAdapter(this);
    }
    
    void IVisitPropertyAdapter<Vector2>.Visit<TContainer>(in VisitContext<TContainer, Vector2> context, ref TContainer container, ref Vector2 value)
    {
        var propertyName = GetPropertyName(context.Property);
        m_Builder.AppendLine($"{Indent}- {propertyName} = {{{nameof(Vector2)}}} {value}");
    }

    void IVisitPropertyAdapter<Color>.Visit<TContainer>(in VisitContext<TContainer, Color> context, ref TContainer container, ref Color value)
    {
        var propertyName = GetPropertyName(context.Property);
        m_Builder.AppendLine($"{Indent}- {propertyName} = {{{nameof(Color)}}} {value}");
    }
}

```

The completed `DumpObjectVisitor` class looks like this:
```
public class DumpObjectVisitor
: PropertyVisitor
, IVisitPropertyAdapter<Vector2>
, IVisitPropertyAdapter<Color> 
{
    private const int k_InitialIndent = 0;
    
    // StringBuilder to store the dumped object's properties and values.
    private readonly StringBuilder m_Builder = new StringBuilder();
    private int m_IndentLevel = k_InitialIndent;
    
    // Helper property to get the current indentation.
    private string Indent => new (' ', m_IndentLevel * 2);

    public DumpObjectVisitor()
    {
        // Constructor, it initializes the DumpObjectVisitor and adds itself as an adapter
        // to handle properties of type Vector2 and Color.
        AddAdapter(this);
    }
    
    // Reset the visitor, clearing the StringBuilder and setting indentation to initial level.
    public void Reset()
    {
        m_Builder.Clear();
        m_IndentLevel = k_InitialIndent;
    }

    // Get the string representation of the dumped object.
    public string GetDump()
    {
        return m_Builder.ToString();
    }

    // Helper method to get the property name, handling collections and other property types.
    private static string GetPropertyName(IProperty property)
    {
        return property switch
        {
            // If it's a collection element property, display it with brackets
            ICollectionElementProperty => $"[{property.Name}]",
            // For other property types, display the name as it is
            _ => property.Name
        };
    }

    // This method is called when visiting each property of an object.
    // It determines the type of the value and formats it accordingly for display.
    protected override void VisitProperty<TContainer, TValue>(Property<TContainer, TValue> property, ref TContainer container, ref TValue value)
    {
        var propertyName = GetPropertyName(property);

        // Get the type of the value or property.
        var type = value?.GetType() ?? property.DeclaredValueType();
        var typeName = TypeUtility.GetTypeDisplayName(type);
        
        // Only display the values for primitives, enums, and strings, and treat other types as containers.
        if (TypeTraits.IsContainer(type))
            m_Builder.AppendLine($"{Indent}- {propertyName} {{{typeName}}}");
        else
            m_Builder.AppendLine($"{Indent}- {propertyName} = {{{typeName}}} {value}");
        
        // Increase indentation level before visiting child properties (if any).
        ++m_IndentLevel;
        if (null != value)
            PropertyContainer.Accept(this, ref value);
        // Decrease indentation level after visiting child properties.
        --m_IndentLevel;
    }

    // This method is a specialized override for Vector2 properties.
    // It displays the property name and its value as a Vector2.
    void IVisitPropertyAdapter<Vector2>.Visit<TContainer>(in VisitContext<TContainer, Vector2> context, ref TContainer container, ref Vector2 value)
    {
        var propertyName = GetPropertyName(context.Property);
        m_Builder.AppendLine($"{Indent}- {propertyName} = {{{nameof(Vector2)}}} {value}");
    }

    // This method is a specialized override for Color properties.
    // It displays the property name and its value as a Color.
    void IVisitPropertyAdapter<Color>.Visit<TContainer>(in VisitContext<TContainer, Color> context, ref TContainer container, ref Color value)
    {
        var propertyName = GetPropertyName(context.Property);
        m_Builder.AppendLine($"{Indent}- {propertyName} = {{{nameof(Color)}}} {value}");
    }
}

```

## Print the current state of a sub-properties
When you run a visitor on data, by default, it starts the visitation on the given object directly. For any property visitor, to start the visitation on sub-properties of an object, pass a [`PropertyPath`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html) to the [`PropertyContainer.Accept`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyContainer.Accept.html) method. 
  1. Update the `DebugUtilities` method to take an optional `PropertyPath`:
```
public static class DebugUtilities
{
    private static readonly DumpObjectVisitor s_Visitor = new();

    public static void PrintObjectDump<T>(T value, PropertyPath path = default)
    {
        s_Visitor.Reset();
        if (path.IsEmpty)
            PropertyContainer.Accept(s_Visitor, ref value);
        else
            PropertyContainer.Accept(s_Visitor, ref value, path);
        Debug.Log(s_Visitor.GetDump());
    }
}

```

  2. Call the `PrintObjectDump` method with the `Data` object. This gets the [desired output](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors-propertyvisitor.html#desired-output).


## Additional resources
  * [Property visitors](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors.html)
  * [Property bags](https://docs.unity3d.com/6000.0/Documentation/Manual/property-bags.html)
  * [Property paths](https://docs.unity3d.com/6000.0/Documentation/Manual/property-paths.html)
  * [Use low-level APIs to create a property visitor](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors-low-level-api.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/property-paths.html)
Property paths
[](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors-low-level-api.html)
Use low-level APIs to create a property visitor

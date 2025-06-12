* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors-low-level-api.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Object-oriented development](https://docs.unity3d.com/6000.0/Documentation/Manual/object-oriented-development.html)
  * [Adding functionality to objects at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/properties.html)
  * Use low-level APIs to create a property visitor


[](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors-propertyvisitor.html)
Use PropertyVisitor to create a property visitor
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-vectors.html)
Moving objects with vectors
# Use low-level APIs to create a property visitor
This example demonstrates how to use the low-level APIs with the [`IPropertyBagVisitor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.IPropertyBagVisitor.html) and [`IPropertyVisitor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.IPropertyVisitor.html) interfaces to create a property visitor. This example is equivalent to the [example](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors-PropertyVisitor.html) that uses the [`PropertyVisitor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.html) base class to create a property visitor.
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
First, create a `DumpObjectVisitor` class that implements the `IPropertyBagVisitor`. Inside the class, use a [StringBuilder](https://learn.microsoft.com/en-us/dotnet/api/system.text.stringbuilder?view=net-7.0) to build a string that represents the current state of an object.
  1. Create a `DumpObjectVisitor` class that implements the `IPropertyBagVisitor` interfaces.
  2. Add a `StringBuilder` field to the class.
  3. Add a `Reset` method that clears the `StringBuilder` and resets the indent level.
  4. Add a `GetDump` method that returns the string representation of the current state of an object.
Your `DumpObjectVisitor` class looks like this:
```
public class DumpObjectVisitor
    : IPropertyBagVisitor
    , IPropertyVisitor
{
    private const int k_InitialIndent = 0;

    private readonly StringBuilder m_Builder = new StringBuilder();
    private int m_IndentLevel = k_InitialIndent;

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



## Get the properties
Inside the `DumpObjectVisitor` class, override the [`IPropertyBagVisitor.Visit`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.IPropertyBagVisitor.Visit.html) method to loop through the properties of the container object. In the object dump visitor, display the values and delegate the visitation to the properties. 
To call the [`Accept`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.Property_2.Accept.html) method on the property using `this`, implement the [`IPropertyVisitor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.IPropertyVisitor.html) interface. This interface allows you to specify the visitation behavior when visiting a property, similar to the [`VisitProperty`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.VisitProperty.html) method of the [`PropertyVisitor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.html) class.
  1. Inside the `DumpObjectVisitor` class, add override the `IPropertyBagVisitor.Visit` and `IPropertyVisitor.Visit` methods.
```
void IPropertyBagVisitor.Visit<TContainer>(IPropertyBag<TContainer> propertyBag, ref TContainer container)
{
    foreach (var property in propertyBag.GetProperties(ref container))
    {
        property.Accept(this, ref container);
    }
}
        
void IPropertyVisitor.Visit<TContainer, TValue>(Property<TContainer, TValue> property, ref TContainer container)
{
    var value = property.GetValue(ref container);
    // Code goes here.
}

```

  2. The `IVisitPropertyAdapter` adapters used with the [`PropertyVisitor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyVisitor.html) base class require access to the internal state of the visitor, so they can’t be used outside of that class. However, you can define domain-specific adapters that have the necessary information. Inside the `DumpObjectVisito` class, update the implementation of the [`IPropertyVisitor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.IPropertyVisitor.html) to use the adapter first:
```
// Create the following methods to encapsulate the formatting of the message and display the value.
public readonly struct PrintContext
{
    private StringBuilder Builder { get; }
    private string Prefix { get; }
    public string PropertyName { get; }

    public void Print<T>(T value)
    {
        Builder.AppendLine($"{Prefix}- {PropertyName} = {{{TypeUtility.GetTypeDisplayName(value?.GetType() ?? typeof(T))}}} {value}");
    }
        
    public void Print(Type type, string value)
    {
        Builder.AppendLine($"{Prefix}- {PropertyName} = {{{TypeUtility.GetTypeDisplayName(type)}}} {value}");
    }

    public PrintContext(StringBuilder builder, string prefix, string propertyName)
    {
        Builder = builder;
        Prefix = prefix;
        PropertyName = propertyName;
    }
}

public interface IPrintValue
{
}

public interface IPrintValue<in T> : IPrintValue
{
    void PrintValue(in PrintContext context, T value);
}

public class DumpObjectVisitor
    : IPropertyBagVisitor
    , IPropertyVisitor
    , IPrintValue<Vector2>
    , IPrintValue<Color>
{
    public IPrintValue Adapter { get; set; }
        
    public DumpObjectVisitor()
    {
        // For simplicity
        Adapter = this;
    }
    void IPropertyVisitor.Visit<TContainer, TValue>(Property<TContainer, TValue> property, ref TContainer container)
    {
        // Here, we need to manually extract the value.
        var value = property.GetValue(ref container);
        
        var propertyName = GetPropertyName(property);
        
        // We can still use adapters, but we must manually dispatch the calls. 
        if (Adapter is IPrintValue<TValue> adapter)
        {
            var context = new PrintContext(m_Builder, Indent, propertyName);
            adapter.PrintValue(context, value);
            return;
        }
            
        // Fallback behaviour here 
    }
        
    void IPrintValue<Vector2>.PrintValue(in PrintContext context, Vector2 value)
    {
        context.Print(value);
    }
    void IPrintValue<Color>.PrintValue(in PrintContext context, Color value)
    {
        const string format = "F3";
        var formatProvider = CultureInfo.InvariantCulture.NumberFormat;
        context.Print(typeof(Color), $"RGBA({value.r.ToString(format, formatProvider)}, {value.g.ToString(format, formatProvider)}, {value.b.ToString(format, formatProvider)}, {value.a.ToString(format, formatProvider)})");
    }
}

```



The completed code looks like this:
```
public readonly struct PrintContext
{
    // A context struct to hold information about how to print the property
    private StringBuilder Builder { get; }
    private string Prefix { get; }
    public string PropertyName { get; }

    // Method to print the value of type T with its associated property name
    public void Print<T>(T value)
    {
        Builder.AppendLine($"{Prefix}- {PropertyName} = {{{TypeUtility.GetTypeDisplayName(value?.GetType() ?? typeof(T))}}} {value}");
    }

    // Method to print the value with a specified type and its associated property name
    public void Print(Type type, string value)
    {
        Builder.AppendLine($"{Prefix}- {PropertyName} = {{{TypeUtility.GetTypeDisplayName(type)}}} {value}");
    }

    // Constructor to initialize the PrintContext
    public PrintContext(StringBuilder builder, string prefix, string propertyName)
    {
        Builder = builder;
        Prefix = prefix;
        PropertyName = propertyName;
    }
}

// Generic interface IPrintValue that acts as a marker interface for all print value adapters
public interface IPrintValue
{
}

// Generic interface IPrintValue<T> to define how to print values of type T
// This interface is used as an adapter for specific types (Vector2 and Color in this case)
public interface IPrintValue<in T> : IPrintValue
{
    void PrintValue(in PrintContext context, T value);
}

// DumpObjectVisitor class that implements various interfaces for property visiting and value printing
private class DumpObjectVisitor : IPropertyBagVisitor, IPropertyVisitor, IPrintValue<Vector2>, IPrintValue<Color>
{
    // (Other members are omitted for brevity)

    public IPrintValue Adapter { get; set; }

    public DumpObjectVisitor()
    {
        // The Adapter property is set to this instance of DumpObjectVisitor
        // This means the current DumpObjectVisitor can be used as a print value adapter for Vector2 and Color.
        Adapter = this;
    }

    // This method is called when visiting a property bag (a collection of properties)
    void IPropertyBagVisitor.Visit<TContainer>(IPropertyBag<TContainer> propertyBag, ref TContainer container)
    {
        foreach (var property in propertyBag.GetProperties(ref container))
        {
            // Call the Visit method of IPropertyVisitor to handle individual properties
            property.Accept(this, ref container);
        }
    }

    // This method is called when visiting each individual property of an object.
    // It tries to find a suitable adapter (IPrintValue<T>) for the property value type (TValue) and uses it to print the value.
    // If no suitable adapter is found, it falls back to displaying the value using its type name.
    void IPropertyVisitor.Visit<TContainer, TValue>(Property<TContainer, TValue> property, ref TContainer container)
    {
        // Here, we need to manually extract the value.
        var value = property.GetValue(ref container);

        var propertyName = GetPropertyName(property);

        // We can still use adapters, but we must manually dispatch the calls.
        // Try to find an adapter for the current property value type (TValue).
        if (Adapter is IPrintValue<TValue> adapter)
        {
            // If an adapter is found, create a print context and call the PrintValue method of the adapter.
            var context = new PrintContext(m_Builder, Indent, propertyName);
            adapter.PrintValue(context, value);
            return;
        }

        // Fallback behavior here - if no adapter is found, handle printing based on type information.
        var type = value?.GetType() ?? property.DeclaredValueType();
        var typeName = TypeUtility.GetTypeDisplayName(type);

        if (TypeTraits.IsContainer(type))
            m_Builder.AppendLine($"{Indent}- {propertyName} {{{typeName}}}");
        else
            m_Builder.AppendLine($"{Indent}- {propertyName} = {{{typeName}}} {value}");

        // Recursively visit child properties (if any).
        ++m_IndentLevel;
        if (null != value)
            PropertyContainer.Accept(this, ref value);
        --m_IndentLevel;
    }

    // Method from IPrintValue<Vector2> used to print Vector2 values
    void IPrintValue<Vector2>.PrintValue(in PrintContext context, Vector2 value)
    {
        // Simply use the Print method of PrintContext to print the Vector2 value.
        context.Print(value);
    }

    // Method from IPrintValue<Color> used to print Color values
    void IPrintValue<Color>.PrintValue(in PrintContext context, Color value)
    {
        const string format = "F3";
        var formatProvider = CultureInfo.InvariantCulture.NumberFormat;
        
        // Format and print the Color value in RGBA format.
        context.Print(typeof(Color), $"RGBA({value.r.ToString(format, formatProvider)}, {value.g.ToString(format, formatProvider)}, {value.b.ToString(format, formatProvider)}, {value.a.ToString(format, formatProvider)})");
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

  2. Call the `PrintObjectDump` method with the `Data` object. This gets the [desired output](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors-low-level-api.html#desired-output).


## Additional resources
  * [Property visitors](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors.html)
  * [Property bags](https://docs.unity3d.com/6000.0/Documentation/Manual/property-bags.html)
  * [Property paths](https://docs.unity3d.com/6000.0/Documentation/Manual/property-paths.html)
  * [Use `PropertyVisitor` to create a property visitor](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors-PropertyVisitor.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/property-visitors-propertyvisitor.html)
Use PropertyVisitor to create a property visitor
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-vectors.html)
Moving objects with vectors

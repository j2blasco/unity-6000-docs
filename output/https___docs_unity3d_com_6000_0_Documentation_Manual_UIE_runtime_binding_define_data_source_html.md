* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-define-data-source.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-data-binding.html)
  * [Runtime data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding.html)
  * Define a data source for runtime binding


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-types.html)
Create a runtime binding in C# scripts
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-mode-update.html)
Define binding mode and update trigger
# Define a data source for runtime binding
When you create a binding object, you must define a data source. The data source is the object that contains the property you want to bind to. You can use any C# object as the runtime binding data source. 
To enable the binding system to access the data source, you must define the `dataSource` property of the binding object to the data source object. For example, if you have a data source object and a UI element like this:
```
using UnityEngine;
using UnityEngine.UIElements;
using Unity.Properties;

public class DataSource
{
    public Vector3 vector3 { get; set; } 
}

var element = new VisualElement();

```

You can then define the `element.dataSource` property to the data source object as follows:
```
element.dataSource = new DataSource();

```

This enables the bindings applied to the element to have access to the `DataSource` object.
To enable the binding applied to the element to have access to the `vector3` field of the `DataSource` object, add the following:
```
element.dataSourcePath = PropertyPath.FromName(nameof(DataSource.vector3));

```

To enable bindings applied to a child element to have access to the `vector3` field of the `DataSource` object, add the following:
```
var child = new VisualElement();
child.dataSourcePath = PropertyPath.FromName(nameof(DataSource.vector3));
element.Add(child)

```

## Property bags
UI Toolkit uses the [`Unity.Properties`](https://docs.unity3d.com/6000.0/Documentation/Manual/properties.html) module to create [property bags](https://docs.unity3d.com/6000.0/Documentation/Manual/property-bags.html) for binding data between two objects. It generates the property bags based on the available C# type information. However, for certain built-in Unity types, the generated property bag might not contain the expected properties. This can occur when these types lack the necessary attributes. For example, the `Rect` type has public properties and private fields that aren’t attributed with `[SerializeField]`, or you define the fields on the native side, which can’t be determined at runtime.
**Note** : When you use a value type as a data source, there is a boxing cost due to the [`VisualElement.dataSource`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-dataSource.html) being defined as an object property. It means that you must box the value type before assigning it to the `dataSource` property. The boxing operation introduces the overhead of memory allocation and copying, resulting in a performance cost. This performance impact may not be significant for small data sets or occasional use. However, in performance-critical scenarios or when you deal with large amounts of data, the boxing cost can become a concern.
To define a data source for runtime bindings and also for authoring or serializing purposes, use a common pattern as shown below:
```
using UnityEngine;
using Unity.Properties;

public class MyBehaviour : MonoBehaviour
{
    // Serializations go through the field. 
    [SerializeField, DontCreateProperty] 
    private int m_Value;
    
    // Bindings go through the property rather than the field. 
    // This allows you to do validation, notify changes, and more.
    [CreateProperty] 
    public int value
    {
        get => m_Value;
        set => m_Value = value;
    }
    
    // This is a similar example, but for an auto-property.
    [field: SerializeField, DontCreateProperty]
    [CreateProperty]
    public float floatValue { get; set; }
}

```

**Note** : These bindable properties inherently possess polymorphic characteristics.
## Integrate versioning and change tracking
To enhance performance, you can integrate versioning and change tracking into a binding data source. By default, the binding system continuously polls the data source and updates the UI on every modification, without knowing if anything has actually changed since the last update. While this approach is convenient for simple projects, it doesn’t scale efficiently when it deals with numerous bindings.
Versioning and change tracking for sources are optional features that require deliberate activation. By default, active binding objects are updated every frame, which can be a resource-intensive process. To minimize processing overhead, there are two interfaces you can implement to instruct the binding system on when to update bindings associated with a source:
  * The `IDataSourceViewHashProvider` interface offers a view hash code to indicate when to update all bindings linked to the source.
  * The `INotifyBindablePropertyChanged` interface enables per-property change notifications to trigger updates only for individual bindings related to the modified property.


You can implement these interfaces separately or together for greater control.
**Note** : Currently, types that implement either interface automatically opt-in to code generation when the assembly is tagged with `[assembly: Unity.Properties.GeneratePropertyBagsForAssembly]`. However, this behavior is subject to change.
### Implement `IDataSourceViewHashProvider`
To provide a view hash code for a specific source, implement the [`IDataSourceViewHashProvider`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IDataSourceViewHashProvider.html) interface. This interface enables the binding system to skip updating certain binding objects if the source hasn’t changed since the last update.
The following example creates a data source that reports changes immediately:
```
using UnityEngine.UIElements;

public class DataSource : IDataSourceViewHashProvider
{
    public int intValue;
    public float floatValue;

    // Determines if the data source has changed. If the hash code is different, then the data source
    // has changed and the bindings are updated.
    public long  GetViewHashCode()
    {
        return HashCode.Combine(intValue, floatValue);
    }
}

```

The `IDataSourceViewHashProvider` interface also buffers changes. This buffering capability is particularly useful when the data change frequently, but the UI doesn’t need to immediately reflect every change.
To buffer changes, implement the [`IDataSourceViewHashProvider`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IDataSourceViewHashProvider.html) interface and call the `CommitChanges` method when you want to notify the binding system that the data source has changed.
By default, the binding system doesn’t update a binding object if the version of its data source remains unchanged. However, binding objects might still be updated even if the version didn’t change if you call its `MarkDirty` method or set the `updateTrigger` to `BindingUpdateTrigger.EveryFrame`. When you use `IDataSourceViewHashProvider` to buffer changes, avoid any structural changes in your source, such as adding or removing items from a list, or changing the type of a sub-field or sub-property.
The following example creates a data source that buffers changes:
```
using UnityEngine.UIElements;

public class DataSource : IDataSourceViewHashProvider
{
    private long m_Version;

    public int intValue;
    
    public void CommitChanges()
    {
        ++m_Version;
    }
    
    // Required by IDataSourceViewHashProvider
    public long  GetViewHashCode()
    {
        return m_Version;
    }
}

```

### Implement `INotifyBindablePropertyChanged`
To notify the binding system about specific property changes, implement the [`INotifyBindablePropertyChanged`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.INotifyBindablePropertyChanged.html) interface. When you implement this interface, the binding system updates only the relevant bindings when a change is detected along the property path. For example, if a change is signaled for the `MyAwesomeObject` property, the binding system updates all bindings associated with data source paths that have the `MyAwesomeObject` prefix. Other binding objects tied to the source remain unaffected.
This approach enables highly efficient updates to the UI because the binding system performs minimal work.
The following example creates a data source that notifies changes per property:
```
using System.Runtime.CompilerServices;
using Unity.Properties;
using UnityEngine.UIElements;

public class DataSource : INotifyBindablePropertyChanged
{
    private int m_Value;
    
    // Required by INotifyBindablePropertyChanged
    public event EventHandler<BindablePropertyChangedEventArgs> propertyChanged;

    [CreateProperty]
    public int value
    {
        get => m_Value;
        set
        {
            if (m_Value == value)
                return;

            m_Value = value;
            Notify();
        }
    }

    void Notify([CallerMemberName] string property = "")
    {
        propertyChanged?.Invoke(this, new BindablePropertyChangedEventArgs(property));
    }
}

```

**Note** : When you implement the `INotifyBindablePropertyChanged` interface, the binding system doesn’t perform checks when it gets notified of a change. Failure to report a change means that the binding system doesn’t update bindings related to that property. Therefore, ensure that you report changes only when necessary.
### Implement `IDataSourceViewHashProvider` and `INotifyBindablePropertyChanged`
To achieve optimal binding performance, implement both the `IDataSourceViewHashProvider` and `INotifyBindablePropertyChanged` interfaces. The binding system tracks changed properties until the view’s hash code changes. At that point, it efficiently updates only the affected bindings tied to the changed properties.
This requires additional boilerplate code but provides maximum flexibility and performance benefits.
The following example creates a data source that implements both interfaces. The data source notifies the binding system when a change occurs. However, instead of immediately updating the bindings, the updates are held until the `Publish()` method is called. This approach is particularly useful when you deal with highly volatile data, where updating the UI every frame incurs performance costs.
```
using System;
using System.Runtime.CompilerServices;
using Unity.Properties;
using UnityEngine.UIElements;

public class DataSource : IDataSourceViewHashProvider, INotifyBindablePropertyChanged
{
    private long m_ViewVersion;
    private int m_Value;
    private int m_OtherValue;
    public event EventHandler<BindablePropertyChangedEventArgs> propertyChanged;
    [CreateProperty]
    public int value
    {
        get => m_Value;
        set
        {
            if (m_Value == value)
                return;
            m_Value = value;
            Notify();
        }
    }
    [CreateProperty]
    public int otherValue
    {
        get => m_OtherValue;
        set
        {
            if (m_OtherValue == value)
                return;
            m_OtherValue = value;
            Notify();
        }
    }
    public void Publish()
    {
        ++m_ViewVersion;
    }
    public long GetViewHashCode()
    {
        return m_ViewVersion;
    }
    void Notify([CallerMemberName] string property = "")
    {
        propertyChanged?.Invoke(this, new BindablePropertyChangedEventArgs(property));
    }
}

```

## Best practices
Follow these tips and best practices to optimize performance:
  * **Use C# properties for bindable properties** : Use C# properties instead of fields when you define bindable properties. This provides flexibility to incorporate validation, notification, or any custom behavior, resulting in more robust and maintainable code.
  * **Avoid extensive computations in C# properties** : If a property requires significant processing, perform the computation only when necessary and use a cached value for subsequent bindings.
  * **Avoid unnecessary notifications** : Be cautious about notifying changes when there has been no actual change in the value. It’s unnecessary to send notifications if the value remains the same.
  * **Implement versioning and change tracking** : Use versioning in your a data source. For optimal performance, use both versioning and change tracking.
  * **Use data sources as buffers between data and UI** : Whenever possible, implement data sources as intermediaries between your data and the UI, instead of directly using the data. This approach offers several benefits:
  * Provide better control over the data flow and facilitates tracking changes originating from the UI. It allows you to manage when and how the data is updated.
  * Centralize all UI data in one location, simplifying data access and reducing complexity throughout the application.
  * Maintain the cleanliness and efficiency of the original data, eliminating the need for additional instrumentation on your types and ensuring data integrity.


## Know limitations
The following section outlines the known limitations of the runtime binding data source.
### Static types
You can’t use static types as data sources. You must create an instance of the type for the system to function.
### Methods
The property bags generated for a type only consider fields and properties. Therefore, you can’t bind to methods or built-in events.
However, it’s possible to bind to delegates such as `Action` or `Func` delegate types. To bind to delegate fields or properties, use the `=` operator instead of `+=` or `-=`. If you need to add or remove delegates instead of assigning them, you might need to implement a custom binding type.
### Interfaces
As mentioned in the [static types](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-define-data-source.html#static-types) section, you must create an object instance for a data source. While the binding system works with interfaces, types that implement an interface with properties tagged with `[CreateProperty]` don’t have bindable properties automatically generated for them. For each type, you must tag its fields and properties respectively to make them bindable. This limitation will be addressed in a future release.
### Built-in components and objects
The property bag generation process in C# is primarily designed to work with user-defined types. As a result, there is currently limited support for Unity’s built-in components and objects. This is due to various factors, including fields of built-in types being defined in native code, explicit serialization handling by the engine, or the absence of the `[SerializeField]` attribute. However, fields and properties from user-defined components and scriptable objects work as expected.
This limitation will be addressed in a future release. In the meantime, there are two workarounds available:
  * To expose a field or property from a built-in base class, add a `private` property in your own class to expose it to the binding system.
  * To use a field or property from a built-in type, such as `Transform`, create a wrapper type that exposes the required properties.


## Additional resources
  * [Runtime data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding.html)
  * [Get started with runtime binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-get-started-runtime-binding.html)
  * [Create runtime data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-types.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-types.html)
Create a runtime binding in C# scripts
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-mode-update.html)
Define binding mode and update trigger

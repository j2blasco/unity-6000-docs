* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-custom-types.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-data-binding.html)
  * [Runtime data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding.html)
  * Create custom binding types


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-logging-levels.html)
Define logging levels
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-examples.html)
Runtime data binding examples
# Create custom binding types
You can create custom binding types to extend the runtime binding system. To create a custom binding type, create a class and inherit it from the [`CustomBinding`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CustomBinding.html) class. 
## Register and unregister binding objects
The `CustomBinding` is like the [`IBinding`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IBinding.html) interface, which allows you to register multiple binding instances instead of a single one. The `CustomBinding` is an extensibility entry point and only provides an [`Update`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CustomBinding.Update.html) method to update the binding. However, you can implement the following methods to receive a callback when a binding is registered, unregistered, and when the data source context has changed on an element:
  * [`OnActivated`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding.OnActivated.html)
  * [`OnDeactivated`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding.OnDeactivated.html)
  * [`OnDataSourceChanged`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding.OnDataSourceChanged.html)


## Define data source and data source path
To define the data source and data source path for a binding type, implement the [`IDataSourceProvider`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IDataSourceProvider.html) interface. The binding system uses the `dataSource` and `dataSourcePath` properties provided by this interface to determine the resolved data source and data source path. These properties are referred to as “local” because they override the values obtained from the hierarchy. Importantly, modifying these “local” properties doesn’t impact the element itself or any of its descendants.
## Define update triggers
By default, the binding system updates a `CustomBinding` instance on every frame. 
To define update triggers, use the following methods:
  * [`MarkDirty`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding.MarkDirty.html): Sets the binding object as [`dirty`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding-isDirty.html) so that it gets updated during the next cycle.
  * [`updateTrigger`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding-updateTrigger.html): Use this `enum` property to change how the binding is updated.
  * [`BindingResult`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingResult.html): Use this method to customize the update process. The [`BindingResult`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingResult.html) is a struct that tells you whether the update was successful. It contains a `status` and a `message`.


The [`BindingResult`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingResult.html) contains a `status` and a `message`. The following are the possible values of `status`:
  * **Success** : The binding update was successful. If the binding instance doesn’t require constant updates, it isn’t updated again until there is a change in the data source or the binding instance is explicitly marked as dirty, based on the update trigger.
  * **Failure** : The binding update was unsuccessful. If the binding instance doesn’t require constant updates, it isn’t updated again until there is a change in the data source or the binding instance is explicitly marked as dirty, based on the update trigger.
  * **Pending** : The binding update is still in progress. The system automatically marks the binding instance as dirty until it receives a success or failure response.


You can use the `Pending` result of the `BindingResult` method to inform the binding system if a binding object needs to be updated on the next cycle.
## Example
This section provides an example to demonstrate how to create a custom binding type and set up the binding in UI Builder, UXML, and C#.
The following example creates a custom binding type that displays the current time. You can bind it to the `text` property of a Label to create a clock. 
```
using System;
using Unity.Properties;
using UnityEngine.UIElements;

[UxmlObject]
public partial class CurrentTimeBinding : CustomBinding
{
    [UxmlAttribute]
    public string timeFormat = "HH:mm:ss";

    public CurrentTimeBinding()
    {
        updateTrigger = BindingUpdateTrigger.EveryUpdate;
    }

    protected override BindingResult Update(in BindingContext context)
    {
        var timeNow = DateTime.Now.ToString(timeFormat);
        var element = context.targetElement;
        if (ConverterGroups.TrySetValueGlobal(ref element, context.bindingId, timeNow, out var errorCode))
            return new BindingResult(BindingStatus.Success);

        // Error handling
        var bindingTypename = TypeUtility.GetTypeDisplayName(typeof(CurrentTimeBinding));
        var bindingId = $"{TypeUtility.GetTypeDisplayName(element.GetType())}.{context.bindingId}";

        return errorCode switch
        {
            VisitReturnCode.InvalidPath => new BindingResult(BindingStatus.Failure, $"{bindingTypename}: Binding id `{bindingId}` is either invalid or contains a `null` value."),
            VisitReturnCode.InvalidCast => new BindingResult(BindingStatus.Failure, $"{bindingTypename}: Invalid conversion from `string` for binding id `{bindingId}`"),
            VisitReturnCode.AccessViolation => new BindingResult(BindingStatus.Failure, $"{bindingTypename}: Trying set value for binding id `{bindingId}`, but it is read-only."),
            _ => throw new ArgumentOutOfRangeException()
        };
    }
}

```

When you create a custom binding type, it appears in the **Add binding** window in UI Builder. To set up the binding in UI Builder, in the **Add Binding** window, select **CurrentTimeBinding** from the **Type** list.
The UXML equivalent of this binding is as follows:
```
 <ui:Label text="Label">
    <Bindings>
        <CurrentTimeBinding property="text" />
    </Bindings>
</ui:Label>

```

The C# equivalent of this binding is as follows:
```
var label = new Label();
label.SetBinding("text",  new CurrentTimeBinding());

```

## Best practices
Follow these tips and best practices to optimize performance:
  * **Minimize per-element state usage** : Reduce reliance on per-element state in your custom binding types. Instead, leverage shared or global state whenever possible to enhance performance and simplify maintenance.
  * **Use`BindingUpdateTrigger.OnSourceChanged`** : When your binding type only requires updates when changes are detected in the source, set the `updateTrigger` to `BindingUpdateTrigger.OnSourceChanged`. This ensures that the binding type is updated only when necessary, optimizing performance.
  * **Use`BindingUpdateTrigger.WhenDirty` for manual updates**: If you update your binding type manually and don’t require immediate synchronization, set the `updateTrigger` to `BindingUpdateTrigger.WhenDirty`. This allows you to manually control when the binding type updates, providing flexibility and control over synchronization.
  * **Leverage callbacks** : Whenever possible, use the `OnActivated`, `OnDeactivated`, or `OnDataSourceChanged` callbacks instead of the `Update` callback. These callbacks are triggered at specific lifecycle events, reducing unnecessary updates and improving efficiency. By using the appropriate callback, you can optimize your binding type’s behavior and ensure updates occur precisely when needed.


## Additional resources
  * [Runtime data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding.html)
  * [Create runtime data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-types.html)
  * [Create a custom binding to bind USS selectors](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-custom-binding-bind-uss.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-logging-levels.html)
Define logging levels
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-examples.html)
Runtime data binding examples

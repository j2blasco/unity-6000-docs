* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CustomBinding.html

# CustomBinding
class in UnityEngine.UIElements
/
Inherits from:[UIElements.Binding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding.html)
/
Implemented in:[UnityEngine.UIElementsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UIElementsModule.html)
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
Base class for general purpose binding extensibility. 
The following example creates a custom binding that displays the current time. You can bind it to the text field of a Label to create a clock. 
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using Unity.Properties;
using UnityEngine.UIElements;  
  
[UxmlObject]
public partial class CurrentTimeBinding : CustomBinding[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CustomBinding.html)
{
    [UxmlAttribute]
    public string timeFormat = "HH:mm:ss";  
  
    public CurrentTimeBinding()
    {
        updateTrigger = BindingUpdateTrigger.EveryUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingUpdateTrigger.EveryUpdate.html);
    }  
  
    protected override BindingResult[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingResult.html) Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)(in BindingContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingContext.html) context)
    {
        var timeNow = DateTime.Now.ToString(timeFormat);
        var element = context.targetElement;
        if (ConverterGroups.TrySetValueGlobal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroups.TrySetValueGlobal.html)(ref element, context.bindingId, timeNow, out var errorCode))
            return new BindingResult[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingResult.html)(BindingStatus.Success[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingStatus.Success.html));  
  
        // Error[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Error.html) handling
        var bindingTypename = TypeUtility.GetTypeDisplayName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.TypeUtility.GetTypeDisplayName.html)(typeof(CurrentTimeBinding));
        var bindingId = $"{TypeUtility.GetTypeDisplayName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.TypeUtility.GetTypeDisplayName.html)(element.GetType())}.{context.bindingId}";  
  
        return errorCode switch
        {
            VisitReturnCode.InvalidPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.VisitReturnCode.InvalidPath.html) => new BindingResult[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingResult.html)(BindingStatus.Failure[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingStatus.Failure.html), $"{bindingTypename}: Binding[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding.html) id `{bindingId}` is either invalid or contains a `null` value."),
            VisitReturnCode.InvalidCast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.VisitReturnCode.InvalidCast.html) => new BindingResult[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingResult.html)(BindingStatus.Failure[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingStatus.Failure.html), $"{bindingTypename}: Invalid conversion from `string` for binding id `{bindingId}`"),
            VisitReturnCode.AccessViolation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.VisitReturnCode.AccessViolation.html) => new BindingResult[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingResult.html)(BindingStatus.Failure[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingStatus.Failure.html), $"{bindingTypename}: Trying set value for binding id `{bindingId}`, but it is read-only."),
            _ => throw new ArgumentOutOfRangeException()
        };
    }
}

```

### Public Methods
Method | Description  
---|---  
[Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CustomBinding.Update.html) |  Called when the binding system updates the binding.   
### Inherited Members
### Properties
Property | Description  
---|---  
[isDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding-isDirty.html) |  When set to true, the binding instance updates during the next update cycle. When set to false, the binding instance updates only if a change is detected.   
[updateTrigger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding-updateTrigger.html) |  When set to BindingUpdateTrigger.EveryUpdate, the binding instance updates in every update, regardless of the data source version.   
### Public Methods
Method | Description  
---|---  
[MarkDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding.MarkDirty.html) |  Notifies the binding system to process this binding.   
[OnActivated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding.OnActivated.html) |  Called when the binding becomes active for a specific VisualElement.   
[OnDataSourceChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding.OnDataSourceChanged.html) |  Called when the resolved data source of a binding changes.   
[OnDeactivated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding.OnDeactivated.html) |  Called when the binding is no longer active for a specific VisualElement.   
### Static Methods
Method | Description  
---|---  
[ResetPanelLogLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding.ResetPanelLogLevel.html) |  Resets the log level for binding failures on a panel to use the global setting.   
[SetGlobalLogLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding.SetGlobalLogLevel.html) |  Sets the log level for all binding failures.   
[SetPanelLogLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding.SetPanelLogLevel.html) |  Sets the log level for binding failures on a panel.   
* * *

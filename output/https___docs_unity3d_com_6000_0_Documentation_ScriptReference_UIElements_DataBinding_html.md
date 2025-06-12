* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding.html

# DataBinding
class in UnityEngine.UIElements
/
Inherits from:[UIElements.Binding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding.html)
/
Implemented in:[UnityEngine.UIElementsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UIElementsModule.html)
Leave feedback
  

Implements interfaces:[IDataSourceProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IDataSourceProvider.html)
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
Binding type that enables data synchronization between a property of a data source and a property of a [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html). 
### Properties
Property | Description  
---|---  
[bindingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding-bindingMode.html) |  Controls how this binding should be updated. The default value is BindingMode.TwoWay.   
[dataSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding-dataSource.html) |  Object that serves as a local source for the binding, and is particularly useful when the data source is not part of the UI hierarchy, such as a static localization table. If this object is null, the binding resolves the data source using its normal resolution method.   
[dataSourcePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding-dataSourcePath.html) |  Path from the data source to the value.   
[dataSourceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding-dataSourceType.html) |  The possible data source types that can be assigned to the binding.   
[sourceToUiConverters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding-sourceToUiConverters.html) |  Returns the ConverterGroup used when trying to convert data from the data source to a UI property.   
[uiToSourceConverters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding-uiToSourceConverters.html) |  Returns the ConverterGroup used when trying to convert data from a UI property back to the data source.   
### Constructors
Constructor | Description  
---|---  
[DataBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding-ctor.html) |  Initializes and returns an instance of DataBinding.   
### Public Methods
Method | Description  
---|---  
[ApplyConverterGroupToSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding.ApplyConverterGroupToSource.html) |  Applies a ConverterGroup to this binding that will be used when converting data between a UI control to a data source.   
[ApplyConverterGroupToUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding.ApplyConverterGroupToUI.html) |  Applies a ConverterGroup to this binding that will be used when converting data between a data source to a UI control.   
[UpdateSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding.UpdateSource.html) |  Callback called to allow derived classes to update the data source with the resolved value when a change from the UI is detected.   
[UpdateUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding.UpdateUI.html) |  Callback called to allow derived classes to update the UI with the resolved value from the data source.   
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

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingMode.html

# BindingMode
enumeration
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
Binding mode to control how a binding is updated. 
To let the data binding system know that the value in the UI changed, use VisualElement.NotifyPropertyChanged.
### Properties
Property | Description  
---|---  
[TwoWay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingMode.TwoWay.html) |  Changes on the data source will be replicated in the UI. Changes on the UI will be replicated to the data source.   
[ToSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingMode.ToSource.html) |  Changes will only be replicated from the UI to the data source for this binding.   
[ToTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingMode.ToTarget.html) |  Changes will only be replicated from the source to the UI for this binding.   
[ToTargetOnce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingMode.ToTargetOnce.html) |  Changes will only be replicated once, from the source to the UI. This binding will be ignored on subsequent updates.   
* * *

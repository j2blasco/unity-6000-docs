* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroup.html

# ConverterGroup
class in UnityEngine.UIElements
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
A type to hold information about a conversion registry used locally on bindings. 
You can apply converter groups on a [DataBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding.html) in UXML with the `source-to-ui-converters` or `ui-to-source-converters` attributes or in C# script with the [DataBinding.ApplyConverterGroupToSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding.ApplyConverterGroupToSource.html) or [DataBinding.ApplyConverterGroupToUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding.ApplyConverterGroupToUI.html) methods. 
### Properties
Property | Description  
---|---  
[description](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroup-description.html) |  Optional description for a converter group ID that may include information about what this group contains or is used for, to be displayed to users to assist while authoring.   
[displayName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroup-displayName.html) |  Optional and alternative name for a converter group ID, to be displayed to users to assist while authoring.   
[id](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroup-id.html) |  The group id.   
### Constructors
Constructor | Description  
---|---  
[ConverterGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroup-ctor.html) |  Creates a ConverterGroup.   
### Public Methods
Method | Description  
---|---  
[AddConverter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroup.AddConverter.html) |  Adds a converter to the group.   
[TryConvert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroup.TryConvert.html) |  Converts the specified value from TSource to TDestination using only the converter group.   
[TrySetValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroup.TrySetValue.html) |  Sets the value of a property at the given path to the given value, using this converter group or the global ones.   
* * *

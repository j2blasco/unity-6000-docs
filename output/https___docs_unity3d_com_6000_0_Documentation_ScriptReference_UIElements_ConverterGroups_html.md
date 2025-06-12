* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroups.html

# ConverterGroups
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
Provides a set of static methods to register and use converter groups and registers a set of global converters. [ConverterGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroup.html). [DataBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding.html). 
### Static Methods
Method | Description  
---|---  
[RegisterConverterGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroups.RegisterConverterGroup.html) |  Registers a converter group by ID. Converter groups can be applied on a binding using local converters.   
[RegisterGlobalConverter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroups.RegisterGlobalConverter.html) |  Registers a global UI conversion delegate that will be used when converting data between a data source and a UI control. This delegate will be used both when converting data from and to UI.   
[TryConvert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroups.TryConvert.html) |  Converts the specified value from TSource to TDestination using the registered global converters.   
[TryGetConverterGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroups.TryGetConverterGroup.html) |  Retrieves a converter group by ID.   
[TrySetValueGlobal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroups.TrySetValueGlobal.html) |  Sets the value of a property at the given path to the given value, using the global converters.   
* * *

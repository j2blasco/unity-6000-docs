* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroup.TrySetValue.html

#  [ConverterGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroup.html).TrySetValue
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
## Declaration
public bool TrySetValue(ref TContainer container, ref [Unity.Properties.PropertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html) path, TValue value, out [Unity.Properties.VisitReturnCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.VisitReturnCode.html) returnCode); 
### Parameters
Parameter | Description  
---|---  
container | The container whose property needs to be set.  
path | The path of the property to set.  
value | The value to assign to the property.  
returnCode | The return code of the conversion.  
### Returns
**bool** `true` if the value was set correctly, and `false` otherwise. 
### Description
Sets the value of a property at the given path to the given value, using this converter group or the global ones. 
This method isn't thread-safe. 
* * *

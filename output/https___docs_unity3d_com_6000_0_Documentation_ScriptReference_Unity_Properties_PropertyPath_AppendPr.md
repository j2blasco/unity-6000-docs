* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.AppendProperty.html

#  [PropertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html).AppendProperty
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
public static [Unity.Properties.PropertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html) AppendProperty(ref [Unity.Properties.PropertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html) path, [Unity.Properties.IProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.IProperty.html) property); 
### Parameters
Parameter | Description  
---|---  
path | The <see cref="PropertyPath" />  
property | The property to add.  
### Returns
**PropertyPath** A new [PropertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html)
### Description
Returns a new [PropertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html) combining the given [PropertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html) and a [PropertyPathPart](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPathPart.html) whose type will be based on the property interfaces. 
* * *

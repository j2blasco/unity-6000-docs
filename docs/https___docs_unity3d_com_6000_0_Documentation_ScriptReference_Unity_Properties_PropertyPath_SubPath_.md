* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.SubPath.html

#  [PropertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html).SubPath
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
public static [Unity.Properties.PropertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html) SubPath(ref [Unity.Properties.PropertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html) path, int startIndex); 
### Parameters
Parameter | Description  
---|---  
path | The <see cref="PropertyPath" />  
startIndex | The zero-based index where the sub path should start.  
### Returns
**PropertyPath** A new [PropertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html)
### Description
Returns a new [PropertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html) containing the [PropertyPathPart](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPathPart.html) starting at the given start index. 
* * *
## Declaration
public static [Unity.Properties.PropertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html) SubPath(ref [Unity.Properties.PropertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html) path, int startIndex, int length); 
### Parameters
Parameter | Description  
---|---  
path | The <see cref="PropertyPath" />  
startIndex | The zero-based index where the sub path should start.  
length | The number of parts to include.  
### Returns
**PropertyPath** A new [PropertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html)
### Description
Returns a new [PropertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPath.html) containing the given number of [PropertyPathPart](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.PropertyPathPart.html) starting at the given start index. 
* * *

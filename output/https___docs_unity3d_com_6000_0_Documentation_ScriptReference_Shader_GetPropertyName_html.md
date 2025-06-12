* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetPropertyName.html

#  [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html).GetPropertyName
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Shader.html "Go to Shader Component in the Manual")
## Declaration
public string GetPropertyName(int propertyIndex); 
### Parameters
Parameter | Description  
---|---  
propertyIndex | The index of the shader property.  
### Description
Returns the name of the shader property at the specified index.
If Unity cannot find a property at the specified index, the function throws an `ArgumentOutOfRangeException`.
* * *

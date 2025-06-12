* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetInt.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).GetInt
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html "Go to Material Component in the Manual")
## Declaration
public int GetInt(string name); 
## Declaration
public int GetInt(int nameID); 
### Parameters
Parameter | Description  
---|---  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
name | The name of the property.  
### Description
This method is deprecated. Use [GetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetFloat.html) or [GetInteger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetInteger.html) instead.
This function is just an alias to [GetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetFloat.html) that casts the resulting value to an integer.
* * *

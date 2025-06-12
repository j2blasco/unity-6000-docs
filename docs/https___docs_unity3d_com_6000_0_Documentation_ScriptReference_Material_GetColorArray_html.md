* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetColorArray.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).GetColorArray
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
public Color[] GetColorArray(string name); 
## Declaration
public Color[] GetColorArray(int nameID); 
### Parameters
Parameter | Description  
---|---  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
name | The name of the property.  
### Description
Get a named color array.
It is just an alias to [GetVectorArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetVectorArray.html), only colors are cast to vectors. No sRGB-linear conversion is done during the function call.  
  
Additional resources: [SetColorArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetColorArray.html), [GetVectorArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetVectorArray.html).
* * *
## Declaration
public void GetColorArray(string name, List<Color> values); 
## Declaration
public void GetColorArray(int nameID, List<Color> values); 
### Parameters
Parameter | Description  
---|---  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
name | The name of the property.  
values | The list to hold the returned array.  
### Description
Fetch a named color array into a list.
The list will be resized to the array size, or cleared if such property doesn't exist. Memory allocation is guaranteed not to happen during the function call.
* * *

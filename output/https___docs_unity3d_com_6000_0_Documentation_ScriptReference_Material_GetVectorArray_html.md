* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetVectorArray.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).GetVectorArray
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
public Vector4[] GetVectorArray(string name); 
## Declaration
public Vector4[] GetVectorArray(int nameID); 
### Parameters
Parameter | Description  
---|---  
name | The name of the property.  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
### Description
Get a named vector array.
Additional resources: [SetVectorArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetVectorArray.html).
* * *
## Declaration
public void GetVectorArray(string name, List<Vector4> values); 
## Declaration
public void GetVectorArray(int nameID, List<Vector4> values); 
### Parameters
Parameter | Description  
---|---  
name | The name of the property.  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
values | The list to hold the returned array.  
### Description
Fetch a named vector array into a list.
The list will be resized to the array size, or cleared if such property doesn't exist. Memory allocation is guaranteed not to happen during the function call.
* * *

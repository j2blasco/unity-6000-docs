* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.GetGlobalVectorArray.html

#  [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html).GetGlobalVectorArray
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
public static Vector4[] GetGlobalVectorArray(string name); 
## Declaration
public static Vector4[] GetGlobalVectorArray(int nameID); 
### Parameters
Parameter | Description  
---|---  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
name | The name of the property.  
### Description
Gets a global vector array for all shaders previously set using [SetGlobalVectorArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalVectorArray.html).
* * *
## Declaration
public static void GetGlobalVectorArray(string name, List<Vector4> values); 
## Declaration
public static void GetGlobalVectorArray(int nameID, List<Vector4> values); 
### Parameters
Parameter | Description  
---|---  
values | The list to hold the returned array.  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
name | The name of the property.  
### Description
Fetches a global vector array into a list.
The list will be resized to the array size, or cleared if such property doesn't exist. Memory allocation is guaranteed not to happen during the function call.
* * *

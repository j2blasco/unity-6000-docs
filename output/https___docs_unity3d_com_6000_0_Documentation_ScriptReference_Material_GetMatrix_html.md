* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetMatrix.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).GetMatrix
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
public [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) GetMatrix(string name); 
## Declaration
public [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) GetMatrix(int nameID); 
### Parameters
Parameter | Description  
---|---  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
name | The name of the property.  
### Description
Get a named matrix value from the shader.
This is mostly used with custom shaders that need extra matrix parameters. Matrix parameters are not exposed in the material inspector, but can be set and queried with `SetMatrix` and `GetMatrix` from scripts.  
  
Additional resources: [SetMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetMatrix.html), [Materials](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html), [ShaderLab documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html), [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).
* * *

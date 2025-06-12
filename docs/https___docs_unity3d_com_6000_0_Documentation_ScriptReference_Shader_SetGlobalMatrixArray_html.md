* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalMatrixArray.html

#  [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html).SetGlobalMatrixArray
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
public static void SetGlobalMatrixArray(string name, Matrix4x4[] values); 
## Declaration
public static void SetGlobalMatrixArray(int nameID, Matrix4x4[] values); 
## Declaration
public static void SetGlobalMatrixArray(string name, List<Matrix4x4> values); 
## Declaration
public static void SetGlobalMatrixArray(int nameID, List<Matrix4x4> values); 
### Parameters
Parameter | Description  
---|---  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
name | The name of the property.  
### Description
Sets a global matrix array property for all shaders.
Global properties are used if a shader needs them but the material does not have them defined (for example, if the shader does not expose them in `Properties` block).  
  
Additional resources: [SetGlobalMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalMatrix.html).
* * *

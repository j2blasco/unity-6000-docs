* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalBuffer.html

#  [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html).SetGlobalBuffer
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
public static void SetGlobalBuffer(string name, [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) value); 
## Declaration
public static void SetGlobalBuffer(int nameID, [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) value); 
## Declaration
public static void SetGlobalBuffer(string name, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) value); 
## Declaration
public static void SetGlobalBuffer(int nameID, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) value); 
### Parameters
Parameter | Description  
---|---  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
name | The name of the property.  
value | The buffer to set.  
### Description
Sets a global buffer property for all shaders.
Global properties are used if a shader needs them but the material does not have them defined (for example, if the shader does not expose them in `Properties` block).  
  
Additional resources: [SetGlobalTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalTexture.html), [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) class, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) class, [ShaderLab documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html).
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalVector.html

#  [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html).SetGlobalVector
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
public static void SetGlobalVector(string name, [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) value); 
## Declaration
public static void SetGlobalVector(int nameID, [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) value); 
### Parameters
Parameter | Description  
---|---  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
name | The name of the property.  
### Description
Sets a global vector property for all shaders.
Global properties are used if a shader needs them but the material does not have them defined (for example, if the shader does not expose them in `Properties` block).  
  
Usually this is used if you have a set of custom shaders that all use the same "global" vector (for example, wind direction). Then you can set the global property from script and don't have to setup the same vector in all materials.  
  
Additional resources: [SetGlobalFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalFloat.html), [SetGlobalColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalColor.html), [SetGlobalTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalTexture.html); [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) class, [ShaderLab documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html).
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalColor.html

#  [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html).SetGlobalColor
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
public static void SetGlobalColor(string name, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) value); 
## Declaration
public static void SetGlobalColor(int nameID, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) value); 
### Parameters
Parameter | Description  
---|---  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
name | The name of the property.  
### Description
Sets a global color property for all shaders.
Global properties are used if a shader needs them but the material does not have them defined (for example, if the shader does not expose them in `Properties` block).  
  
Usually this is used if you have a set of custom shaders that all use the same "global" color (for example, color of the sun). Then you can set the global property from script and don't have to setup the same color in all materials.  
  
Note that unlike [Material.SetColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetColor.html), this function doesn't do color space conversion. It is just an alias to [SetGlobalVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalVector.html).  
  
Additional resources: [SetGlobalFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalFloat.html), [SetGlobalVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalVector.html), [SetGlobalTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalTexture.html); [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) class, [ShaderLab documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html).
* * *

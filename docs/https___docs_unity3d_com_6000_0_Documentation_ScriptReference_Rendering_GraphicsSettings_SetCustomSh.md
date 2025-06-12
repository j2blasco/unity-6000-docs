* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.SetCustomShader.html

#  [GraphicsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.html).SetCustomShader
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
## Declaration
public static void SetCustomShader([Rendering.BuiltinShaderType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinShaderType.html) type, [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader); 
### Parameters
Parameter | Description  
---|---  
type | Built-in shader type to set custom shader to.  
shader | The shader to use.  
### Description
Set custom shader to use instead of a built-in shader.
This is only used when built-in shader is set to [BuiltinShaderMode.UseCustom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinShaderMode.UseCustom.html) mode; see [SetShaderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.SetShaderMode.html).  
  
Additional resources: [GetCustomShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.GetCustomShader.html), [SetShaderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.SetShaderMode.html), [Graphics Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html).
* * *

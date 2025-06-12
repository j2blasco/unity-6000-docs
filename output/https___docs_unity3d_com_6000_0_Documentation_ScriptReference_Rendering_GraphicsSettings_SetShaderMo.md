* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.SetShaderMode.html

#  [GraphicsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.html).SetShaderMode
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
public static void SetShaderMode([Rendering.BuiltinShaderType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinShaderType.html) type, [Rendering.BuiltinShaderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinShaderMode.html) mode); 
### Parameters
Parameter | Description  
---|---  
type | Built-in shader type to change.  
mode | Mode to use for built-in shader.  
### Description
Set built-in shader mode.
By default, certain parts of rendering pipeline in Unity (e.g. deferred shading light calculations) use built-in shader. However, it is possible to setup a custom shader to replace the built-in functionality, or to turn off support for it altogether.  
  
When setting [BuiltinShaderMode.UseCustom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinShaderMode.UseCustom.html), you also need to indicate which shader to use. See [SetCustomShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.SetCustomShader.html).  
  
Additional resources: [GetShaderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.GetShaderMode.html), [SetCustomShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.SetCustomShader.html), [Graphics Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html).
* * *

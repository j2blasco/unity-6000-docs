* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinShaderMode.Disabled.html

#  [BuiltinShaderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinShaderMode.html).Disabled
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
### Description
Don't use any shader, effectively disabling the functionality.
This is primarily used as a build size optimization, for example if you know the project never uses deferred shading, you could disable support for it in [Graphics Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html) and save some build data size.  
  
When [BuiltinShaderType.DeferredReflections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinShaderType.DeferredReflections.html) is disabled, then in deferred shading the reflection probes are done in per-object way, instead of a separate deferred per-pixel reflections pass.  
  
Additional resources: [GraphicsSettings.SetShaderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.SetShaderMode.html), [BuiltinShaderType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinShaderType.html), [Graphics Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html).
* * *

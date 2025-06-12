* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinShaderType.DeferredReflections.html

#  [BuiltinShaderType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinShaderType.html).DeferredReflections
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
Shader used for deferred reflection probes.
When using deferred shading, [reflection probes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html) are rendered in "deferred" way by default. All deferred objects in the Scene get per-pixel reflection probes that are calculated using this shader.  
  
When setting deferred reflections shader to "disabled" ([BuiltinShaderMode.Disabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinShaderMode.Disabled.html)), reflection probes are done in per-object way, similar to how forward rendering computes them.  
  
Additional resources: [GraphicsSettings.SetShaderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.SetShaderMode.html), [BuiltinShaderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinShaderMode.html), [Graphics Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html).
* * *

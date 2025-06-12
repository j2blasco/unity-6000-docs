* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeUsage.html

# ReflectionProbeUsage
enumeration
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
Reflection Probe usage.
### Properties
Property | Description  
---|---  
[Off](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeUsage.Off.html) | Reflection probes are disabled, skybox will be used for reflection.  
[BlendProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeUsage.BlendProbes.html) | Reflection probes are enabled. Blending occurs only between probes, useful in indoor environments. The renderer will use default reflection if there are no reflection probes nearby, but no blending between default reflection and probe will occur.  
[BlendProbesAndSkybox](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeUsage.BlendProbesAndSkybox.html) | Reflection probes are enabled. Blending occurs between probes or probes and default reflection, useful for outdoor environments.  
[Simple](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeUsage.Simple.html) | Reflection probes are enabled, but no blending will occur between probes when there are two overlapping volumes.  
* * *

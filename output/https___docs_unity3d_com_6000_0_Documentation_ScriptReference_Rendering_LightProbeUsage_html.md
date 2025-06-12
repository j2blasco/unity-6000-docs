* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.html

# LightProbeUsage
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
Light probe interpolation type.
Additional resources: [Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html), [Light Probe Proxy Volume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume.html).
### Properties
Property | Description  
---|---  
[Off](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.Off.html) | Light Probes are not used. The Scene's ambient probe is provided to the shader.  
[BlendProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.BlendProbes.html) | Simple light probe interpolation is used.  
[UseProxyVolume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.UseProxyVolume.html) | Uses a 3D grid of interpolated light probes.  
[CustomProvided](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.CustomProvided.html) | The light probe shader uniform values are extracted from the material property block set on the renderer.  
* * *

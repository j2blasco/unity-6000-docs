* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PerObjectData.html

# PerObjectData
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
What kind of per-object data to setup during rendering.
At minimum, object transformation matrices are set up per-object, but extra data (e.g. lightmaps, light probes etc.) can be set up by combining PerObjectData flags.  
  
Additional resources: [DrawingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings.html), ScriptableRenderContext.DrawRenderers.
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PerObjectData.None.html) | Do not setup any particular per-object data besides the transformation matrix.  
[LightProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PerObjectData.LightProbe.html) | Setup per-object light probe SH data.  
[ReflectionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PerObjectData.ReflectionProbes.html) | Setup per-object reflection probe data.  
[LightProbeProxyVolume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PerObjectData.LightProbeProxyVolume.html) | Setup per-object light probe proxy volume data.  
[Lightmaps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PerObjectData.Lightmaps.html) | Setup per-object lightmaps.  
[LightData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PerObjectData.LightData.html) | Setup per-object light data.  
[MotionVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PerObjectData.MotionVectors.html) | Setup per-object motion vectors.  
[LightIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PerObjectData.LightIndices.html) | Setup per-object light indices.  
[ReflectionProbeData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PerObjectData.ReflectionProbeData.html) | Setup per-object reflection probe index offset and count.  
[OcclusionProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PerObjectData.OcclusionProbe.html) | Setup per-object occlusion probe data.  
[OcclusionProbeProxyVolume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PerObjectData.OcclusionProbeProxyVolume.html) | Setup per-object occlusion probe proxy volume data (occlusion in alpha channels).  
[ShadowMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PerObjectData.ShadowMask.html) | Setup per-object shadowmask.  
* * *

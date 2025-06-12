* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingOptions.html

# CullingOptions
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
Flags used by [ScriptableCullingParameters.cullingOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableCullingParameters-cullingOptions.html) to configure a culling operation.
Unity sets some of the [CullingOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingOptions.html) flags with default values, and others depending on the properties of the [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) from which you obtained the [ScriptableCullingParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableCullingParameters.html) struct. You can override these values before performing the culling operation.  
  
Additional resources: [ScriptableCullingParameters.cullingOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableCullingParameters-cullingOptions.html), [ScriptableRenderContext.Cull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.Cull.html), [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingOptions.None.html) | Unset all CullingOptions flags.  
[ForceEvenIfCameraIsNotActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingOptions.ForceEvenIfCameraIsNotActive.html) | When this flag is set, Unity performs the culling operation even if the Camera is not active.  
[OcclusionCull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingOptions.OcclusionCull.html) | When this flag is set, Unity performs occlusion culling as part of the culling operation.  
[NeedsLighting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingOptions.NeedsLighting.html) | When this flag is set, Unity culls Lights as part of the culling operation.  
[NeedsReflectionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingOptions.NeedsReflectionProbes.html) | When this flag is set, Unity culls Reflection Probes as part of the culling operation.  
[Stereo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingOptions.Stereo.html) | When this flag is set, Unity culls both eyes together for stereo rendering.  
[DisablePerObjectCulling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingOptions.DisablePerObjectCulling.html) | When this flag is set, Unity does not perform per-object culling.  
[ShadowCasters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingOptions.ShadowCasters.html) | When this flag is set, Unity culls shadow casters as part of the culling operation.  
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingMeshInstanceConfig-subMeshFlags.html

#  [RayTracingMeshInstanceConfig](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingMeshInstanceConfig.html).subMeshFlags
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
[Rendering.RayTracingSubMeshFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingSubMeshFlags.html) subMeshFlags; 
### Description
Flags that determine how rays intersect the geometry for each submesh relative to Material type during ray tracing.
The Material type can influence the value of this flag. For example if Unity considers the Material opaque, you can specify the [RayTracingSubMeshFlags.Enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingSubMeshFlags.Enabled.html) and [RayTracingSubMeshFlags.ClosestHitOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingSubMeshFlags.ClosestHitOnly.html) flags together for maximum ray tracing performance.
* * *

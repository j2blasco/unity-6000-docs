* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingInstanceCullingConfig-lodParameters.html

#  [RayTracingInstanceCullingConfig](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingInstanceCullingConfig.html).lodParameters
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
[Rendering.LODParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LODParameters.html) lodParameters; 
### Description
Parameters used for LOD culling.
LOD culling is enabled by using [RayTracingInstanceCullingFlags.EnableLODCulling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingInstanceCullingFlags.EnableLODCulling.html) flag in [RayTracingInstanceCullingConfig.flags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingInstanceCullingConfig-flags.html). If the flag is not used then all the Renderers in the [LODGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LODGroup.html) will be processes and eventually added to the acceleration structure.  
  
Additional resources: [RayTracingAccelerationStructure.CullInstances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.CullInstances.html), [QualitySettings.lodBias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-lodBias.html).
* * *

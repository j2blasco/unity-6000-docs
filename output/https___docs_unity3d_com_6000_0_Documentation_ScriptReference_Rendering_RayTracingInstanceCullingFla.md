* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingInstanceCullingFlags.ComputeMaterialsCRC.html

#  [RayTracingInstanceCullingFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingInstanceCullingFlags.html).ComputeMaterialsCRC
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
Causes [RayTracingAccelerationStructure.CullInstances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.CullInstances.html) to compute the CRC hash values of all unique Materials used by ray tracing instances that were added to the acceleration structure.
The array of Material CRC values is returned by [RayTracingAccelerationStructure.CullInstances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.CullInstances.html) in [RayTracingInstanceCullingResults](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingInstanceCullingResults.html).  
  
The cost for enabling this flag depends on how complex the Materials are and how many different Materials are used in a Scene. The CRC array can be used for example to reset the convergence during path tracing if a Material property has changed between frames.  
  
Additional resources: [Material.ComputeCRC](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.ComputeCRC.html), [HashUtilities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HashUtilities.html).
* * *

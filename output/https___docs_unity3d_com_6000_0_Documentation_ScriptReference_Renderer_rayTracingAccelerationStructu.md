* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-rayTracingAccelerationStructureBuildFlagsOverride.html

#  [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html).rayTracingAccelerationStructureBuildFlagsOverride
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
rayTracingAccelerationStructureBuildFlagsOverride; 
### Description
Whether to override the default build flags specified when creating a [RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html).
If you set this value to `true`, Unity uses [Renderer.rayTracingAccelerationStructureBuildFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-rayTracingAccelerationStructureBuildFlags.html) when it builds the acceleration structure associated with this renderer.  
  
If you set this value to false (default) and if [Renderer.rayTracingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-rayTracingMode.html) is [RayTracingMode.DynamicGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.RayTracingMode.DynamicGeometry.html) then Unity uses [RayTracingAccelerationStructure.Settings.buildFlagsDynamicGeometries](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.Settings-buildFlagsDynamicGeometries.html) value as build flags, otherwise [RayTracingAccelerationStructure.Settings.buildFlagsStaticGeometries](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.Settings-buildFlagsStaticGeometries.html) is used.  
  
Additional resources: [RayTracingAccelerationStructure.Build](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.Build.html), [RayTracingAccelerationStructure.CullInstances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.CullInstances.html), [SystemInfo.supportsRayTracing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsRayTracing.html).
* * *

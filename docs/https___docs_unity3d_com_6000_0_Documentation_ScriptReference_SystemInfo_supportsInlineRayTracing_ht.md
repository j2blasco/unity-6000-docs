* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsInlineRayTracing.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).supportsInlineRayTracing
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
supportsInlineRayTracing; 
### Description
Is inline ray tracing (ray query) supported? (Read Only)
Inline ray tracing is an alternative form of ray tracing available in compute shaders and rasterization stages through the `RayQuery` HLSL object. In DirectX 12 (DX12), this property corresponds to DirectX Raytracing (DXR) Tier 1.1 support.  
  
The `RayQuery` object is defined in HLSL when you use the DirectX 12 and DirectX Shader Compiler (DXC). Other shader compilers that different platforms use either don’t define the `RayQuery` object or its name is different. Because of this, the recommended approach is to include the `UnityRayQuery.cginc` header and use the `UnityRayQuery` object instead of `RayQuery`.   
  
Additional resources: [Shader.SetGlobalRayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalRayTracingAccelerationStructure.html), [ComputeShader.SetRayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetRayTracingAccelerationStructure.html), [SystemInfo.supportsRayTracingShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsRayTracingShaders.html).
* * *

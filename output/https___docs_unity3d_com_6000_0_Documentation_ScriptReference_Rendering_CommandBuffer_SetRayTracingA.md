* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetRayTracingAccelerationStructure.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).SetRayTracingAccelerationStructure
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
## Declaration
public void SetRayTracingAccelerationStructure([Rendering.RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html) rayTracingShader, string name, [Rendering.RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) rayTracingAccelerationStructure); 
## Declaration
public void SetRayTracingAccelerationStructure([Rendering.RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html) rayTracingShader, int nameID, [Rendering.RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) rayTracingAccelerationStructure); 
## Declaration
public void SetRayTracingAccelerationStructure([ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader, int kernelIndex, int nameID, [Rendering.RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) rayTracingAccelerationStructure); 
## Declaration
public void SetRayTracingAccelerationStructure([ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader, int kernelIndex, string name, [Rendering.RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) rayTracingAccelerationStructure); 
### Parameters
Parameter | Description  
---|---  
rayTracingShader | The [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html) to set parameter for.  
name | The name of the acceleration structure in the shader code.  
nameID | Property name ID. Use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get this ID.  
rayTracingAccelerationStructure | The [RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) object to be set.  
computeShader | The [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) object to set the parameter for.  
kernelIndex | Which kernel the acceleration structure is being set for.  
### Description
Adds a command to set the [RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) to be used in a [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html) or a [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html).
When using a [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html), the [RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) specified as argument is visible globally in all ray tracing shader types (e.g. closest hit, any hit, miss, etc.).  
  
When using a [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html), it binds a [RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) to a [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) kernel to be used for Inline Ray Tracing (Ray Queries). This functionality is available on platforms where this feature is supported. Use [SystemInfo.supportsInlineRayTracing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsInlineRayTracing.html) to check this.  
  
In compute shaders, ray queries can be used to perform acceleration structure traversal and geometry intersection tests. To access this functionality, the HLSL code needs to be compiled using `#pragma require inlineraytracing`.
```
#include "UnityRayQuery.cginc"  
  
#pragma require inlineraytracing
#pragma kernel CSRayQueryTest  
  
RaytracingAccelerationStructure g_AccelStruct;
RWTexture2D<float> g_Output;  
  
[numthreads(8,4,1)]
void CSRayQueryTest (uint3 id : SV_DispatchThreadID)
{
    const uint rayFlags = RAY_FLAG_ACCEPT_FIRST_HIT_AND_END_SEARCH;
    UnityRayQuery<rayFlags> rayQuery;  
  
    RayDesc ray;
    ray.Origin = float3(0, 0, 0);
    ray.Direction = float3(0, 1, 0);
    ray.TMin = 0;
    ray.TMax = 10000;  
  
    rayQuery.TraceRayInline(g_AccelStruct, rayFlags, 0xff, ray);
    rayQuery.Proceed();  
  
    g_Output[id.xy] = (rayQuery.CommittedStatus() == COMMITTED_TRIANGLE_HIT) ? 1.0 : 0.0;
}
```

This is a simple compute shader that checks if a ray with the origin at (0, 0, 0) and direction (0, 1, 0) intersects any geometry consisting of triangles. The `g_AccelStruct` shader object can be bound using the SetRayTracingAccelerationStructure function. The compute shader can be dispatched if [SystemInfo.supportsInlineRayTracing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsInlineRayTracing.html) is true.  
  
Additional resources: [RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html), [SystemInfo.supportsRayTracingShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsRayTracingShaders.html), [SystemInfo.supportsInlineRayTracing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsInlineRayTracing.html).
* * *

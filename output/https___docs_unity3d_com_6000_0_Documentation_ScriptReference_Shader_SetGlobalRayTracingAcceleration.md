* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalRayTracingAccelerationStructure.html

#  [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html).SetGlobalRayTracingAccelerationStructure
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Shader.html "Go to Shader Component in the Manual")
## Declaration
public static void SetGlobalRayTracingAccelerationStructure(string name, [Rendering.RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) value); 
## Declaration
public static void SetGlobalRayTracingAccelerationStructure(int nameID, [Rendering.RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) value); 
### Parameters
Parameter | Description  
---|---  
name | The name of the acceleration structure in shader code.  
nameID | The name ID of the acceleration structure in shader code. Use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get this value.  
value | The acceleration structure to set.  
### Description
Sets a global [RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) property for all shaders.
This command binds a [RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) object to all shader stages. You can use the acceleration structure for inline ray tracing (ray queries) or as an argument in `TraceRay` calls in ray tracing shaders. The [RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) object must be built using the [RayTracingAccelerationStructure.Build](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.Build.html) method before calling this command.  
  
Ray queries can be used to perform acceleration structure traversal and geometry intersection tests. To access this functionality, the HLSL code must be compiled using the `#pragma require inlineraytracing` directive or by using the built-in shader keyword `UNITY_DEVICE_SUPPORTS_INLINE_RAY_TRACING` (for example, #pragma multi_compile _ UNITY_DEVICE_SUPPORTS_INLINE_RAY_TRACING).  
  
Additional resources: [CommandBuffer.SetGlobalRayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetGlobalRayTracingAccelerationStructure.html), [SystemInfo.supportsRayTracingShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsRayTracingShaders.html), [SystemInfo.supportsInlineRayTracing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsInlineRayTracing.html).
* * *

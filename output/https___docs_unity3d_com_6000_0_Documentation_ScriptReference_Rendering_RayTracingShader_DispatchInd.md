* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.DispatchIndirect.html

#  [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html).DispatchIndirect
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
public void DispatchIndirect(string rayGenFunctionName, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) argsBuffer, uint argsOffset, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera); 
### Parameters
Parameter | Description  
---|---  
rayGenFunctionName | The name of the ray generation shader.  
argsBuffer | Buffer containing dispatch dimensions.  
argsOffset | The byte offset into the buffer where the dispatch dimensions start.  
camera | If you pass this parameter, Unity sets up built-in shader variables related to that camera.  
### Description
Dispatches this [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html).
This method is similar to [Dispatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.Dispatch.html) but the GPU retrieves the dispatch dimensions from `argsBuffer`. The typical use case is generating arbitrary amount of data using a [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) and then dispatching that data, without requiring a readback to the CPU to retrieve the data size.  
  
The buffer with arguments, `argsBuffer`, must contain three integer numbers at given `argsOffset` values representing the dispatch dimensions: width, height and depth.   
  
Additional resources: [SystemInfo.supportsIndirectDispatchRays](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsIndirectDispatchRays.html), [GraphicsBuffer.CopyCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.CopyCount.html).
* * *

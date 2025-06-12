* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.AddCommandBufferAsync.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).AddCommandBufferAsync
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
## Declaration
public void AddCommandBufferAsync([Rendering.CameraEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.html) evt, [Rendering.CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) buffer, [Rendering.ComputeQueueType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ComputeQueueType.html) queueType); 
### Parameters
Parameter | Description  
---|---  
evt | The point during the graphics processing at which this command buffer should commence on the GPU.  
buffer | The buffer to execute.  
queueType | The desired async compute queue type to execute the buffer on.  
### Description
Adds a command buffer to the GPU's async compute queues and executes that command buffer when graphics processing reaches a given point.
Executes an async compute command buffer on the GPU when the graphics queues processing reaches a point described by the evt parameter.  
  
Multiple command buffers can be set to execute at the same camera event (or even the same buffer can be added multiple times). To remove a command buffer from execution, use [RemoveCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.RemoveCommandBuffer.html).  
  
The command buffer can only call the following commands for execution on the async compute queues, otherwise an error will be logged and displayed in the Editor window:  
  
[CommandBuffer.BeginSample](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.BeginSample.html)  
  
[CommandBuffer.BuildRayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.BuildRayTracingAccelerationStructure.html)  
  
[CommandBuffer.CopyCounterValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.CopyCounterValue.html)  
  
[CommandBuffer.CopyTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.CopyTexture.html)  
  
CommandBuffer.CreateGPUFence  
  
[CommandBuffer.DispatchCompute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DispatchCompute.html)  
  
[CommandBuffer.EndSample](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.EndSample.html)  
  
[CommandBuffer.IssuePluginEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.IssuePluginEvent.html)  
  
[CommandBuffer.SetComputeBufferParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeBufferParam.html)  
  
[CommandBuffer.SetComputeFloatParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeFloatParam.html)  
  
[CommandBuffer.SetComputeFloatParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeFloatParams.html)  
  
[CommandBuffer.SetComputeTextureParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeTextureParam.html)  
  
[CommandBuffer.SetComputeVectorParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeVectorParam.html)  
  
CommandBuffer.WaitOnGPUFence  
  
All of the commands within the buffer are guaranteed to be executed on the same queue. If the target platform does not support async compute queues then the work is dispatched on the graphics queue. This API is only available with the Built-in renderer.  
  
Additional resources:GPUFence, [SystemInfo.supportsAsyncCompute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsAsyncCompute.html), [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html), [RemoveCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.RemoveCommandBuffer.html), [GetCommandBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.GetCommandBuffers.html).
* * *

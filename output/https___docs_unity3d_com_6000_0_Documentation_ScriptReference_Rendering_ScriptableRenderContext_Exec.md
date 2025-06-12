* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.ExecuteCommandBufferAsync.html

#  [ScriptableRenderContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html).ExecuteCommandBufferAsync
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
public void ExecuteCommandBufferAsync([Rendering.CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) commandBuffer, [Rendering.ComputeQueueType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ComputeQueueType.html) queueType); 
### Parameters
Parameter | Description  
---|---  
commandBuffer | The [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) to be executed.  
queueType | Describes the desired async compute queue the supplied [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) should be executed on.  
### Description
Schedules the execution of a Command Buffer on an async compute queue. The [ComputeQueueType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ComputeQueueType.html) that you pass in determines the queue order.
Note that all of the commands within the Command Buffer need to be of a type suitable for execution on the async compute queues. If the buffer contains any commands that are not appropriate then Unity logs an error and displays it in the Editor console window. The commands that a [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) can use on async compute queues are:  

  * [CommandBuffer.BeginSample](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.BeginSample.html)
  * [CommandBuffer.BuildRayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.BuildRayTracingAccelerationStructure.html)
  * [CommandBuffer.CopyCounterValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.CopyCounterValue.html)
  * [CommandBuffer.CopyTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.CopyTexture.html)
  * [CommandBuffer.CreateGraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.CreateGraphicsFence.html)
  * [CommandBuffer.DisableShaderKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DisableShaderKeyword.html)
  * [CommandBuffer.DispatchCompute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DispatchCompute.html)
  * [CommandBuffer.EnableShaderKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.EnableShaderKeyword.html)
  * [CommandBuffer.EndSample](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.EndSample.html)
  * [CommandBuffer.GetTemporaryRT](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.GetTemporaryRT.html)
  * [CommandBuffer.GetTemporaryRTArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.GetTemporaryRTArray.html)
  * [CommandBuffer.IssuePluginEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.IssuePluginEvent.html)
  * [CommandBuffer.ReleaseTemporaryRT](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.ReleaseTemporaryRT.html)
  * CommandBuffer.SetComputeBufferData
  * [CommandBuffer.SetComputeBufferParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeBufferParam.html)
  * [CommandBuffer.SetComputeFloatParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeFloatParam.html)
  * [CommandBuffer.SetComputeFloatParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeFloatParams.html)
  * [CommandBuffer.SetComputeIntParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeIntParam.html)
  * [CommandBuffer.SetComputeIntParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeIntParams.html)
  * [CommandBuffer.SetComputeMatrixArrayParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeMatrixArrayParam.html)
  * [CommandBuffer.SetComputeMatrixParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeMatrixParam.html)
  * [CommandBuffer.SetComputeTextureParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeTextureParam.html)
  * [CommandBuffer.SetComputeVectorParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeVectorParam.html)
  * [CommandBuffer.SetComputeVectorArrayParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeVectorArrayParam.html)
  * [CommandBuffer.SetGlobalBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetGlobalBuffer.html)
  * [CommandBuffer.SetGlobalColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetGlobalColor.html)
  * [CommandBuffer.SetGlobalFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetGlobalFloat.html)
  * [CommandBuffer.SetGlobalFloatArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetGlobalFloatArray.html)
  * [CommandBuffer.SetGlobalInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetGlobalInt.html)
  * [CommandBuffer.SetGlobalMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetGlobalMatrix.html)
  * [CommandBuffer.SetGlobalMatrixArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetGlobalMatrixArray.html)
  * [CommandBuffer.SetGlobalTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetGlobalTexture.html)
  * [CommandBuffer.SetGlobalVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetGlobalVector.html)
  * [CommandBuffer.SetGlobalVectorArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetGlobalVectorArray.html)
  * CommandBuffer.WaitOnGraphicsFence


These commands are guaranteed to be executed on the same queue. If the target platform does not support async compute queues then Unity dispatches the work on the graphics queue.  
  
Additional resources: [SystemInfo.supportsAsyncCompute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsAsyncCompute.html), GPUFence, [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).
* * *

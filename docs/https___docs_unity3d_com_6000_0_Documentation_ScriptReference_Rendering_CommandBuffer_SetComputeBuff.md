* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeBufferParam.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).SetComputeBufferParam
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
public void SetComputeBufferParam([ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader, int kernelIndex, string name, [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) buffer); 
## Declaration
public void SetComputeBufferParam([ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader, int kernelIndex, int nameID, [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) buffer); 
## Declaration
public void SetComputeBufferParam([ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader, int kernelIndex, string name, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) buffer); 
## Declaration
public void SetComputeBufferParam([ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader, int kernelIndex, int nameID, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) buffer); 
## Declaration
public void SetComputeBufferParam([ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader, int kernelIndex, int nameID, [GraphicsBufferHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBufferHandle.html) bufferHandle); 
## Declaration
public void SetComputeBufferParam([ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader, int kernelIndex, string name, [GraphicsBufferHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBufferHandle.html) bufferHandle); 
### Parameters
Parameter | Description  
---|---  
computeShader |  [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) to set parameter for.  
kernelIndex | Which kernel the buffer is being set for. See [ComputeShader.FindKernel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.FindKernel.html).  
name | Name of the buffer variable in shader code.  
nameID | Property name ID. Use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get this ID.  
buffer | Buffer to set.  
bufferHandle | The handle of the buffer to set.  
### Description
Adds a command to set an input or output buffer parameter on a [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html).
Buffers and textures are set per-kernel. Use [ComputeShader.FindKernel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.FindKernel.html) to find kernel index by function name.  
  
Setting a compute buffer to a kernel will leave the append/consume counter value unchanged. To set or reset the value, use [ComputeBuffer.SetCounterValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.SetCounterValue.html) or [GraphicsBuffer.SetCounterValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.SetCounterValue.html).  
  
Additional resources: [DispatchCompute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DispatchCompute.html), [SetComputeFloatParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeFloatParam.html), [SetComputeFloatParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeFloatParams.html), [SetComputeIntParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeIntParam.html), [SetComputeIntParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeIntParams.html), [SetComputeMatrixParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeMatrixParam.html), [SetComputeMatrixArrayParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeMatrixArrayParam.html), [SetComputeVectorParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeVectorParam.html), [SetComputeVectorArrayParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeVectorArrayParam.html), [SetComputeTextureParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetComputeTextureParam.html).
* * *

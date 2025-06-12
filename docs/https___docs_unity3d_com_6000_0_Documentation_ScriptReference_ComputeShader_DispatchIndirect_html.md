* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.DispatchIndirect.html

#  [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html).DispatchIndirect
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html "Go to ComputeShader Component in the Manual")
## Declaration
public void DispatchIndirect(int kernelIndex, [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) argsBuffer, uint argsOffset = 0); 
## Declaration
public void DispatchIndirect(int kernelIndex, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) argsBuffer, uint argsOffset = 0); 
### Parameters
Parameter | Description  
---|---  
kernelIndex | Which kernel to execute. A single compute shader asset can have multiple kernel entry points.  
argsBuffer | Buffer with dispatch arguments.  
argsOffset | The byte offset into the buffer, where the draw arguments start.  
### Description
Execute a compute shader.
This function "runs" the compute shader, with the given work size read directly from the GPU. Typical use case is generating arbitrary amount of data from a [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) and then dispatching that, without requiring a readback to the CPU.  
  
Buffer with arguments, `argsBuffer`, has to have three integer numbers at given `argsOffset` offset: number of work groups in X dimension, number of work groups in Y dimension, number of work groups in Z dimension.  
  
Within each work group, a number of shader invocations ("threads") are done. The work group size is specified in the compute shader itself (using "numthreads" HLSL attribute), and the total amount of compute shader invocations is thus group count multiplied by the thread group size. Work group size can be queried using [GetKernelThreadGroupSizes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.GetKernelThreadGroupSizes.html) function.  
  
This very much maps to Direct3D11 DispatchIndirect, OpenGL glDispatchComputeIndirect and equivalent functions on other graphics APIs.  
  
Additional resources: [Dispatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.Dispatch.html), [Graphics.DrawProceduralIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawProceduralIndirect.html), [ComputeBuffer.CopyCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.CopyCount.html), [Compute Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html).
* * *

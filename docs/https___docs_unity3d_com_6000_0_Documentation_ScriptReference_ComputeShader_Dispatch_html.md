* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.Dispatch.html

#  [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html).Dispatch
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
public void Dispatch(int kernelIndex, int threadGroupsX, int threadGroupsY, int threadGroupsZ); 
### Parameters
Parameter | Description  
---|---  
kernelIndex | Which kernel to execute. A single compute shader asset can have multiple kernel entry points.  
threadGroupsX | Number of work groups in the X dimension.  
threadGroupsY | Number of work groups in the Y dimension.  
threadGroupsZ | Number of work groups in the Z dimension.  
### Description
Execute a compute shader.
This functions "runs" the compute shader, launching the indicated number of compute shader thread groups in the X, Y and Z dimensions. Within each work group, a number of shader invocations ("threads") are made. The work group size is specified in the compute shader itself (using "numthreads" HLSL attribute), and the total amount of compute shader invocations is thus group count multiplied by the thread group size. Work group size can be queried using [GetKernelThreadGroupSizes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.GetKernelThreadGroupSizes.html) function.  
  
Additional resources: [FindKernel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.FindKernel.html), [GetKernelThreadGroupSizes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.GetKernelThreadGroupSizes.html), [DispatchIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.DispatchIndirect.html), [Compute Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html).
* * *

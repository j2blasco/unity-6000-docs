* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.GetKernelThreadGroupSizes.html

#  [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html).GetKernelThreadGroupSizes
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
public void GetKernelThreadGroupSizes(int kernelIndex, out uint x, out uint y, out uint z); 
### Parameters
Parameter | Description  
---|---  
kernelIndex | Which kernel to query. A single compute shader asset can have multiple kernel entry points.  
x | Thread group size in the X dimension.  
y | Thread group size in the Y dimension.  
z | Thread group size in the Z dimension.  
### Description
Get kernel thread group sizes.
Work group size for each compute shader kernel is specified in the shader code itself (using "numthreads" HLSL attribute). Use this function to query it.  
  
Additional resources: [Dispatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.Dispatch.html), [FindKernel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.FindKernel.html), [Compute Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html).
* * *

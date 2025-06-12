* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-computeSubGroupSize.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).computeSubGroupSize
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
computeSubGroupSize; 
### Description
Size of the compute thread group that supports efficient memory sharing on the GPU (Read Only).
The most efficient thread group size for a set of compute shader calls. This value takes synchronization and shared data into account. This value is a subset of the total workgroup size. It is also known as a "warp" or a "wavefront".  
  
Additional resources:[ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) class, [supportsComputeShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsComputeShaders.html).
* * *

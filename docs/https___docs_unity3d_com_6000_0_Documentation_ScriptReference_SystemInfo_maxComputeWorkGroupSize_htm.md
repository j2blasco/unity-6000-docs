* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxComputeWorkGroupSize.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).maxComputeWorkGroupSize
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
maxComputeWorkGroupSize; 
### Description
The largest total number of invocations in a single local work group that can be dispatched to a compute shader (Read Only).
The product of SystemInfo.maxComputeWorkgroupSizeX, SystemInfo.maxComputeWorkgroupSizeY and SystemInfo.maxComputeWorkgroupSizeZ cannot exceed this number on the current device. Note that this is the theoretical maximum. The actual limit depends on the shader complexity, so it can be lower.  
  
Additional resources:[SystemInfo.maxComputeWorkGroupSizeX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxComputeWorkGroupSizeX.html) [SystemInfo.maxComputeWorkGroupSizeY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxComputeWorkGroupSizeY.html) [SystemInfo.maxComputeWorkGroupSizeZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxComputeWorkGroupSizeZ.html)
* * *

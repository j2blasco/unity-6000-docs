* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.Counter.html

#  [ComputeBufferType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.html).Counter
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
### Description
[ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) with a counter.
Adds a "counter" to a `RWStructuredBuffer` and allows using `IncrementCounter` / `DecrementCounter` HLSL functions on it.  
  
The `stride` passed when constructing the buffer must match structure size, be a multiple of 4 and less than 2048.  
  
See Microsoft's HLSL documentation on [IncrementCounter](https://msdn.microsoft.com/en-us/library/windows/desktop/ff471497.aspx) and [DecrementCounter](https://msdn.microsoft.com/en-us/library/windows/desktop/ff471495.aspx).  
  
The buffer size value can be copied into another buffer using [ComputeBuffer.CopyCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.CopyCount.html), or explicitly reset with [ComputeBuffer.SetCounterValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.SetCounterValue.html).  
  
Additional resources: [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html), [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html), [Material.SetBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetBuffer.html).
* * *

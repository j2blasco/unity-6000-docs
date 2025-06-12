* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.Append.html

#  [ComputeBufferType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.html).Append
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
Append-consume [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) type.
Allows a buffer to be treated like a stack in compute shaders. Maps to `AppendStructuredBuffer<T>` or `ConsumeStructuredBuffer<T>` in HLSL.  
  
The `stride` passed when constructing the buffer must match structure size, be a multiple of 4 and less than 2048.  
  
See Microsoft's HLSL documentation on [AppendStructuredBuffer](https://learn.microsoft.com/en-gb/windows/win32/direct3dhlsl/sm5-object-appendstructuredbuffer) and [ConsumeStructuredBuffer](https://learn.microsoft.com/en-gb/windows/win32/direct3dhlsl/sm5-object-consumestructuredbuffer).  
  
The buffer size value can be copied into another buffer using [ComputeBuffer.CopyCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.CopyCount.html), or explicitly reset with [ComputeBuffer.SetCounterValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.SetCounterValue.html).  
  
Additional resources: [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html), [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html), [Material.SetBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetBuffer.html).
* * *

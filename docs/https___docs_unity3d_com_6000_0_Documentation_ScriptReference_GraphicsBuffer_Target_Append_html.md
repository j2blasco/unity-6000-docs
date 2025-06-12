* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Append.html

#  [GraphicsBuffer.Target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.html).Append
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
GraphicsBuffer can be used as an append-consume buffer.
Allows a buffer to be treated like a stack in compute shaders. Maps to `AppendStructuredBuffer<T>` or `ConsumeStructuredBuffer<T>` in HLSL.  
  
When you construct a GraphicsBuffer of this type, the value of `stride` must match the stride of the corresponding StructuredBuffer struct type in your HLSL code. It must also be a multiple of 4, and less than 2048.  
  
See Microsoft's HLSL documentation on [AppendStructuredBuffer](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/sm5-object-appendstructuredbuffer) and [ConsumeStructuredBuffer](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/sm5-object-consumestructuredbuffer).  
  
The buffer size value can be copied into another buffer using [GraphicsBuffer.CopyCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.CopyCount.html), or explicitly reset with [GraphicsBuffer.SetCounterValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.SetCounterValue.html).  
  
Additional resources: [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html), [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html), [Material.SetBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetBuffer.html).
* * *

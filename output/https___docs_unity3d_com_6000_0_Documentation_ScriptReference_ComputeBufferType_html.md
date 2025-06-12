* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.html

# ComputeBufferType
enumeration
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
[ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) type.
Different types of compute buffers map to different usage and declarations in HLSL shaders. Default type is "structured buffer" (`StructuredBuffer<T>` or `RWStructuredBuffer<T>`).  
  
Additional resources: [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html), [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html), [Material.SetBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetBuffer.html).
### Properties
Property | Description  
---|---  
[Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.Default.html) | Default ComputeBuffer type (structured buffer).  
[Raw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.Raw.html) | Raw ComputeBuffer type (byte address buffer).  
[Append](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.Append.html) | Append-consume ComputeBuffer type.  
[Counter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.Counter.html) |  ComputeBuffer with a counter.  
[Constant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.Constant.html) |  ComputeBuffer that you can use as a constant buffer (uniform buffer).  
[Structured](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.Structured.html) |  ComputeBuffer that you can use as a structured buffer.  
[IndirectArguments](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.IndirectArguments.html) |  ComputeBuffer used for Graphics.DrawProceduralIndirect, ComputeShader.DispatchIndirect or Graphics.DrawMeshInstancedIndirect arguments.  
* * *

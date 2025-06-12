* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.Structured.html

#  [ComputeBufferType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.html).Structured
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
[ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) that you can use as a structured buffer.
This is otherwise identical to [ComputeBufferType.Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.Default.html) except that if any other [ComputeBufferType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.html) flags are used, the resulting ComputeBuffer will not be able to be bound as a structured buffer unless [ComputeBufferType.Structured](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.Structured.html) is explicitly added.  
  
When you construct a ComputeBuffer of this type, the value of `stride` must match the stride of the corresponding `StructuredBuffer` struct type in your HLSL code.  
  
The value of `stride` must also be a multiple of 4, and less than 2048.  
  
To meet requirements on some platforms and avoid performance issues, `stride` should be a multiple of 16. Use float4 and float4x4 variables to create a multiple of 16, and put smaller variables inside them. Avoid the use of 'padding' variables to create a multiple of 16, for example using a float3 variable to pad a struct containing a single float, because some data types may be different sizes on different platforms.  
  
If you use a mix of variable sizes, the data layout of a shader's structured buffer may be different depending on the graphics API. This means [ComputeShader.SetBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetBuffer.html) or [Material.SetBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetBuffer.html) might overwrite data or set variables to the wrong values. See [Writing shaders for different graphics APIs](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PlatformDifferences.html) for more information. 
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.Constant.html

#  [ComputeBufferType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.html).Constant
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
[ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) that you can use as a constant buffer (uniform buffer).
If you use this flag, you can use the [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) as a parameter to [ComputeShader.SetConstantBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetConstantBuffer.html) and [Material.SetConstantBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetConstantBuffer.html). If you also need the buffer to be bound as a structured buffer, you must add the ComputeBufferType.StructuredBuffer flag. Some renderers (such as DX11) do not support binding buffers as both constant and structured buffers.  
  
The data layout of a shader's constant buffer may be different depending on the graphics API. This means [ComputeShader.SetConstantBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetConstantBuffer.html) or [Material.SetConstantBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetConstantBuffer.html) might overwrite data or set variables to the wrong values. See [Writing shaders for different graphics APIs](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PlatformDifferences.html) for more information. 
* * *

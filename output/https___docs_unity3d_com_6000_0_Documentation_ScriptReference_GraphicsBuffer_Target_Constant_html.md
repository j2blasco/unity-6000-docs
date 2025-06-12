* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Constant.html

#  [GraphicsBuffer.Target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.html).Constant
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
GraphicsBuffer can be used as a constant buffer (uniform buffer).
If you use this target, you can use the [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) as a parameter to [ComputeShader.SetConstantBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetConstantBuffer.html) and [Material.SetConstantBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetConstantBuffer.html).  
  
If you also need the buffer to be bound as a structured buffer, you must add the [GraphicsBuffer.Target.Structured](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Structured.html) flag. Some renderers (such as DX11) do not support binding buffers as both constant and structured buffers.  
  
The data layout of a shader's constant buffer may be different depending on the graphics API. This means [ComputeShader.SetConstantBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetConstantBuffer.html) or [Material.SetConstantBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetConstantBuffer.html) might overwrite data or set variables to the wrong values. See [Writing shaders for different graphics APIs](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PlatformDifferences.html) for more information. 
* * *

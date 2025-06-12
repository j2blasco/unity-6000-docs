* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.IndirectArguments.html

#  [ComputeBufferType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.html).IndirectArguments
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
[ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) used for [Graphics.DrawProceduralIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawProceduralIndirect.html), [ComputeShader.DispatchIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.DispatchIndirect.html) or [Graphics.DrawMeshInstancedIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshInstancedIndirect.html) arguments.
Buffer size has to be at least 12 bytes. Underlying DX11 unordered access view format will be R32_UINT, and shader resource view format will be R32 typeless.  
  
Additional resources: [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html), [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html), [Material.SetBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetBuffer.html), [ComputeBuffer.CopyCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.CopyCount.html).
* * *

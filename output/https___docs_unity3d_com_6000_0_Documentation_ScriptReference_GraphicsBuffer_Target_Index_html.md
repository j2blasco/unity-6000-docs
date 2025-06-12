* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Index.html

#  [GraphicsBuffer.Target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.html).Index
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
GraphicsBuffer can be used as an index buffer.
Allows a buffer to be used as an index buffer for [Graphics.DrawProcedural](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawProcedural.html) and similar low level drawing APIs.  
  
When you construct a GraphicsBuffer of this type, the value of `stride` must be either 2 (16-bit indices) or 4 (32-bit indices).  
  
DirectX 11 does not allow `Index` buffers to also be [Structured](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Structured.html). For compute shader mesh data access with DirectX 11 compatibility, it is best to use [Raw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Raw.html).  
  
Additional resources: [Graphics.RenderPrimitivesIndexed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderPrimitivesIndexed.html), [Graphics.RenderPrimitivesIndexedIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderPrimitivesIndexedIndirect.html), [CommandBuffer.DrawProcedural](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DrawProcedural.html), [CommandBuffer.DrawProceduralIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DrawProceduralIndirect.html), [Mesh.indexBufferTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-indexBufferTarget.html), [Mesh.GetIndexBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetIndexBuffer.html).
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.html

# Target
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
The intended targets for GraphicsBuffer.
Provide the intended targets ([target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer-target.html)) when creating a GraphicsBuffer. For example, pass [GraphicsBuffer.Target.Index](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Index.html) for a buffer to be usable as a geometry index buffer.  
  
Different platforms and devices might or might not support different targets. Any target values different from [Vertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Vertex.html), [Index](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Index.html) or [Constant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Constant.html) require the compute shader support (see [SystemInfo.supportsComputeShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsComputeShaders.html)).  
  
You can combine values in this enum. For example, `GraphicsBuffer.Target.Index | GraphicsBuffer.Target.Raw` creates a buffer that can be used both as an index buffer in a [Graphics.DrawProcedural](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawProcedural.html) call, and as a raw byte address buffer in a compute shader.  
  
DirectX 11 does not allow [Index](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Index.html) or [Vertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Vertex.html) buffers to also be [Structured](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Structured.html). For compute shader mesh data access with DirectX 11 compatibility, use [Raw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Raw.html).  
  
Additional resources: [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) class, [GraphicsBuffer constructor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer-ctor.html), [Mesh.vertexBufferTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertexBufferTarget.html), [Mesh.indexBufferTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-indexBufferTarget.html).
### Properties
Property | Description  
---|---  
[Vertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Vertex.html) | GraphicsBuffer can be used as a vertex buffer.  
[Index](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Index.html) | GraphicsBuffer can be used as an index buffer.  
[CopySource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.CopySource.html) | GraphicsBuffer can be used as a source for CopyBuffer.  
[CopyDestination](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.CopyDestination.html) | GraphicsBuffer can be used as a destination for CopyBuffer.  
[Structured](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Structured.html) | GraphicsBuffer can be used as a structured buffer.  
[Raw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Raw.html) | GraphicsBuffer can be used as a raw byte-address buffer.  
[Append](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Append.html) | GraphicsBuffer can be used as an append-consume buffer.  
[Counter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Counter.html) | GraphicsBuffer with an internal counter.  
[IndirectArguments](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.IndirectArguments.html) | GraphicsBuffer can be used as an indirect argument buffer for indirect draws and dispatches.  
[Constant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Constant.html) | GraphicsBuffer can be used as a constant buffer (uniform buffer).  
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawProceduralNow.html

#  [Graphics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html).DrawProceduralNow
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
## Declaration
public static void DrawProceduralNow([MeshTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.html) topology, int vertexCount, int instanceCount); 
### Parameters
Parameter | Description  
---|---  
topology | Topology of the procedural geometry.  
vertexCount | Vertex count to render.  
instanceCount | Instance count to render.  
### Description
Draws procedural geometry on the GPU.
DrawProceduralNow does a draw call on the GPU, without any vertex or index buffers. If the shader requires vertex buffers, one of the following occurs depending on platform: - If the vertex buffer is declared but the compiler can optimize it away, the normal DrawProcedural call occurs. - If the compiler is not able to optimize the vertex buffer declaration away, the draw call will be converted into a normal mesh drawing call with emulated vertex buffers injected.  
  
The latter option has performance overhead so it is recommended not to declare vertex inputs in shaders when using DrawProceduralNow. This is mainly useful on [Shader Model 4.5](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompileTargets.html) level hardware where shaders can read arbitrary data from [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) buffers.  
  
Note that this call executes immediately, similar to [Graphics.DrawMeshNow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshNow.html). It uses the currently set render target, transformation matrices and shader pass.  
  
There's also similar functionality in CommandBuffers, see [CommandBuffer.DrawProcedural](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DrawProcedural.html).  
  
Additional resources: [Graphics.DrawProceduralIndirectNow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawProceduralIndirectNow.html), [SystemInfo.supportsInstancing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsInstancing.html).
* * *
## Declaration
public static void DrawProceduralNow([MeshTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.html) topology, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) indexBuffer, int indexCount, int instanceCount); 
### Parameters
Parameter | Description  
---|---  
topology | Topology of the procedural geometry.  
indexCount | Index count to render.  
instanceCount | Instance count to render.  
indexBuffer | Index buffer used to submit vertices to the GPU.  
### Description
Draws procedural geometry on the GPU.
DrawProceduralNow does a draw call on the GPU, without a vertex buffer. This is mainly useful on [Shader Model 4.5](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompileTargets.html) level hardware where shaders can read arbitrary data from [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) buffers.  
  
Note that this call executes immediately, similar to [Graphics.DrawMeshNow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshNow.html). It uses the currently set render target, transformation matrices and shader pass.  
  
There's also similar functionality in CommandBuffers, see [CommandBuffer.DrawProcedural](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DrawProcedural.html).  
  
Additional resources: [Graphics.DrawProceduralIndirectNow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawProceduralIndirectNow.html), [SystemInfo.supportsInstancing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsInstancing.html).
* * *

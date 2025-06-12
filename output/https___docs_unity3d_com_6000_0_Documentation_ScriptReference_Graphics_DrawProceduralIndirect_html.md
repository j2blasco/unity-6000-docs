* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawProceduralIndirect.html

#  [Graphics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html).DrawProceduralIndirect
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
public static void DrawProceduralIndirect([Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds, [MeshTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.html) topology, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) bufferWithArgs, int argsOffset, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) properties, [Rendering.ShadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastingMode.html) castShadows, bool receiveShadows, int layer); 
## Declaration
public static void DrawProceduralIndirect([Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds, [MeshTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.html) topology, [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) bufferWithArgs, int argsOffset, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) properties, [Rendering.ShadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastingMode.html) castShadows, bool receiveShadows, int layer); 
### Parameters
Parameter | Description  
---|---  
material |  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) to use.  
bounds | The bounding volume surrounding the instances you intend to draw.  
topology | Topology of the procedural geometry.  
camera | If `null` (default), the mesh will be drawn in all cameras. Otherwise it will be rendered in the given Camera only.  
bufferWithArgs | Buffer with draw arguments.  
argsOffset | Byte offset where in the buffer the draw arguments are.  
properties | Additional material properties to apply onto material just before this mesh will be drawn. See [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).  
castShadows | Determines whether the mesh can cast shadows.  
receiveShadows | Determines whether the mesh can receive shadows.  
layer |  [Layer](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) to use.  
### Description
Draws procedural geometry on the GPU.
This function is now obsolete. For non-indexed rendering, use RenderPrimitivesIndirect instead. For indexed rendering, use RenderPrimitivesIndexedIndirect.  
  
This function only works on platforms that support [compute shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html).  
  
DrawProceduralIndirect does a draw call on the GPU, without any vertex or index buffers. If the shader requires vertex buffers one of the following occurs depending on platform: If the vertex buffer is declared but compiler can optimize it away then the normal DrawProcedural call will occur. If the compiler is not able to optimize the vertex buffer declaration away then this will be converted into a normal mesh drawing call with emulated vertexbuffers injected. The latter option has performance overhead so it is recommended not to declare vertex inputs in shaders when using DrawProceduralIndirect. The amount of geometry to draw is read from a [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html). Typical use case is generating an arbitrary amount of data from a [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) and then rendering that, without requiring a readback to the CPU.  
  
This is mainly useful on [Shader Model 4.5](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompileTargets.html) level hardware where shaders can read arbitrary data from [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) buffers.  
  
Buffer with arguments, `bufferWithArgs`, has to have four integer numbers at given `argsOffset` offset: vertex count per instance, instance count, start vertex location, and start instance location. This maps to Direct3D11 DrawInstancedIndirect and equivalent functions on other graphics APIs. On OpenGL versions before 4.2 and all OpenGL ES versions that support indirect draw, the last argument is reserved and therefore must be zero.  
  
There's also similar functionality in CommandBuffers, see [CommandBuffer.DrawProceduralIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DrawProceduralIndirect.html).  
  
Additional resources: [Graphics.RenderPrimitivesIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderPrimitivesIndirect.html), [Graphics.RenderPrimitivesIndexedIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderPrimitivesIndexedIndirect.html), [Graphics.DrawProcedural](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawProcedural.html), [ComputeBuffer.CopyCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.CopyCount.html), [SystemInfo.supportsComputeShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsComputeShaders.html).
* * *
## Declaration
public static void DrawProceduralIndirect([Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds, [MeshTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.html) topology, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) indexBuffer, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) bufferWithArgs, int argsOffset, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) properties, [Rendering.ShadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastingMode.html) castShadows, bool receiveShadows, int layer); 
## Declaration
public static void DrawProceduralIndirect([Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds, [MeshTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.html) topology, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) indexBuffer, [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) bufferWithArgs, int argsOffset, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) properties, [Rendering.ShadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastingMode.html) castShadows, bool receiveShadows, int layer); 
### Parameters
Parameter | Description  
---|---  
material |  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) to use.  
bounds | The bounding volume surrounding the instances you intend to draw.  
topology | Topology of the procedural geometry.  
indexBuffer | Index buffer used to submit vertices to the GPU.  
camera | If `null` (default), the mesh will be drawn in all cameras. Otherwise it will be rendered in the given Camera only.  
bufferWithArgs | Buffer with draw arguments.  
argsOffset | Byte offset where in the buffer the draw arguments are.  
properties | Additional material properties to apply onto material just before this mesh will be drawn. See [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).  
castShadows | Determines whether the mesh can cast shadows.  
receiveShadows | Determines whether the mesh can receive shadows.  
layer |  [Layer](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) to use.  
### Description
Draws procedural geometry on the GPU.
DrawProceduralIndirect does a draw call on the GPU, without a vertex buffer. The amount of geometry to draw is read from a [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html). Typical use case is generating an arbitrary amount of data from a [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) and then rendering that, without requiring a readback to the CPU.  
  
This is mainly useful on [Shader Model 4.5](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompileTargets.html) level hardware where shaders can read arbitrary data from [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) buffers.  
  
Buffer with arguments, `bufferWithArgs`, has to have five integer numbers at given `argsOffset` offset: index count per instance, instance count, start index location, base vertex location, and start instance location. This maps to Direct3D11 DrawIndexedInstancedIndirect and equivalent functions on other graphics APIs. On OpenGL versions before 4.2 and all OpenGL ES versions that support indirect draw, the last argument is reserved and therefore must be zero.  
  
There's also similar functionality in CommandBuffers, see [CommandBuffer.DrawProceduralIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DrawProceduralIndirect.html).  
  
Additional resources: [Graphics.DrawProcedural](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawProcedural.html), [ComputeBuffer.CopyCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.CopyCount.html), [SystemInfo.supportsComputeShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsComputeShaders.html).
* * *

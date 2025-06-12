* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DrawProcedural.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).DrawProcedural
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
public void DrawProcedural([Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) matrix, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, int shaderPass, [MeshTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.html) topology, int vertexCount, int instanceCount = 1, [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) properties = null); 
### Parameters
Parameter | Description  
---|---  
matrix | Transformation matrix to use.  
material | Material to use.  
shaderPass | Which pass of the shader to use (or -1 for all passes).  
topology | Topology of the procedural geometry.  
vertexCount | Vertex count to render.  
instanceCount | Instance count to render.  
properties | Additional material properties to apply just before rendering. See [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).  
### Description
Add a "draw procedural geometry" command.
When the command buffer executes, this will do a draw call on the GPU, without any vertex or index buffers. This is mainly useful on [Shader Model 4.5](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompileTargets.html) level hardware where shaders can read arbitrary data from [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) buffers.  
  
In the vertex shader, you'd typically use the SV_VertexID and SV_InstanceID input variables to fetch data from some buffers.  
  
Note that the draw call will not have any lighting related shader data (light colors, directions, shadows, light and reflection probes etc.) set up. If the shader used by the material uses any lighting related variables, the results are undefined.  
  
Additional resources: [DrawProceduralIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DrawProceduralIndirect.html), [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html), [Graphics.DrawProcedural](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawProcedural.html).
* * *
## Declaration
public void DrawProcedural([GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) indexBuffer, [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) matrix, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, int shaderPass, [MeshTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.html) topology, int indexCount, int instanceCount, [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) properties); 
## Declaration
public void DrawProcedural([GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) indexBuffer, [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) matrix, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, int shaderPass, [MeshTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.html) topology, int indexCount, int instanceCount); 
## Declaration
public void DrawProcedural([GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) indexBuffer, [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) matrix, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, int shaderPass, [MeshTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.html) topology, int indexCount); 
### Parameters
Parameter | Description  
---|---  
matrix | Transformation matrix to use.  
material | Material to use.  
shaderPass | Which pass of the shader to use (or -1 for all passes).  
topology | Topology of the procedural geometry.  
indexCount | Index count to render.  
instanceCount | Instance count to render.  
indexBuffer | The index buffer used to submit vertices to the GPU.  
properties | Additional material properties to apply just before rendering. See [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).  
### Description
Add a "draw procedural geometry" command.
When the command buffer executes, this will do a draw call on the GPU, without a vertex buffer. This is mainly useful on [Shader Model 4.5](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompileTargets.html) level hardware where shaders can read arbitrary data from [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) buffers.  
  
In the vertex shader, you'd typically use the SV_VertexID and SV_InstanceID input variables to fetch data from some buffers.  
  
Additional resources: [DrawProceduralIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DrawProceduralIndirect.html), [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html), [Graphics.DrawProcedural](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawProcedural.html).
* * *

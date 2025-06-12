* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexBuffer.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).GetVertexBuffer
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html "Go to Mesh Component in the Manual")
## Declaration
public [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) GetVertexBuffer(int index); 
### Parameters
Parameter | Description  
---|---  
index | Vertex data stream index to get the buffer for.  
### Returns
**GraphicsBuffer** The mesh vertex buffer as a [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html). 
### Description
Retrieves a [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) that provides direct acces to the GPU vertex buffer.
Most of the `Mesh` methods work on a CPU copy of the mesh data, which Unity then uploads to the GPU. For example, [SetIndexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferData.html) modifies CPU copy of the data, and [UploadMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.UploadMeshData.html) sends the CPU copy of the data to the GPU.  
  
You can access the GPU copy of the vertex buffer directly using `GetVertexBuff`. This allows more direct manipulation of the mesh index data on the GPU, which can potentially improve performance. However, any modifications that you make to the index data this way will not be reflected in the CPU copy of the mesh data.  
  
You can also use this method to make the vertex buffer available for reading or writing in a [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html). To do that, first request an appropriate buffer binding target via [vertexBufferTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertexBufferTarget.html), then get the mesh data using `GetVertexBuffer`, and then set it up as a parameter for your shaders using ComputeBuffer.SetBuffer, [Material.SetBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetBuffer.html) and similar methods.  
  
[GetVertexBufferStride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexBufferStride.html), [GetVertexAttributeOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttributeOffset.html) and related methods can be used to query the exact mesh vertex data layout and format, so that the compute shader can access it properly.  
  
If you modify the CPU copy of the data, this can cause the GPU vertex buffers to be re-created; in that case, you must call `GetVertexBuffer` again.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh;
    public ComputeShader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader;
    void Start()
    {
        // Mark the vertex buffer as needing "Raw"
        // (ByteAddressBuffer, RWByteAddressBuffer in HLSL shaders)
        // access.
        mesh.vertexBufferTarget |= GraphicsBuffer.Target.Raw[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Raw.html);
        // Get the vertex buffer of the Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html), and set it up
        // as a buffer parameter to a compute shader.
        var vertexBuffer = mesh.GetVertexBuffer(0);
        computeShader.SetBuffer(0, "MeshVertexBuffer", vertexBuffer);
        vertexBuffer.Dispose();
    }
}

```

Additional resources: [GetIndexBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetIndexBuffer.html), [vertexBufferTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertexBufferTarget.html).
* * *

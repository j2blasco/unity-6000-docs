* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetIndexBuffer.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).GetIndexBuffer
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
public [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) GetIndexBuffer(); 
### Returns
**GraphicsBuffer** The mesh index buffer as a [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html). 
### Description
Retrieves a [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) to the GPU index buffer.
Most of the `Mesh` methods work on a CPU copy of the mesh data, which Unity then uploads to the GPU. For example, [SetIndexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferData.html) modifies CPU copy of the data, and [UploadMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.UploadMeshData.html) sends the CPU copy of the data to the GPU.  
  
You can access the GPU copy of the index buffer directly using `GetIndexBuffer`. This allows more direct manipulation of the mesh index data on the GPU, which can potentially improve performance. However, any modifications that you make to the index data this way will not be reflected in the CPU copy of the mesh data.  
  
You can also use this method to make the index buffer available for reading or writing in a [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html). To do that, first request an appropriate buffer binding target via [indexBufferTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-indexBufferTarget.html), then get the mesh data using `GetIndexBuffer`, and then set it up as a parameter for your shaders using ComputeBuffer.SetBuffer, [Material.SetBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetBuffer.html) and similar methods.  
  
If you modify the CPU copy of the data, this can cause the GPU index buffer to be re-created; in that case, you must call `GetIndexBuffer` again.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh;
    public ComputeShader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader;
    void Start()
    {
        // Mark the index buffer as needing "Raw"
        // (ByteAddressBuffer, RWByteAddressBuffer in HLSL shaders)
        // access.
        mesh.indexBufferTarget |= GraphicsBuffer.Target.Raw[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Raw.html);
        // Get the index buffer of the Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html), and set it up
        // as a buffer parameter to a compute shader.
        var indexBuffer = mesh.GetIndexBuffer();
        computeShader.SetBuffer(0, "MeshIndexBuffer", indexBuffer);
        indexBuffer.Dispose();
    }
}

```

Additional resources: [GetVertexBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexBuffer.html), [indexBufferTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-indexBufferTarget.html).
* * *

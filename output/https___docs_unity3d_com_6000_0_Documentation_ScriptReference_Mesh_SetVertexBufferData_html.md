* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferData.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).SetVertexBufferData
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
public void SetVertexBufferData(NativeArray<T> data, int dataStart, int meshBufferStart, int count, int stream, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags); 
## Declaration
public void SetVertexBufferData(T[] data, int dataStart, int meshBufferStart, int count, int stream, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags); 
## Declaration
public void SetVertexBufferData(List<T> data, int dataStart, int meshBufferStart, int count, int stream, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags); 
### Parameters
Parameter | Description  
---|---  
data | Vertex data array.  
dataStart | The first element in the data to copy from.  
meshBufferStart | The first element in mesh vertex buffer to receive the data.  
count | Number of vertices to copy.  
stream | Vertex buffer stream to set data for (default 0). Value must be within range 0 to 3.  
flags | Flags controlling the function behavior, see [MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html).  
### Description
Sets the data of the vertex buffer of the Mesh.
Simple usage of [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) scripting API involves using functions like [vertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertices.html), [normals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-normals.html) to setup vertex data.  
  
For advanced use cases that require maximum performance, you can use the advanced API, which has functions like [SetSubMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetSubMesh.html), [SetIndexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferParams.html), [SetIndexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferData.html), and [SetVertexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferParams.html). This advanced API gives access to the underlying mesh data structures that primarily work on raw index buffers, vertex buffers and mesh subset data.  
  
You can use `SetVertexBufferData` to set vertex data directly, without using format conversions for each vertex attribute. The supplied data layout has to match the vertex data layout of the mesh (see [SetVertexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferParams.html), [GetVertexAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttributes.html)). Partial updates of the data are also possible, via `dataStart`, `meshBufferStart`, `count` parameters.
```
using UnityEngine;
using UnityEngine.Rendering;
using Unity.Collections;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html) with FP32 position, FP16 2D normal and a 4-byte tangent.
    // In some cases StructLayout attribute needs
    // to be used, to get the data layout match exactly what it needs to be.
    [System.Runtime.InteropServices.StructLayout(System.Runtime.InteropServices.LayoutKind.Sequential)]
    struct ExampleVertex
    {
        public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) pos;
        public ushort normalX, normalY;
        public Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) tangent;
    }  
  
    void Start()
    {
        var mesh = new Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)();
        // specify vertex count and layout
        var layout = new[]
        {
            new VertexAttributeDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor.html)(VertexAttribute.Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Position.html), VertexAttributeFormat.Float32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeFormat.Float32.html), 3),
            new VertexAttributeDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor.html)(VertexAttribute.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Normal.html), VertexAttributeFormat.Float16[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeFormat.Float16.html), 2),
            new VertexAttributeDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor.html)(VertexAttribute.Tangent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Tangent.html), VertexAttributeFormat.UNorm8[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeFormat.UNorm8.html), 4),
        };
        var vertexCount = 10;
        mesh.SetVertexBufferParams(vertexCount, layout);  
  
        // set vertex data
        var verts = new NativeArray<ExampleVertex>(vertexCount, Allocator.Temp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Temp.html));  
  
        // ... fill in vertex array data here...  
  
        mesh.SetVertexBufferData(verts, 0, 0, vertexCount);
    }
}

```

Additional resources: [SetVertexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferParams.html), [SetIndexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferParams.html), [SetIndexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferData.html), [SetSubMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetSubMesh.html), [MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html), [AcquireReadOnlyMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AcquireReadOnlyMeshData.html).
* * *

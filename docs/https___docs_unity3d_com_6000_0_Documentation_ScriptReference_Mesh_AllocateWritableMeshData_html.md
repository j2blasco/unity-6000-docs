* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AllocateWritableMeshData.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).AllocateWritableMeshData
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
public static [Mesh.MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html) AllocateWritableMeshData(int meshCount); 
### Parameters
Parameter | Description  
---|---  
meshCount | The amount of meshes that will be created.  
### Returns
**MeshDataArray** Returns a `MeshDataArray` containing writeable `MeshData` structs. See [MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html) and [MeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshData.html). 
### Description
Allocates data structures for Mesh creation using C# Jobs.
Use [Mesh.AllocateWritableMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AllocateWritableMeshData.html) to obtain a [MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html) of writeable `MeshData` structs. You can access the resulting `MeshDataArray` and `MeshData` structs from any thread. Creating a `MeshDataArray` has some overhead for memory tracking and safety reasons, so it is more efficient to make a single call to [Mesh.AllocateWritableMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AllocateWritableMeshData.html) and request multiple `MeshData` structs in the same `MeshDataArray` than it is to make multiple calls to [Mesh.AllocateWritableMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AllocateWritableMeshData.html). If you use the override that takes a Mesh or Mesh Array as argument you will be returned a copy of an existing Mesh that can be used on a thread.  
  
You can populate writeable `MeshData` structs with data to create new Meshes. Use [Mesh.MeshData.SetVertexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshData.SetVertexBufferParams.html) to set the vertex buffer size and layout, and then write to the array returned by [Mesh.MeshData.GetVertexData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshData.GetVertexData.html) to set the vertices. Use [Mesh.MeshData.SetIndexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshData.SetIndexBufferParams.html) to set the index buffer size and format, and then write to the array returned by [Mesh.MeshData.GetIndexData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshData.GetIndexData.html) to set the indices. Write to [Mesh.MeshData.subMeshCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshData-subMeshCount.html) to set the number of sub meshes, and then use [Mesh.MeshData.SetSubMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshData.SetSubMesh.html) to set sub mesh data.  
  
When you have populated the writeable `MeshData` struct with your data, use [Mesh.ApplyAndDisposeWritableMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.ApplyAndDisposeWritableMeshData.html) to apply the data to [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) objects and automatically dispose of the `MeshDataArray`.
```
using UnityEngine;
using UnityEngine.Rendering;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)))]
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Allocate mesh data for one mesh.
        var dataArray = Mesh.AllocateWritableMeshData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AllocateWritableMeshData.html)(1);
        var data = dataArray[0];  
  
        // Tetrahedron vertices with positions and normals.
        // 4 faces with 3 unique vertices in each -- the faces
        // don't share the vertices since normals have to be
        // different for each face.
        data.SetVertexBufferParams(12,
            new VertexAttributeDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor.html)(VertexAttribute.Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Position.html)),
            new VertexAttributeDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor.html)(VertexAttribute.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Normal.html), stream:1));
        // Four tetrahedron vertex positions:
        var sqrt075 = Mathf.Sqrt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sqrt.html)(0.75f);
        var p0 = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0,0,0);
        var p1 = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1,0,0);
        var p2 = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.5f,0,sqrt075);
        var p3 = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.5f,sqrt075,sqrt075/3);
        // The first vertex buffer data stream is just positions;
        // fill them in.
        var pos = data.GetVertexData<Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)>();
        pos[0] = p0; pos[1] = p1; pos[2] = p2;
        pos[3] = p0; pos[4] = p2; pos[5] = p3;
        pos[6] = p2; pos[7] = p1; pos[8] = p3;
        pos[9] = p0; pos[10] = p3; pos[11] = p1;
        // Note: normals will be calculated later in RecalculateNormals.  
  
        // Tetrahedron index buffer: 4 triangles, 3 indices per triangle.
        // All vertices are unique so the index buffer is just a
        // 0,1,2,...,11 sequence.
        data.SetIndexBufferParams(12, IndexFormat.UInt16[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.IndexFormat.UInt16.html));
        var ib = data.GetIndexData<ushort>();
        for (ushort i = 0; i < ib.Length; ++i)
            ib[i] = i;  
  
        // One sub-mesh with all the indices.
        data.subMeshCount = 1;
        data.SetSubMesh(0, new SubMeshDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubMeshDescriptor.html)(0, ib.Length));  
  
        // Create the mesh and apply data to it:
        var mesh = new Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)();
        mesh.name = "Tetrahedron";
        Mesh.ApplyAndDisposeWritableMeshData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.ApplyAndDisposeWritableMeshData.html)(dataArray, mesh);
        mesh.RecalculateNormals();
        mesh.RecalculateBounds();  
  
        GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().mesh = mesh;
    }
}

```

Additional resources: [ApplyAndDisposeWritableMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.ApplyAndDisposeWritableMeshData.html), [MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html), [MeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshData.html).
* * *

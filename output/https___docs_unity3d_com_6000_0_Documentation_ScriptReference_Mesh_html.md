* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html

# Mesh
class in UnityEngine
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
A class that allows you to create or modify meshes.
Meshes contain vertices and multiple triangle arrays.  
  
Conceptually, all vertex data is stored in separate arrays of the same size. For example, if you have a mesh of 100 Vertices, and want to have a position, normal and two texture coordinates for each vertex, then the mesh should have [vertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertices.html), [normals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-normals.html), [uv](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-uv.html) and [uv2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-uv2.html) arrays, each being 100 in size. Data for i-th vertex is at index "i" in each array.  
  
For every vertex there can be a vertex position, normal, tangent, color and up to 8 texture coordinates. Texture coordinates most often are 2D data ([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)), but it is possible to make them [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) or [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) if needed. This is most often used for holding arbitrary data in mesh vertices, for special effects used in shaders. For skinned meshes, the vertex data can also contain [boneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-boneWeights.html).  
  
The mesh face data, i.e. the triangles it is made of, is simply three vertex indices for each triangle. For example, if the mesh has 10 triangles, then the [triangles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-triangles.html) array should be 30 numbers, with each number indicating which vertex to use. The first three elements in the triangles array are the indices for the vertices that make up that triangle; the second three elements make up another triangle and so on.  
  
Note that while triangle meshes are the most common use case, Unity also supports other mesh topology types, for example Line or Point meshes. For line meshes, each line is composed of two vertex indices and so on. See [SetIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndices.html) and [MeshTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.html).  
  
**Simple vs Advanced Mesh API**  
  
The Mesh class has two sets of methods for assigning data to a Mesh from script. The "simple" set of methods provide a basis for setting the indices, triangle, normals, tangents, etc. These methods include validation checks, for example to ensure that you are not passing in data that would include out-of-bounds indices. They represent the standard way to assign Mesh data from script in Unity.  
  
The "simple" methods are: [SetColors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetColors.html), [SetIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndices.html), [SetNormals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetNormals.html), [SetTangents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetTangents.html), [SetTriangles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetTriangles.html), [SetUVs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetUVs.html), [SetVertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertices.html), [SetBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetBoneWeights.html).  
  
There is also an "advanced" set of methods, which allow you to directly write to the mesh data with control over whether any checks or validation should be performed. These methods are intended for advanced use cases which require maximum performance. They are faster, but allow you to skip the checks on the data you supply. If you use these methods you must make sure that you are not supplying invalid data, because Unity will not check for you.  
  
The "advanced" methods are: [SetVertexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferParams.html), [SetVertexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferData.html), [SetIndexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferParams.html), [SetIndexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferData.html), [SetSubMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetSubMesh.html), and you can use the [MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) to control which checks or validation are performed or omitted. Use [AcquireReadOnlyMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AcquireReadOnlyMeshData.html) to take a read-only snapshot of Mesh data that you can use with C# Jobs and Burst, and [AllocateWritableMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AllocateWritableMeshData.html) with [ApplyAndDisposeWritableMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.ApplyAndDisposeWritableMeshData.html) to create Meshes from C# Jobs and Burst.  
  
  
  
**Manipulating meshes from a script**  
  
There are three common tasks that might want to use the Mesh API for:  
  
**1. Building a mesh from scratch** : should always be done in the following order:  
a) Assign [vertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertices.html)  
b) Assign [triangles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-triangles.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] newVertices;
    Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)[] newUV;
    int[] newTriangles;  
  
   void Start()
    {
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = new Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)();
        GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().mesh = mesh;
        mesh.vertices = newVertices;
        mesh.uv = newUV;
        mesh.triangles = newTriangles;
    }
}

```

**2. Modifying vertex attributes every frame** :  
a) Get vertices  
b) Modify them  
c) Assign them back to the mesh.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().mesh;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] vertices = mesh.vertices;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] normals = mesh.normals;  
  
       for (var i = 0; i < vertices.Length; i++)
        {
            vertices[i] += normals[i] * Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
        }  
  
       mesh.vertices = vertices;
    }
}

```

**3. Continously changing the mesh triangles and vertices** :  
a) Call [Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.Clear.html) to start fresh  
b) Assign vertices and other attributes  
c) Assign triangle indices.  
  
It is important to call [Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.Clear.html) before assigning new vertices or triangles. Unity always checks the supplied triangle indices whether they don't reference out of bounds vertices. Calling [Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.Clear.html) then assigning vertices then triangles makes sure you never have out of bounds data.
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] newVertices;
    Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)[] newUV;
    int[] newTriangles;  
  
   void Start()
    {
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().mesh;  
  
       mesh.Clear();  
  
       // Do some calculations...
        mesh.vertices = newVertices;
        mesh.uv = newUV;
        mesh.triangles = newTriangles;
    }
}

```

### Properties
Property | Description  
---|---  
[bindposeCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-bindposeCount.html) | The number of bind poses in the Mesh.  
[bindposes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-bindposes.html) | The bind poses. The bind pose at each index refers to the bone with the same index.  
[blendShapeCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-blendShapeCount.html) | Returns BlendShape count on this mesh.  
[boneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-boneWeights.html) | The BoneWeight for each vertex in the Mesh, which represents 4 bones per vertex.  
[bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-bounds.html) | The bounding volume of the Mesh.  
[colors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-colors.html) | Vertex colors of the Mesh.  
[colors32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-colors32.html) | Vertex colors of the Mesh.  
[indexBufferTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-indexBufferTarget.html) | The intended target usage of the Mesh GPU index buffer.  
[indexFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-indexFormat.html) | Format of the mesh index buffer data.  
[isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-isReadable.html) | Returns true if the Mesh is read/write enabled, or false if it is not.  
[normals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-normals.html) | The normals of the Mesh.  
[skinWeightBufferLayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-skinWeightBufferLayout.html) | The dimension of data in the bone weight buffer.  
[subMeshCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-subMeshCount.html) | The number of sub-meshes inside the Mesh object.  
[tangents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-tangents.html) | The tangents of the Mesh.  
[triangles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-triangles.html) | An array containing all triangles in the Mesh.  
[uv](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-uv.html) | The texture coordinates (UVs) in the first channel.  
[uv2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-uv2.html) | The texture coordinates (UVs) in the second channel.  
[uv3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-uv3.html) | The texture coordinates (UVs) in the third channel.  
[uv4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-uv4.html) | The texture coordinates (UVs) in the fourth channel.  
[uv5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-uv5.html) | The texture coordinates (UVs) in the fifth channel.  
[uv6](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-uv6.html) | The texture coordinates (UVs) in the sixth channel.  
[uv7](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-uv7.html) | The texture coordinates (UVs) in the seventh channel.  
[uv8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-uv8.html) | The texture coordinates (UVs) in the eighth channel.  
[vertexAttributeCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertexAttributeCount.html) | Returns the number of vertex attributes that the mesh has. (Read Only)  
[vertexBufferCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertexBufferCount.html) | Gets the number of vertex buffers present in the Mesh. (Read Only)  
[vertexBufferTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertexBufferTarget.html) | The intended target usage of the Mesh GPU vertex buffer.  
[vertexCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertexCount.html) | Returns the number of vertices in the Mesh (Read Only).  
[vertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertices.html) | Returns a copy of the vertex positions or assigns a new vertex positions array.  
### Constructors
Constructor | Description  
---|---  
[Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-ctor.html) | Creates an empty Mesh.  
### Public Methods
Method | Description  
---|---  
[AddBlendShapeFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AddBlendShapeFrame.html) | Adds a new blend shape frame.  
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.Clear.html) | Clears all vertex data and all triangle indices.  
[ClearBlendShapes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.ClearBlendShapes.html) | Clears all blend shapes from Mesh.  
[CombineMeshes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.CombineMeshes.html) | Combines several Meshes into this Mesh.  
[GetAllBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetAllBoneWeights.html) | Gets the bone weights for the Mesh.  
[GetBaseVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBaseVertex.html) | Gets the base vertex index of the given sub-mesh.  
[GetBindposes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBindposes.html) | Gets the bind poses of the Mesh.  
[GetBlendShapeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBlendShapeBuffer.html) | Retrieves a GraphicsBuffer that provides direct read and write access to GPU blend shape vertex data.  
[GetBlendShapeBufferRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBlendShapeBufferRange.html) | Get the location of blend shape vertex data for a given blend shape.  
[GetBlendShapeFrameCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBlendShapeFrameCount.html) | Returns the frame count for a blend shape.  
[GetBlendShapeFrameVertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBlendShapeFrameVertices.html) | Retreives deltaVertices, deltaNormals and deltaTangents of a blend shape frame.  
[GetBlendShapeFrameWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBlendShapeFrameWeight.html) | Returns the weight of a blend shape frame.  
[GetBlendShapeIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBlendShapeIndex.html) | Returns index of BlendShape by given name.  
[GetBlendShapeName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBlendShapeName.html) | Returns name of BlendShape by given index.  
[GetBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBonesPerVertex.html) | The number of non-zero bone weights for each vertex.  
[GetBoneWeightBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBoneWeightBuffer.html) | Retrieves a GraphicsBuffer that provides direct read and write access to GPU bone weight data.  
[GetBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBoneWeights.html) | Gets the bone weights for the Mesh.  
[GetColors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetColors.html) | Gets the vertex colors of the Mesh.  
[GetIndexBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetIndexBuffer.html) | Retrieves a GraphicsBuffer to the GPU index buffer.  
[GetIndexCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetIndexCount.html) | Gets the index count of the given sub-mesh.  
[GetIndexStart](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetIndexStart.html) | Gets the starting index location within the Mesh's index buffer, for the given sub-mesh.  
[GetIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetIndices.html) | Fetches the index list for the specified sub-mesh.  
[GetNativeIndexBufferPtr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetNativeIndexBufferPtr.html) | Retrieves a native (underlying graphics API) pointer to the index buffer.  
[GetNativeVertexBufferPtr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetNativeVertexBufferPtr.html) | Retrieves a native (underlying graphics API) pointer to the vertex buffer.  
[GetNormals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetNormals.html) | Gets the vertex normals of the Mesh.  
[GetSubMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetSubMesh.html) | Get information about a sub-mesh of the Mesh.  
[GetTangents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetTangents.html) | Gets the tangents of the Mesh.  
[GetTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetTopology.html) | Gets the topology of a sub-mesh.  
[GetTriangles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetTriangles.html) | Fetches the triangle list for the specified sub-mesh on this object.  
[GetUVDistributionMetric](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetUVDistributionMetric.html) | The UV distribution metric can be used to calculate the desired mipmap level based on the position of the camera.  
[GetUVs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetUVs.html) | Gets the texture coordinates (UVs) stored in a given channel.  
[GetVertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttribute.html) | Returns information about a vertex attribute based on its index.  
[GetVertexAttributeDimension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttributeDimension.html) | Get dimension of a specific vertex data attribute on this Mesh.  
[GetVertexAttributeFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttributeFormat.html) | Get format of a specific vertex data attribute on this Mesh.  
[GetVertexAttributeOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttributeOffset.html) | Get offset within a vertex buffer stream of a specific vertex data attribute on this Mesh.  
[GetVertexAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttributes.html) | Get information about vertex attributes of a Mesh.  
[GetVertexAttributeStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexAttributeStream.html) | Gets the vertex buffer stream index of a specific vertex data attribute on this Mesh.  
[GetVertexBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexBuffer.html) | Retrieves a GraphicsBuffer that provides direct acces to the GPU vertex buffer.  
[GetVertexBufferStride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertexBufferStride.html) | Get vertex buffer stream stride in bytes.  
[GetVertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertices.html) | Gets the vertex positions of the Mesh.  
[HasVertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.HasVertexAttribute.html) | Checks if a specific vertex data attribute exists on this Mesh.  
[MarkDynamic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MarkDynamic.html) | Optimize mesh for frequent updates.  
[MarkModified](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MarkModified.html) | Notify Renderer components of mesh geometry change.  
[Optimize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.Optimize.html) | Optimizes the Mesh data to improve rendering performance.  
[OptimizeIndexBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.OptimizeIndexBuffers.html) | Optimizes the geometry of the Mesh to improve rendering performance.  
[OptimizeReorderVertexBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.OptimizeReorderVertexBuffer.html) | Optimizes the vertices of the Mesh to improve rendering performance.  
[RecalculateBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.RecalculateBounds.html) | Recalculate the bounding volume of the Mesh and all of its sub-meshes with the vertex data.  
[RecalculateNormals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.RecalculateNormals.html) | Recalculates the normals of the Mesh from the triangles and vertices.  
[RecalculateTangents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.RecalculateTangents.html) | Recalculates the tangents of the Mesh from the normals and texture coordinates.  
[RecalculateUVDistributionMetric](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.RecalculateUVDistributionMetric.html) | Recalculates the UV distribution metric of the Mesh from the vertices and uv coordinates.  
[RecalculateUVDistributionMetrics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.RecalculateUVDistributionMetrics.html) | Recalculates the UV distribution metrics of the Mesh from the vertices and uv coordinates.  
[SetBindposes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetBindposes.html) | Sets the bind poses of the Mesh.  
[SetBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetBoneWeights.html) | Sets the bone weights for the Mesh.  
[SetColors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetColors.html) | Set the per-vertex colors of the Mesh.  
[SetIndexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferData.html) | Sets the data of the index buffer of the Mesh.  
[SetIndexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferParams.html) | Sets the index buffer size and format.  
[SetIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndices.html) | Sets the index buffer for the sub-mesh.  
[SetNormals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetNormals.html) | Set the normals of the Mesh.  
[SetSubMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetSubMesh.html) | Sets the information about a sub-mesh of the Mesh.  
[SetSubMeshes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetSubMeshes.html) | Sets information defining all sub-meshes in this Mesh, replacing any existing sub-meshes.  
[SetTangents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetTangents.html) | Set the tangents of the Mesh.  
[SetTriangles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetTriangles.html) | Sets the triangle list for the sub-mesh.  
[SetUVs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetUVs.html) | Sets the texture coordinates (UVs) stored in a given channel.  
[SetVertexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferData.html) | Sets the data of the vertex buffer of the Mesh.  
[SetVertexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferParams.html) | Sets the vertex buffer size and layout.  
[SetVertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertices.html) | Assigns a new vertex positions array.  
[UploadMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.UploadMeshData.html) | Upload previously done Mesh modifications to the graphics API.  
### Static Methods
Method | Description  
---|---  
[AcquireReadOnlyMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AcquireReadOnlyMeshData.html) | Gets a snapshot of Mesh data for read-only access.  
[AllocateWritableMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AllocateWritableMeshData.html) | Allocates data structures for Mesh creation using C# Jobs.  
[ApplyAndDisposeWritableMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.ApplyAndDisposeWritableMeshData.html) | Applies data defined in MeshData structs to Mesh objects.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *

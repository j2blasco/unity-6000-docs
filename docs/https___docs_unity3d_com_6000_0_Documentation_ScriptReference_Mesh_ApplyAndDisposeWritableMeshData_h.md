* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.ApplyAndDisposeWritableMeshData.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).ApplyAndDisposeWritableMeshData
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
public static void ApplyAndDisposeWritableMeshData([Mesh.MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html) data, [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags); 
## Declaration
public static void ApplyAndDisposeWritableMeshData([Mesh.MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html) data, Mesh[] meshes, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags); 
## Declaration
public static void ApplyAndDisposeWritableMeshData([Mesh.MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html) data, List<Mesh> meshes, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags); 
### Parameters
Parameter | Description  
---|---  
data | The mesh data array, see [MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html).  
mesh | The destination Mesh. Mesh data array must be of size 1.  
meshes | The destination Meshes. Must match the size of mesh data array.  
flags | The mesh data update flags, see [MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html).  
### Description
Applies data defined in `MeshData` structs to Mesh objects.
`ApplyAndDisposeWritableMeshData` takes a [MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html) containing writeable `MeshData` structs, and applies the vertex buffer, index buffer, and sub-mesh data to [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) objects. Use this to create new Meshes using the C# Job System and Burst.  
  
After `ApplyAndDisposeWritableMeshData` is called, the `MeshDataArray` struct is disposed and can no longer be used.  
  
Additional resources: [AllocateWritableMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AllocateWritableMeshData.html), [MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html), [MeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshData.html).
* * *

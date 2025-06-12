* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshUtility.AcquireReadOnlyMeshData.html

#  [MeshUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshUtility.html).AcquireReadOnlyMeshData
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
public static [Mesh.MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html) AcquireReadOnlyMeshData([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh); 
## Declaration
public static [Mesh.MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html) AcquireReadOnlyMeshData(Mesh[] meshes); 
## Declaration
public static [Mesh.MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html) AcquireReadOnlyMeshData(List<Mesh> meshes); 
### Parameters
Parameter | Description  
---|---  
mesh | The input mesh.  
meshes | The input meshes.  
### Returns
**MeshDataArray** Returns a read-only snapshot of Mesh data. See [MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html) and [MeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshData.html). 
### Description
Gets a snapshot of Mesh data for read-only access in the Unity Editor.
This method retrieves the same data as [Mesh.AcquireReadOnlyMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AcquireReadOnlyMeshData.html).  
  
[Mesh.AcquireReadOnlyMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AcquireReadOnlyMeshData.html) only retrieves data from meshes where [Mesh.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-isReadable.html) is `true`. In the Editor, all meshes are readable, even when [Mesh.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-isReadable.html) is set to `false`. This Editor-only method skips the `isReadable` check, and retrieves data whether [Mesh.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-isReadable.html) is `true` or `false`.  
  
Additional resources: [Mesh.AcquireReadOnlyMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AcquireReadOnlyMeshData.html), [MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html), [MeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshData.html)
* * *

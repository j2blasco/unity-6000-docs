* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetIndices.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).GetIndices
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
public int[] GetIndices(int submesh, bool applyBaseVertex = true); 
### Parameters
Parameter | Description  
---|---  
submesh | The sub-mesh index. See [subMeshCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-subMeshCount.html).  
applyBaseVertex | True (default value) will apply base vertex offset to returned indices.  
### Returns
**int[]** Array with face indices. 
### Description
Fetches the index list for the specified sub-mesh.
Each integer in the returned list is a vertex index, which is used as an offset into the Mesh's vertex arrays. See [vertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertices.html) and [GetVertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertices.html). The layout of the indices depends on the [MeshTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.html) of the sub-mesh. For example, a triangular mesh will return indices in multiples of three.  
  
A sub-mesh represents a list of triangles (or indices with a different [MeshTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.html)) that are rendered using a single [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html). When the Mesh is used with a [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) that has multiple materials, you should ensure that there is one sub-mesh per Material.  
  
Call the method overload with a `List` parameter if you control the life cycle of the index buffer and wish to avoid allocation of a new array with every access.  
  
Additional resources: [subMeshCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-subMeshCount.html), [GetTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetTopology.html), [MeshTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.html) enum, [AcquireReadOnlyMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AcquireReadOnlyMeshData.html) function.
* * *
## Declaration
public void GetIndices(List<int> indices, int submesh, bool applyBaseVertex = true); 
## Declaration
public void GetIndices(List<ushort> indices, int submesh, bool applyBaseVertex); 
### Parameters
Parameter | Description  
---|---  
indices | A list of indices to populate.  
submesh | The sub-mesh index. See [subMeshCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-subMeshCount.html).  
applyBaseVertex | True (default value) will apply base vertex offset to returned indices.  
### Description
Use this method overload if you control the life cycle of the list passed in and you want to avoid allocating a new array with every access.
* * *

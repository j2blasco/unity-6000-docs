* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetTriangles.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).GetTriangles
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
public int[] GetTriangles(int submesh); 
## Declaration
public int[] GetTriangles(int submesh, bool applyBaseVertex = true); 
## Declaration
public void GetTriangles(List<int> triangles, int submesh, bool applyBaseVertex = true); 
## Declaration
public void GetTriangles(List<int> triangles, int submesh); 
## Declaration
public void GetTriangles(List<ushort> triangles, int submesh, bool applyBaseVertex); 
### Parameters
Parameter | Description  
---|---  
triangles | A list of vertex indices to populate. Any existing items in the list are replaced.  
submesh | The sub-mesh index. See [subMeshCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-subMeshCount.html).  
applyBaseVertex | True (default value) will apply base vertex offset to returned indices.  
### Description
Fetches the triangle list for the specified sub-mesh on this object.
Each integer in the returned triangle list is a vertex index, which is used as an offset into the Mesh's vertex arrays. See [vertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertices.html) and [GetVertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetVertices.html). The triangle list contains a multiple of three indices, one for each corner in each triangle.  
  
A sub-mesh represents a list of triangles that are rendered using a single [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html). When the Mesh is used with a [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) that has multiple materials, you should ensure that there is one sub-mesh per Material.  
  
Call the method overload with a `List<int>` parameter if you control the life cycle of the index buffer and wish to avoid allocation of a new array with every access.  
  
Additional resources: [subMeshCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-subMeshCount.html).
* * *

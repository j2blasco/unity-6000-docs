* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.RecalculateNormals.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).RecalculateNormals
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
public void RecalculateNormals([Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags = MeshUpdateFlags.Default); 
### Parameters
Parameter | Description  
---|---  
flags | Flags controlling the function behavior, see [MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html).  
### Description
Recalculates the normals of the Mesh from the triangles and vertices.
After modifying the vertices it is often useful to update the normals to reflect the change. Normals are calculated from all shared vertices.  
  
Imported Meshes sometimes don't share all vertices. For example, a vertex at a UV seam is split into two vertices, so the RecalculateNormals function creates normals that are not smooth at the UV seam.  
  
Note that RecalculateNormals does not generate tangents automatically, to do that use [RecalculateTangents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.RecalculateTangents.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().mesh;
        mesh.RecalculateNormals();
    }
}

```

`RecalculateNormals` converts Mesh vertex position data to [VertexAttributeFormat.Float32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeFormat.Float32.html) format, if the format is different.  
  
Additional resources: [RecalculateTangents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.RecalculateTangents.html).
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-subMeshCount.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).subMeshCount
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
subMeshCount; 
### Description
The number of sub-meshes inside the Mesh object.
Each sub-mesh corresponds to a [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) in a [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html), such as [MeshRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html) or [SkinnedMeshRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.html). A sub-mesh consists of a list of triangles, which refer to a set of vertices. Vertices can be shared between multiple sub-meshes.  
  
Additional resources: [GetTriangles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetTriangles.html), [SetTriangles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetTriangles.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().mesh;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Submeshes: " + mesh.subMeshCount);
    }
}

```

For advanced lower-level sub-mesh and mesh data manipulation functions, see [SubMeshDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubMeshDescriptor.html), [SetSubMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetSubMesh.html), [SetIndexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferParams.html), [SetIndexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferData.html).  
  
Note that changing `subMeshCount` to a smaller value than it was previously resizes the Mesh index buffer to be smaller. The new index buffer size is set to [SubMeshDescriptor.indexStart](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubMeshDescriptor-indexStart.html) of the first removed sub-mesh.
* * *

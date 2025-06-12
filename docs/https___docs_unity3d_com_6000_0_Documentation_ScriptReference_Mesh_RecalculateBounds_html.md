* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.RecalculateBounds.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).RecalculateBounds
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
public void RecalculateBounds([Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags = MeshUpdateFlags.Default); 
### Parameters
Parameter | Description  
---|---  
flags | Flags controlling the function behavior, see [MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html).  
### Description
Recalculate the bounding volume of the Mesh and all of its sub-meshes with the vertex data.
After modifying vertices you should call this function to ensure the bounding volume is correct. Assigning [triangles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-triangles.html) automatically recalculates the bounding volume.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().mesh;
        mesh.RecalculateBounds();
    }
}

```

Unity can only recalculate the bounding volume for Meshes that use the default [VertexAttributeFormat.Float32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeFormat.Float32.html) vertex position format. If your Mesh uses a non-standard vertex position data format, you must assign the [bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-bounds.html) manually.  
  
The bounds of a [SkinnedMeshRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.html) cannot be recalculated, and can only be changed by setting the SkinnedMeshRenderer.localBounds manually.  
  
Additional resources: [bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-bounds.html).
* * *

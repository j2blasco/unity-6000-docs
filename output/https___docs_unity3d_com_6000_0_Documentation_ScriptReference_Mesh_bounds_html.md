* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-bounds.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).bounds
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
[Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds; 
### Description
The bounding volume of the Mesh.
This is the axis-aligned bounding box of the mesh in its own space, so the bounds don't change if you change the Transform position, rotation or scale. The [Renderer.bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-bounds.html) property is similar but returns the bounds in world space.  
  
Additional resources: [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) class, [Renderer.bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-bounds.html)
```
// Generates planar UV coordinates independent of mesh size
// by scaling vertices by the bounding box size  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().mesh;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] vertices = mesh.vertices;
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)[] uvs = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)[vertices.Length];
        Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds = mesh.bounds;
        int i = 0;
        while (i < uvs.Length)
        {
            uvs[i] = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(vertices[i].x / bounds.size.x, vertices[i].z / bounds.size.x);
            i++;
        }
        mesh.uv = uvs;
    }
}

```

* * *

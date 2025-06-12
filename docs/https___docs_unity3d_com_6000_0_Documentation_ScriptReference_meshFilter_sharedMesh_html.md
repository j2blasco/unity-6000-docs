* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter-sharedMesh.html

#  [MeshFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html).sharedMesh
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshFilter.html "Go to MeshFilter Component in the Manual")
[Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) sharedMesh; 
### Description
Returns the shared mesh of the mesh filter.
It is recommended to use this function only for **reading mesh data** and not for writing, since you might modify imported assets and all objects that use this mesh will be affected. Also, be aware that is not possible to undo the changes done to this mesh.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Permanently scales the size of the mesh by a factor.  
  
    float scaleFactor = 2f;  
  
    void Start()
    {
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().sharedMesh;  
  
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] vertices = mesh.vertices;
        for (int p = 0; p < vertices.Length; p++)
        {
            vertices[p] *= scaleFactor;
        }
        mesh.vertices = vertices;
        mesh.RecalculateNormals();
    }
}

```

* * *

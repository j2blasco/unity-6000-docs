* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshUtility.Optimize.html

#  [MeshUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshUtility.html).Optimize
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
public static void Optimize([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh); 
### Description
Optimizes the Mesh data to improve rendering performance.
This function causes the geometry and vertices of the mesh to be reordered internally in an attempt to improve vertex cache utilisation on the graphics hardware and thus rendering performance. This operation can take a few seconds or more for complex meshes and should only be used where the ordering of the geometry and vertices is not significant as both will change.  
  
You should only use this function on meshes you generate procedurally in code, for regular mesh assets it is called automatically by the import pipeline when 'Optimize Mesh' is enabled in the mesh importer settings.  
  
This function is effectively the same as calling [Mesh.Optimize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.Optimize.html) or [Mesh.OptimizeIndexBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.OptimizeIndexBuffers.html) followed by [Mesh.OptimizeReorderVertexBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.OptimizeReorderVertexBuffer.html) on the mesh.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = gameObject.GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().mesh;
        MeshUtility.Optimize[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshUtility.Optimize.html)(mesh);
    }
}

```

* * *

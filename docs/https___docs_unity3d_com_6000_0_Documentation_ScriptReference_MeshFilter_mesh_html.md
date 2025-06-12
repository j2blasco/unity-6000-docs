* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter-mesh.html

#  [MeshFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html).mesh
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
[Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh; 
### Description
Returns either a new [mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) or a duplicate of the existing mesh, and assigns it to the mesh filter.
If no mesh is assigned to the mesh filter a new mesh will be created and assigned.  
  
If a mesh is assigned to the mesh filter already, then the first query of `mesh` property will create a duplicate of it, and this copy will be returned. Further queries of `mesh` property will return this duplicated mesh instance. Once `mesh` property is queried, link to the original shared mesh is lost and [MeshFilter.sharedMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter-sharedMesh.html) property becomes an alias to `mesh`. If you want to avoid this automatic mesh duplication, use [MeshFilter.sharedMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter-sharedMesh.html) instead.  
  
By using `mesh` property you can modify the mesh for a single object only. The other objects that used the same mesh will not be modified.  
  
It is your responsibility to destroy the automatically instantiated mesh when the game object is being destroyed. [Resources.UnloadUnusedAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.UnloadUnusedAssets.html) also destroys the mesh but it is usually only called when loading a new level.  
  
Consider `mesh` property as a shortcut for the following code:
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().sharedMesh;
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh2 = Instantiate(mesh);
        GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().sharedMesh = mesh2;
    }
}

```

Which is called on first query of `mesh` property.  
  
**Note:**  
If [MeshFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html) is a part of an asset object, quering `mesh` property is not allowed and only asset mesh can be assigned.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Distorts the mesh vertically.
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Get instantiated mesh
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().mesh;
        // Randomly change vertices
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] vertices = mesh.vertices;
        int p = 0;
        while (p < vertices.Length)
        {
            vertices[p] += new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(-0.3F, 0.3F), 0);
            p++;
        }
        mesh.vertices = vertices;
        mesh.RecalculateNormals();
    }
}

```

Additional resources: [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) class.
* * *

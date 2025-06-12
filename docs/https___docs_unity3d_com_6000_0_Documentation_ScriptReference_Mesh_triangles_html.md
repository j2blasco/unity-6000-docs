* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-triangles.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).triangles
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
triangles; 
### Description
An array containing all triangles in the Mesh.
The array is a list of triangles that contains indices into the vertex array. The size of the triangle array must always be a multiple of 3. Vertices can be shared by simply indexing into the same vertex. If the Mesh contains multiple sub-meshes (Materials), the triangle list will contain all the triangles belonging to all its sub-meshes. When you assign a triangle array using this function, the [subMeshCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-subMeshCount.html) is set to 1. If you want to have multiple sub-meshes, use [subMeshCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-subMeshCount.html) and [SetTriangles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetTriangles.html).  
  
It is recommended to assign a triangle array after assigning the vertex array, in order to avoid out of bounds errors.
```
// Builds a Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) containing a single triangle with uvs.
// Create arrays of vertices, uvs and triangles, and copy them into the mesh.  
  
using UnityEngine;  
  
public class meshTriangles : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Use this for initialization
    void Start()
    {
        gameObject.AddComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>();
        gameObject.AddComponent<MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html)>();
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().mesh;  
  
        mesh.Clear();  
  
        // make changes to the Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) by creating arrays which contain the new values
        mesh.vertices = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] {new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0, 0), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 1, 0), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1, 1, 0)};
        mesh.uv = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)[] {new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 0), new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 1), new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1, 1)};
        mesh.triangles =  new int[] {0, 1, 2};
    }
}

```

Additional resources: [SetTriangles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetTriangles.html), [SetIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndices.html).
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.Clear.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).Clear
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
public void Clear(bool keepVertexLayout = true); 
### Parameters
Parameter | Description  
---|---  
keepVertexLayout | True if the existing Mesh data layout should be preserved.  
### Description
Clears all vertex data and all triangle indices.
You should call this function before rebuilding [triangles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-triangles.html) array.
```
// Convert any GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) into a single triangle  
  
using UnityEngine;  
  
public class meshClear : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private bool once = false;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) > 2.0f)
        {
            convertMesh();
        }
    }  
  
    void convertMesh()
    {
        if (once)
            return;  
  
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().mesh;  
  
        // Clears all the data that the mesh currently has
        mesh.Clear();  
  
        // create 3 vertices for the triangle
        mesh.vertices = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] {new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0, 0), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 1, 0), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1, 1, 0)};
        mesh.uv = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)[] {new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 0), new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 1), new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1, 1)};
        mesh.triangles = new int[] {0, 1, 2};  
  
        once = true;
    }
}

```

Default behaviour of this function keeps the existing vertex layout: if the mesh had tangent vectors and vertex colors, for example, then the tangents and colors will be part of mesh data once you fill in new vertex data. If you want to completely clear the mesh and start with an empty vertex layout, pass false for `keepVertexLayout` parameter. Alternatively, assigning an empty array to any mesh component will also remove it from the vertex layout.
* * *

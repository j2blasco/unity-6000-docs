* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertices.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).vertices
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
vertices; 
### Description
Returns a copy of the vertex positions or assigns a new vertex positions array.
The number of vertices in the Mesh is changed by assigning a vertex array with a different number of vertices.  
  
If you resize the vertex array then all other vertex attributes (normals, colors, tangents, UVs) are automatically resized too. [RecalculateBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.RecalculateBounds.html) is automatically invoked if no vertices have been assigned to the Mesh when setting the vertices.  
  
Note that this method returns the vertices in local space, not in world space.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] vertices;
    void Start()
    {
        mesh = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().mesh;
        vertices = mesh.vertices;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        for (var i = 0; i < vertices.Length; i++)
        {
            vertices[i] += Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);
        }  
  
        // assign the local vertices array into the vertices array of the Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).
        mesh.vertices = vertices;
        mesh.RecalculateBounds();
    }
}

```

**Note:** To make changes to the [vertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertices.html) it is important to copy the vertices from the [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html). Once the [vertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertices.html) have been copied and changed the [vertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertices.html) can be reassigned back to the [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).
* * *

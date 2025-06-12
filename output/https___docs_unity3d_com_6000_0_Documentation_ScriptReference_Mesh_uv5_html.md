* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-uv5.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).uv5
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
uv5; 
### Description
The texture coordinates (UVs) in the fifth channel.
This channel is also commonly called "UV4". It maps to the shader semantic `TEXCOORD4`. When you call [Mesh.HasVertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.HasVertexAttribute.html), this channel corresponds to [VertexAttribute.TexCoord4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.TexCoord4.html).  
  
Unity stores UVs in 0-1 space. [0,0] represents the bottom-left corner of the texture, and [1,1] represents the top-right. Values are not clamped; you can use values below 0 and above 1 if needed.  
  
This property is supported for backwards compatibility, but the newer [GetUVs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetUVs.html) and [SetUVs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetUVs.html) functions allow you to access the same data in a more user-friendly way, and use a Vector3 or Vector4 value if you need to.  
  
This property returns a copy of the data. This means that it causes a heap memory allocation. It also means that to make changes to the original data, you must update the copy and then reassign the updated copy to the mesh.  
  
The following example demonstrates how to create an array to hold UV data, assign texture coordinates to it, and then assign it to the mesh.
```
// Generate planar uv coordinates for the fifth uv set  
  
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().mesh;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] vertices = mesh.vertices;
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)[] uvs = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)[vertices.Length];  
  
        for (int i = 0; i < uvs.Length; i++)
        {
            uvs[i] = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(vertices[i].x, vertices[i].z);
        }
        mesh.uv5 = uvs;
    }
}

```

Additional resources: [GetUVs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetUVs.html), [SetUVs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetUVs.html), [AcquireReadOnlyMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AcquireReadOnlyMeshData.html).
* * *

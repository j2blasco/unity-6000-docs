* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshNow.html

#  [Graphics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html).DrawMeshNow
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
public static void DrawMeshNow([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation); 
## Declaration
public static void DrawMeshNow([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, int materialIndex); 
## Declaration
public static void DrawMeshNow([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) matrix); 
## Declaration
public static void DrawMeshNow([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) matrix, int materialIndex); 
### Parameters
Parameter | Description  
---|---  
mesh | The [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) to draw.  
position | Position of the mesh.  
rotation | Rotation of the mesh.  
matrix | The transformation matrix of the mesh (combines position, rotation and other transformations).  
materialIndex | Subset of the mesh to draw.  
### Description
Draw a mesh immediately.
This function will draw a given mesh immediately. Currently set shader and material (see [Material.SetPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetPass.html)) will be used.  
  
The mesh will be just drawn once, it won't be per-pixel lit and will not cast or receive real-time shadows. If you want full integration with lighting and shadowing, use [Graphics.DrawMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMesh.html) instead.
```
using UnityEngine;
using System.Collections;  
  
// Attach this script to a Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) {
    public Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh;
    public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat;
    public void OnPostRender() {
        // set first shader pass of the material
        mat.SetPass(0);
        // draw mesh at the origin
        Graphics.DrawMeshNow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshNow.html)(mesh, Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html));
    }
}
```

Additional resources: [Graphics.DrawMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMesh.html), [Material.SetPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetPass.html).
* * *

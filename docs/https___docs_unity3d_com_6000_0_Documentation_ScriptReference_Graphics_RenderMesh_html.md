* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMesh.html

#  [Graphics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html).RenderMesh
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
public static void RenderMesh(ref [RenderParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams.html) rparams, [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, int submeshIndex, [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) objectToWorld, Nullable<Matrix4x4> prevObjectToWorld = null); 
### Parameters
Parameter | Description  
---|---  
rparams | The parameters Unity uses to render the mesh.  
mesh | The [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) to render.  
submeshIndex | The index of a submesh Unity renders when the Mesh contains multiple Materials (submeshes). For a Mesh with a single Material, use value 0.  
objectToWorld | The transformation matrix Unity uses to transform the mesh from object to world space.  
prevObjectToWorld | The previous frame transformation matrix Unity uses to calculate motion vectors for the mesh.  
### Description
Renders a mesh with given rendering parameters.
`RenderMesh` renders a Mesh for the current frame. This Mesh is affected by Lights, can cast and receive shadows, and is affected by Projectors. This Mesh can be rendered by all Cameras or by a specific Camera.  
  
Use `RenderMesh` to control Mesh rendering programmatically without the need to create and manage GameObjects. `RenderMesh` submits the Mesh for rendering, which means it does not render the Mesh immediately. Unity renders the Mesh as part of normal rendering process. If you want to render a mesh immediately, use [Graphics.DrawMeshNow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshNow.html).  
  
`RenderMesh` does not apply any changes you make to the Material properties of a Mesh between calls. This is because it does not render the Mesh immediately. If you want to render series of Meshes that have the same Material, but with slightly different properties (for example, to change color of each mesh), use [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) parameter.  
  
This call creates internal resources while the Mesh is in the render queue. The allocation happens immediately and exists until the end of frame if the object is in the render queue for all cameras. Otherwise, the allocation exists until the specified Camera finishes rendering.  
  
Additional resources: [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).  
  
The following example renders 10 Meshes with a given Material:
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material;
    public Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        RenderParams[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams.html) rp = new RenderParams[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams.html)(material);
        for(int i=0; i<10; ++i)
            Graphics.RenderMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMesh.html)(rp, mesh, 0, Matrix4x4.Translate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Translate.html)(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-4.5f+i, 0.0f, 5.0f)));
    }
}
```

* * *

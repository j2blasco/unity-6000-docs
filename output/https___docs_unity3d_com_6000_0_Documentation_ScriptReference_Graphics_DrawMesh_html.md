* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMesh.html

#  [Graphics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html).DrawMesh
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
public static void DrawMesh([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, int layer, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera = null, int submeshIndex = 0, [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) properties = null, bool castShadows = true, bool receiveShadows = true, bool useLightProbes = true); 
## Declaration
public static void DrawMesh([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, int layer, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, int submeshIndex, [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) properties, [Rendering.ShadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastingMode.html) castShadows, bool receiveShadows = true, [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) probeAnchor = null, bool useLightProbes = true); 
## Declaration
public static void DrawMesh([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) matrix, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, int layer, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera = null, int submeshIndex = 0, [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) properties = null, bool castShadows = true, bool receiveShadows = true, bool useLightProbes = true); 
## Declaration
public static void DrawMesh([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) matrix, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, int layer, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, int submeshIndex, [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) properties, [Rendering.ShadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastingMode.html) castShadows, bool receiveShadows = true, [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) probeAnchor = null, bool useLightProbes = true); 
## Declaration
public static void DrawMesh([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) matrix, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, int layer, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, int submeshIndex, [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) properties, [Rendering.ShadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastingMode.html) castShadows, bool receiveShadows, [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) probeAnchor, [Rendering.LightProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.html) lightProbeUsage, [LightProbeProxyVolume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume.html) lightProbeProxyVolume = null); 
### Parameters
Parameter | Description  
---|---  
mesh | The [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) to draw.  
position | Position of the mesh.  
rotation | Rotation of the mesh.  
matrix | Transformation matrix of the mesh (combines position, rotation and other transformations).  
material |  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) to use.  
layer |  [Layer](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) the mesh is drawn on.  
camera | If `null` (default), the mesh will be drawn in all cameras. Otherwise it will be rendered in the given Camera only.  
submeshIndex | Which subset of the mesh to draw. This applies only to meshes that are composed of several materials.  
properties | Additional material properties to apply onto material just before this mesh will be drawn. See [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).  
castShadows | Determines whether the mesh can cast shadows.  
receiveShadows | Determines whether the mesh can receive shadows.  
useLightProbes | Should the mesh use light probes?  
probeAnchor | If used, the mesh will use this Transform's position to sample light probes and find the matching reflection probe.  
lightProbeUsage |  [LightProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.html) for the mesh.  
### Description
Draw a mesh.
This function is now obsolete. Use [Graphics.RenderMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMesh.html) instead.  
  
DrawMesh draws a mesh for one frame. The mesh will be affected by the lights, can cast and receive shadows and be affected by Projectors - just like it was part of some game object. It can be drawn for all cameras or just for some specific camera.  
  
Use DrawMesh in situations where you want to draw large amount of meshes, but don't want the overhead of creating and managing game objects. Note that DrawMesh does not draw the mesh immediately; it merely "submits" it for rendering. The mesh will be rendered as part of normal rendering process. If you want to draw a mesh immediately, use [Graphics.DrawMeshNow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshNow.html).  
  
Because DrawMesh does not draw mesh immediately, modifying material properties between calls to this function won't make the meshes pick them up. If you want to draw series of meshes with the same material, but slightly different properties (e.g. change color of each mesh), use [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) parameter.  
  
Note that this call will create some internal resources while the mesh is queued up for rendering. The allocation happens immediately and will be kept around until the end of frame (if the object was queued for all cameras) or until the specified camera renders itself.  
  
Additional resources: [Graphics.RenderMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMesh.html), [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) {
    public Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh;
    public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material;
    public void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)() {
        // will make the mesh appear in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) at origin position
        Graphics.DrawMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMesh.html)(mesh, Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html), material, 0);
    }
}

```

* * *

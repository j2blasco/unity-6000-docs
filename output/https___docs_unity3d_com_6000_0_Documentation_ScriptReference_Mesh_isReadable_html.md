* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-isReadable.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).isReadable
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
isReadable; 
### Description
Returns true if the Mesh is read/write enabled, or false if it is not.
When a Mesh is read/write enabled, Unity uploads the Mesh data to GPU-addressable memory, but also keeps it in CPU-addressable memory. When a Mesh is not read/write enabled, Unity uploads the Mesh data to GPU-addressable memory, and then removes it from CPU-addressable memory.  
  
You can set this value using the Read/Write Enabled checkbox when importing a model to Unity. To set the value to false at run time, set the `markNoLongerReadable` argument of [Mesh.UploadMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.UploadMeshData.html).  
  
In most cases, you should disable this option to save runtime memory usage. You should only enable it under the following circumstances: 
  * When you read from or write to the Mesh data in your code.
  * When you pass the Mesh to `StaticBatchingUtility.Combine()` to combine the Mesh at run time.
  * When you pass the mesh to [CanvasRenderer.SetMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.SetMesh.html).
  * When you use the Mesh to bake a NavMesh using the NavMesh building components at run time.
  * When the Mesh is convex, you use the Mesh with a Mesh Collider, and the Mesh Collider's Transform has negative scaling (for example, (–1, 1, 1)).
  * When you use the Mesh with a Mesh Collider, and the Mesh Collider's transform is skewed or sheared (for example, when a rotated Transform has a scaled parent Transform).
  * When you use the Mesh with a Mesh Collider, and the Mesh Collider's Cooking Options flags are set to any value other than the default.
  * When using a Mesh with a Particle System's Shape module or Renderer module when not using GPU instancing.


Note that the Particle System will automatically change Meshes to readable when assigned through the inspector  
  
Notes: When Unity creates a Mesh from script, this value is initially set to true. Meshes not marked readable will throw an error on accessing any data arrays from script at runtime. Access is always allowed in the Unity Editor outside of the game and rendering loop, regardless of this setting.  
  
Additional resources: [StaticBatchingUtility.Combine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticBatchingUtility.Combine.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().sharedMesh;
        print(mesh.isReadable);
    }
}

```

* * *

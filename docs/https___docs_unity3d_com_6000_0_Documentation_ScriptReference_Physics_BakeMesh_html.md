* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.BakeMesh.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).BakeMesh
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
public static void BakeMesh(int meshID, bool convex); 
### Parameters
Parameter | Description  
---|---  
meshID | The instance ID of the mesh to bake collision data from.  
convex | A flag to indicate whether to bake convex geometry or not.  
### Description
Prepares the mesh for use with a [MeshCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshCollider.html) and uses default cooking options.
* * *
## Declaration
public static void BakeMesh(int meshID, bool convex, [MeshColliderCookingOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshColliderCookingOptions.html) cookingOptions); 
### Parameters
Parameter | Description  
---|---  
meshID | The instance ID of the mesh to bake collision data from.  
convex | A flag to indicate whether to bake convex geometry or not.  
cookingOptions | The cooking options to use when you bake the mesh.  
### Description
Prepares the mesh for use with a [MeshCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshCollider.html).
In order for the mesh to be usable with the [MeshCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshCollider.html), the physics system must prepare it first, by creating the spatial search acceleration structures. This process is called baking.  
  
Normally, the MeshCollider component requires the baked mesh when the user instantiates it, or when the user sets a new mesh to it with the sharedMesh property. Baking is a resource-intensive operation so you might want to run it when the moment is right (for example during a less resource-intensive part of the application), or to spread the load across all available cores if multiple meshes require baking. That said, the purpose of this function is to pre-bake the mesh for later use so that no further baking is required.  
  
The mesh instance stores the baked mesh.  
  
The baking process needs access to the mesh geometry. If the user invokes the BakeMesh method in the Player, the BakeMesh method requires the Read/Write property of the mesh to be enabled. However, using the BakeMesh method in the Editor doesn't require any extra settings, because the geometry is always available in the Editor.  
  
The MeshCollider component reuses the baked mesh if, and only if, all of the following conditions are met: 
  * The MeshCollider's cookingOptions are exactly the same as were specified during baking,
  * The MeshCollider's transform allows mesh sharing (*),
  * The mesh geometry hasn't been changed since the last bake.


In this context, the MeshCollider's transform allows mesh sharing if:
  * Its scaling is not negative and is not skewed, or
  * Its scaling is negative but only when MeshCollider is not convex  



Note: When you add a [MeshCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshCollider.html) component to a GameObject with a [MeshFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html) component already present, the sharedMesh property is set automatically and this might trigger a re-bake.  
  
  
  
Here is a simple example baking the mesh on the main thread:
```
using UnityEngine;  
  
public class MinimalTest : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh;  
  
    private MeshCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshCollider.html) collider;  
  
    private MeshColliderCookingOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshColliderCookingOptions.html) cookingOptions =
        MeshColliderCookingOptions.UseFastMidphase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshColliderCookingOptions.UseFastMidphase.html) | MeshColliderCookingOptions.CookForFasterSimulation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshColliderCookingOptions.CookForFasterSimulation.html);  
  
    private void OnEnable()
    {
        // Bake this Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) to use later.
        Physics.BakeMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.BakeMesh.html)(mesh.GetInstanceID(), false, cookingOptions);
    }  
  
    public void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        // If the collider wasn't yet created - create it now.
        if (collider == null)
        {
            // No mesh baking will happen here because the mesh was pre-baked, making instantiation faster.
            collider = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)().AddComponent<MeshCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshCollider.html)>();
            collider.cookingOptions = cookingOptions;
            collider.sharedMesh = mesh;
        }
    }
}

```

BakeMesh is thread-safe, and does computations on the thread it was called from. However, don't call BakeMesh on the same mesh from multiple threads at the same time because that causes undefined behavior. You can use BakeMesh with the C# Job System. This example shows how to bake meshes across multiple threads so that MeshCollider instantiation takes less time on the main thread.
```
using Unity.Collections;
using Unity.Jobs;
using UnityEngine;  
  
public struct BakeJob : IJobParallelFor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobParallelFor.html)
{
    private NativeArray<int> meshIds;  
  
    public BakeJob(NativeArray<int> meshIds)
    {
        this.meshIds = meshIds;
    }  
  
    public void Execute(int index)
    {
        Physics.BakeMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.BakeMesh.html)(meshIds[index], false);
    }
}  
  
public class JobifiedBaking : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)[] meshes;
    public int meshesPerJob = 10;  
  
    // Bake all the Meshes off of the main thread, and then instantiate on the main thread.
    private void OnEnable()
    {
        // You cannot access GameObjects and Components from other threads directly.
        // As such, you need to create a native array of instance IDs that BakeMesh will accept.
        NativeArray<int> meshIds = new NativeArray<int>(meshes.Length, Allocator.TempJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.TempJob.html));  
  
        for (int i = 0; i < meshes.Length; ++i)
        {
            meshIds[i] = meshes[i].GetInstanceID();
        }  
  
        // This spreads the expensive operation over all cores.
        var job = new BakeJob(meshIds);
        job.Schedule(meshIds.Length, meshesPerJob).Complete();  
  
        meshIds.Dispose();  
  
        // Now instantiate colliders on the main thread.
        for (int i = 0; i < meshes.Length; ++i)
        {
            new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)().AddComponent<MeshCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshCollider.html)>().sharedMesh = meshes[i];
        }
    }
}

```

* * *

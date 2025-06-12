* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AcquireReadOnlyMeshData.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).AcquireReadOnlyMeshData
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
public static [Mesh.MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html) AcquireReadOnlyMeshData([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh); 
## Declaration
public static [Mesh.MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html) AcquireReadOnlyMeshData(Mesh[] meshes); 
## Declaration
public static [Mesh.MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html) AcquireReadOnlyMeshData(List<Mesh> meshes); 
### Parameters
Parameter | Description  
---|---  
mesh | The input mesh.  
meshes | The input meshes.  
### Returns
**MeshDataArray** Returns a `MeshDataArray` containing read-only `MeshData` structs. See [MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html) and [MeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshData.html). 
### Description
Gets a snapshot of Mesh data for read-only access.
When you pass one or more Meshes to [Mesh.AcquireReadOnlyMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AcquireReadOnlyMeshData.html), Unity returns a [MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html) of read-only `MeshData` structs. You can access the resulting `MeshDataArray` and `MeshData` structs from any thread. Creating a `MeshDataArray` has some overhead for memory tracking and safety reasons, so it is more efficient to make a single call to [Mesh.AcquireReadOnlyMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AcquireReadOnlyMeshData.html) and request multiple `MeshData` structs in the same `MeshDataArray` than it is to make multiple calls to [Mesh.AcquireReadOnlyMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AcquireReadOnlyMeshData.html).  
  
Each `MeshData` struct contains a read-only snapshot of data for a given Mesh.  
  
You must dispose of the `MeshDataArray` once you have finished working with it. Calling [Mesh.AcquireReadOnlyMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AcquireReadOnlyMeshData.html) does not cause any memory allocations or data copies by default, as long as you dispose of the `MeshDataArray` before modifying the Mesh. However, if you call [Mesh.AcquireReadOnlyMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AcquireReadOnlyMeshData.html) and then modify the Mesh while the `MeshDataArray` exists, Unity must copy the `MeshDataArray` into a new memory allocation. In addition to this, if you call [Mesh.AcquireReadOnlyMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AcquireReadOnlyMeshData.html) and then modify the Mesh, your modifications are not reflected in the `MeshData` structs.  
  
This method will throw an `InvalidOperationException` if [isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-isReadable.html) is `false` for one or more input meshes. When working in the Unity Editor, use [MeshUtility.AcquireReadOnlyMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshUtility.AcquireReadOnlyMeshData.html) to skip this check.  
  
Use [Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.Dispose.html) to dispose of the `MeshDataArray`, or use the C# `using` pattern to do this automatically:
```
using Unity.Collections;
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = new Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)();
        mesh.vertices = new[] {Vector3.one[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-one.html), Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html)};
        using (Mesh.MeshDataArray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html) dataArray = Mesh.AcquireReadOnlyMeshData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AcquireReadOnlyMeshData.html)(mesh))
        {
            Mesh.MeshData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshData.html) data = dataArray[0];
            // prints "2"
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(data.vertexCount);
            NativeArray<Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)> gotVertices = new NativeArray<Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)>(mesh.vertexCount, Allocator.TempJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.TempJob.html));
            data.GetVertices(gotVertices);
            // prints "(1.0, 1.0, 1.0)" and "(0.0, 0.0, 0.0)"
            foreach (Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) v in gotVertices)
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(v);
            gotVertices.Dispose();
        }
    }
}

```

Additional resources: [MeshDataArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshDataArray.html), [MeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MeshData.html), [AllocateWritableMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AllocateWritableMeshData.html), [ApplyAndDisposeWritableMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.ApplyAndDisposeWritableMeshData.html).
* * *

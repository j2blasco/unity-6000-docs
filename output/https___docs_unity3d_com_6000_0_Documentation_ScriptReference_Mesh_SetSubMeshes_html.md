* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetSubMeshes.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).SetSubMeshes
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
public void SetSubMeshes(SubMeshDescriptor[] desc, int start, int count, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags); 
## Declaration
public void SetSubMeshes(SubMeshDescriptor[] desc, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags); 
## Declaration
public void SetSubMeshes(List<SubMeshDescriptor> desc, int start, int count, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags); 
## Declaration
public void SetSubMeshes(List<SubMeshDescriptor> desc, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags); 
## Declaration
public void SetSubMeshes(NativeArray<T> desc, int start, int count, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags); 
## Declaration
public void SetSubMeshes(NativeArray<T> desc, [Rendering.MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) flags); 
### Parameters
Parameter | Description  
---|---  
desc | An array or list of sub-mesh data descriptors.  
start | Index of the first element to take from the array or list in `desc`.  
count | Number of elements to take from the array or list in `desc`.  
flags | (Optional) Flags controlling the function behavior, see [MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html).  
### Description
Sets information defining all sub-meshes in this [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html), replacing any existing sub-meshes.
Note that [SetSubMeshes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetSubMeshes.html), [SetSubMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetSubMesh.html), [SubMeshDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubMeshDescriptor.html), and [SetIndexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferData.html) are designed for maximum performance. These functions operate on the underlying mesh data structures involving raw index buffers, vertex buffers and mesh subset data. When you use these methods, Unity performs very little data validation, so you must ensure your data is valid.  
  
In particular, you must ensure that the [SubMeshDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubMeshDescriptor.html) index ranges and [SubMeshDescriptor.topology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubMeshDescriptor-topology.html) values are set to correct values. SubMesh indices, both indexStart and indexCount, must not overlap with any other SubMesh indices.  
  
For information about the difference between the simpler and more advanced methods of assigning data to a Mesh from script, see [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).  
  
The [SubMeshDescriptor-bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubMeshDescriptor-bounds.html), [SubMeshDescriptor-firstVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubMeshDescriptor-firstVertex.html) and [SubMeshDescriptor-vertexCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubMeshDescriptor-vertexCount.html) values of [SubMeshDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubMeshDescriptor.html) are calculated automatically by `SetSubMeshes`, unless [MeshUpdateFlags.DontRecalculateBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.DontRecalculateBounds.html) flag is passed. Note that this only applies to the bounds of the SubMesh. You must call [Mesh.RecalculateBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.RecalculateBounds.html) to recalculate the bounds of the Mesh itself.  
  
General usage pattern is:
```
var mesh = new Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)();  
  
// setup vertex buffer data
mesh.vertices = ...;  
  
// set index buffer
mesh.SetIndexBufferParams(...);
mesh.SetIndexBufferData(...);  
  
// setup information about mesh subsets
SubMeshDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubMeshDescriptor.html)[] sm = new SubMeshDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubMeshDescriptor.html)[] {...}
mesh.SetSubMeshes(sm);  
  
// update bounds of the mesh
mesh.RecalculateBounds();
```

For details on what data to set up for each sub-mesh, see [SubMeshDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubMeshDescriptor.html).  
  
Additional resources: [subMeshCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-subMeshCount.html), [GetSubMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetSubMesh.html), [SetSubMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetSubMesh.html), [SetIndexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferParams.html), [SetIndexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferData.html), [MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html).
* * *

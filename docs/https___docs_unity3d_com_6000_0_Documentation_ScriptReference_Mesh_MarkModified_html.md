* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MarkModified.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).MarkModified
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
public void MarkModified(); 
### Description
Notify [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) components of mesh geometry change.
By default, whenever Mesh data changes that could affect the geometry of the mesh, all [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) components that use this mesh get notified. For example, [MeshRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html) components recalculate their bounding boxes, and [ShapeModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ShapeModule.html) rebuild internal data used for mesh surface emission.  
  
However a [MeshUpdateFlags.DontNotifyMeshUsers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.DontNotifyMeshUsers.html) flag can be used in [Mesh.SetVertexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferData.html), [Mesh.SetIndexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferData.html) or [Mesh.SetSubMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetSubMesh.html) in order to skip this notification. This can be beneficial when you know that many mesh modifications will happen before the renderer components will need to actually update. A manual call to `MarkModified` can be used later to notify the dependent renderer components of a mesh geometry change.  
  
`MarkModified` function only needs to be called if you actually use the `DontNotifyMeshUsers` flag. In all other cases the mesh change notifications happen automatically.  
  
Additional resources: [Mesh.SetVertexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferData.html), [Mesh.SetIndexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferData.html), [Mesh.SetSubMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetSubMesh.html).
* * *

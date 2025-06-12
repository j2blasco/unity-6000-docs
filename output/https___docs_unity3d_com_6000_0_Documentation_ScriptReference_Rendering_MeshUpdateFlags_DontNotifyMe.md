* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.DontNotifyMeshUsers.html

#  [MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html).DontNotifyMeshUsers
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
### Description
Indicates that Unity should not notify [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) components about a possible [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) bounds change, when you modify Mesh data.
When you modify Mesh data that could affect the geometry of the mesh, Unity's default behaviour is to notify all [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) components that use this mesh, so that they can perform recalculations based on the new data that are typically desirable. For example, [MeshRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html) components recalculate their bounding boxes, and the [ShapeModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ShapeModule.html) rebuilds internal data used for mesh surface emission.  
  
If you supply the `MeshUpdateFlags.DontNotifyMeshUsers` flag when using the "advanced" Mesh API, Unity will omit these notifications. This can be beneficial to performance when you know that many mesh modifications will happen before the renderer components actually need to update.  
  
You must therefore make sure that you call [Mesh.MarkModified](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.MarkModified.html) at a later point to notify the dependent renderer components that they should perform their recalculations.  
  
You can use this flag with the following "advanced" mesh API: [Mesh.SetVertexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferData.html), [Mesh.SetIndexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferData.html) or [Mesh.SetSubMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetSubMesh.html)  
  
For information about the difference between the simpler and more advanced methods of assigning data to a Mesh from script, see the notes on the [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) page.  
  

* * *

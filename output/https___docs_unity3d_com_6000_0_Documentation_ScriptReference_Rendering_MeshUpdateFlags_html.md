* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html

# MeshUpdateFlags
enumeration
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
Mesh data update flags.
Some advanced [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) functions like [SetVertexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferData.html), [SetIndexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferData.html), [SetSubMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetSubMesh.html) take an optional `flags` parameter that controls behavior of these functions. In particular, these flags allow you to control what happens when a Mesh's data is updated.  
  
By default, Unity performs checks and validation on the data you supply when using these methods - for example, to check whether the indices array has any out-of-bounds values.  
  
These flags allow you to optionally omit some or all of these checks for the purpose of increasing performance. If you choose to omit these checks, you must ensure that the data you are supplying is valid.  
  
You can combine individual flags using the logical OR operator. For example: `MeshUpdateFlags.DontNotifyMeshUsers | MeshUpdateFlags.DontValidateIndices`.  
  
For information about the difference between the simpler and more advanced methods of assigning data to a Mesh from script, see the notes on the [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) page. 
### Properties
Property | Description  
---|---  
[Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.Default.html) | Indicates that Unity should perform the default checks and validation when you update a Mesh's data.  
[DontValidateIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.DontValidateIndices.html) | Indicates that Unity should not check index values when you use Mesh.SetIndexBufferData to modify a Mesh's data.  
[DontResetBoneBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.DontResetBoneBounds.html) | Indicates that Unity should not reset skinned mesh bone bounds when you modify Mesh data using Mesh.SetVertexBufferData or Mesh.SetIndexBufferData.  
[DontNotifyMeshUsers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.DontNotifyMeshUsers.html) | Indicates that Unity should not notify Renderer components about a possible Mesh bounds change, when you modify Mesh data.  
[DontRecalculateBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.DontRecalculateBounds.html) | Indicates that Unity should not recalculate the bounds when you set Mesh data using Mesh.SetSubMesh.  
* * *

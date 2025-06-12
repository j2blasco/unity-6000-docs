* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.DontResetBoneBounds.html

#  [MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html).DontResetBoneBounds
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
Indicates that Unity should not reset skinned mesh bone bounds when you modify Mesh data using [Mesh.SetVertexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferData.html) or [Mesh.SetIndexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferData.html).
When you modify Skinned Mesh vertex position or index buffer data, Unity's default behaviour is to reset the internal data structure that contains the cached bounding boxes of each bone, and then recalculate these bounds from the new vertex and index buffer data.  
  
You can make Unity skip this behaviour by using the `MeshUpdateFlags.DontResetBoneBounds` flag. This can be beneficial to performance when you know that many mesh modifications will happen before the bone bounds need an update, or when you know that bone bounds do not need to be recalculated.  
  
You can use this flag with the [Mesh.SetVertexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferData.html) and [Mesh.SetIndexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferData.html) methods. 
* * *

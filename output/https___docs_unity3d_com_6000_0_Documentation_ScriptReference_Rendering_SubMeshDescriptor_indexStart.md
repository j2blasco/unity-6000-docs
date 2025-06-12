* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubMeshDescriptor-indexStart.html

#  [SubMeshDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubMeshDescriptor.html).indexStart
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
indexStart; 
### Description
Starting point inside the whole Mesh index buffer where the face index data is found.
This property, together with [indexCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubMeshDescriptor-indexCount.html), determines which part of the whole index buffer is used by a particular sub-mesh. Values in the index buffer are interpreted according to the [topology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubMeshDescriptor-topology.html) property, for example the usual [MeshTopology.Triangles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.Triangles.html) topology needs three indices for each triangle.  
  
Additional resources: [indexCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubMeshDescriptor-indexCount.html), [Mesh.SetSubMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetSubMesh.html), [Mesh.GetSubMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetSubMesh.html), [Mesh.SetIndexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferParams.html), [Mesh.SetIndexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferData.html).
* * *

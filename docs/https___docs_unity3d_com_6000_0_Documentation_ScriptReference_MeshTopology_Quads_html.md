* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.Quads.html

#  [MeshTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.html).Quads
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
Mesh is made from quads.
Each four indices in the mesh index buffer form a quadrangular face. Note that quad topology is emulated on many platforms, so it's more efficient to use a triangular mesh. Unless you really need quads, for example if using DirectX 11 tessellation shaders that operate on quad patches.  
  
Additional resources: [Mesh.SetIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndices.html) function.
* * *

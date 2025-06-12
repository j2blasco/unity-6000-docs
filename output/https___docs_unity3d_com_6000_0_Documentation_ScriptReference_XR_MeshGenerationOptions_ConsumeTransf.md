* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshGenerationOptions.ConsumeTransform.html

#  [MeshGenerationOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshGenerationOptions.html).ConsumeTransform
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
Indicates you plan to consume the resulting mesh's transform.
Used by [XRMeshSubsystem.GenerateMeshAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMeshSubsystem.GenerateMeshAsync.html) when the mesh provider supplies a transform. If `MeshGenerationOptions` has this value, Unity does not apply the supplied transform to the vertices. Otherwise, Unity applies the supplied transform to the vertices of the mesh, and rebakes the physics mesh.  
  
Additional resources: [XRMeshSubsystem.GenerateMeshAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMeshSubsystem.GenerateMeshAsync.html), [MeshGenerationResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshGenerationResult.html)
* * *

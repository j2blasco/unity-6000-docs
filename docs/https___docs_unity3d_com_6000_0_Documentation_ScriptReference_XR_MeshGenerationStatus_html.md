* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshGenerationStatus.html

# MeshGenerationStatus
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
The status of a [XRMeshSubsystem.GenerateMeshAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMeshSubsystem.GenerateMeshAsync.html).
[XRMeshSubsystem.GenerateMeshAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMeshSubsystem.GenerateMeshAsync.html) will always invoke the provided delegate when the generation completes. This enum contains information about whether the generation was successful, or if an error occurred.  
  
Additional resources: [XRMeshSubsystem.GenerateMeshAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMeshSubsystem.GenerateMeshAsync.html)
### Properties
Property | Description  
---|---  
[Success](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshGenerationStatus.Success.html) | The mesh generation was successful.  
[InvalidMeshId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshGenerationStatus.InvalidMeshId.html) | The mesh generation failed because the mesh does not exist.  
[GenerationAlreadyInProgress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshGenerationStatus.GenerationAlreadyInProgress.html) | The XRMeshSubsystem was already generating the requested mesh.  
[Canceled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshGenerationStatus.Canceled.html) | The mesh generation was canceled.  
[UnknownError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshGenerationStatus.UnknownError.html) | The mesh generation failed for unknown reasons.  
* * *

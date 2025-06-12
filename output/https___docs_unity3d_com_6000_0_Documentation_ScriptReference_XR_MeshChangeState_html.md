* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshChangeState.html

# MeshChangeState
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
The state of a tracked mesh since the last query.
This enum is used by [MeshInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshInfo.html) to indicate which meshes have been added, updated, or removed.  
  
Additional resources: [XRMeshSubsystem.TryGetMeshInfos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMeshSubsystem.TryGetMeshInfos.html)
### Properties
Property | Description  
---|---  
[Added](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshChangeState.Added.html) | The mesh has been added since the last call to XRMeshSubsystem.TryGetMeshInfos.  
[Updated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshChangeState.Updated.html) | The mesh has been updated since the last call to XRMeshSubsystem.TryGetMeshInfos.  
[Removed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshChangeState.Removed.html) | The mesh has been removed since the last call to XRMeshSubsystem.TryGetMeshInfos.  
[Unchanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshChangeState.Unchanged.html) | The mesh has not changed since the last call to XRMeshSubsystem.TryGetMeshInfos.  
* * *

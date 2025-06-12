* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshTransform.html

# MeshTransform
struct in UnityEngine.XR
/
Implemented in:[UnityEngine.XRModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.XRModule.html)
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
Contains transform information related to a tracked mesh.
This struct is used by the [XRMeshSubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMeshSubsystem.html) to communication information about a mesh's transform.  
  
Additional resources: [XRMeshSubsystem.GetUpdatedMeshTransforms](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMeshSubsystem.GetUpdatedMeshTransforms.html)
### Properties
Property | Description  
---|---  
[MeshId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshTransform.MeshId.html) | The session-unique identifier of the tracked mesh.  
[Position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshTransform.Position.html) | The position of the mesh, relative to the session origin.  
[Rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshTransform.Rotation.html) | The rotation of the mesh, relative to the session origin.  
[Scale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshTransform.Scale.html) | The scale of the mesh, relative to the session origin.  
[Timestamp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshTransform.Timestamp.html) | The timestamp associated with this transform.  
### Constructors
Constructor | Description  
---|---  
[MeshTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshTransform-ctor.html) | Creates a new MeshTransform.  
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMeshSubsystem.SetBoundingVolume.html

#  [XRMeshSubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMeshSubsystem.html).SetBoundingVolume
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
## Declaration
public bool SetBoundingVolume([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) origin, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) extents); 
### Description
Set the bounding volume to restrict the space in which Unity generates and tracks Meshes.  
  
The bounding volume is an Axis Aligned Bounding Box (AABB) centered at the `origin` and extends in each dimension as defined in `extents`.  
  
The units of measurement depend on the provider.
* * *

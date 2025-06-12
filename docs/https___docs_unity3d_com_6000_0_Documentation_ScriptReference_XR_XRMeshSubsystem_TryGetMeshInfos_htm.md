* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMeshSubsystem.TryGetMeshInfos.html

#  [XRMeshSubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMeshSubsystem.html).TryGetMeshInfos
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
public bool TryGetMeshInfos(List<MeshInfo> meshInfosOut); 
### Parameters
Parameter | Description  
---|---  
meshInfosOut | A `List` of [MeshInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshInfo.html)s to be filled. Passing `null` will throw an `ArgumentNullException`.  
### Returns
**bool** `True` if the `List` was populated. 
### Description
Gets information about every Mesh the system currently tracks.
Use this to determine which meshes have been added, changed, or removed.  
  
**Note:** This method provides state changes since the last time the method was called. Typically, a single system should manage this information.  
  
Additional resources: [XRMeshSubsystem.GenerateMeshAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMeshSubsystem.GenerateMeshAsync.html)
* * *

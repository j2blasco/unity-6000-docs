* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRInputSubsystem.TryGetBoundaryPoints.html

#  [XRInputSubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRInputSubsystem.html).TryGetBoundaryPoints
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
public bool TryGetBoundaryPoints(List<Vector3> boundaryPoints); 
### Parameters
Parameter | Description  
---|---  
boundaryPoints | The list of boundary points.  
### Returns
**bool** True if this [XRInputSubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRInputSubsystem.html) supports boundary points and they are available. Returns false otherwise. 
### Description
Gets the list of 3D position values that represents the SDK-set boundary.
* * *

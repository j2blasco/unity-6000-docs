* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.SetDistanceReferencePoint.html

#  [CullingGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.html).SetDistanceReferencePoint
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
public void SetDistanceReferencePoint([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point); 
## Declaration
public void SetDistanceReferencePoint([Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) transform); 
### Parameters
Parameter | Description  
---|---  
point | A fixed point to measure the distance from.  
transform | A transform to measure the distance from. The transform's position will be automatically tracked.  
### Description
Set the reference point from which distance bands are measured.
Additional resources: [CullingGroup.SetBoundingDistances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.SetBoundingDistances.html).
* * *

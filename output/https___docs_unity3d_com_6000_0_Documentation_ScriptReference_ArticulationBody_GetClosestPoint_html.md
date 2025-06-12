* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetClosestPoint.html

#  [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).GetClosestPoint
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ArticulationBody.html "Go to ArticulationBody Component in the Manual")
## Declaration
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) GetClosestPoint([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point); 
### Parameters
Parameter | Description  
---|---  
point | The point of interest.  
### Returns
**Vector3** The point on the surfaces of all Colliders attached to this articulation body that is closest to the given one. 
### Description
Return the point on the articulation body that is closest to a given one.
This returns the input point in case it was not possible to calculate the actual closest point for some reason.
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-suspensionDistance.html

#  [WheelCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.html).suspensionDistance
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WheelCollider.html "Go to WheelCollider Component in the Manual")
suspensionDistance; 
### Description
Maximum extension distance of wheel suspension, measured in local space.
Suspension always extends downwards the local y-axis. Suspension travel will be scaled by the transform's scale. The value `suspensionDistance` is the distance that the wheel travels as it moves along the local up vector of the rigid body from the coordinate of the wheel center at maximum spring elongation to the coordinateof the wheel center at maximum spring compression. It is expressed in metres. The range of suspension travel will be scaled by the transform's scale.
* * *

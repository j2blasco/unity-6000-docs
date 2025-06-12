* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterJoint-projectionDistance.html

#  [CharacterJoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterJoint.html).projectionDistance
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterJoint.html "Go to CharacterJoint Component in the Manual")
projectionDistance; 
### Description
Set the linear tolerance threshold for projection.
If the joint separates by more than this distance along its locked degrees of freedom, the solver will move the bodies to close the distance.  
  
Setting a very small tolerance may result in simulation jitter or other artifacts.  
  
Sometimes it is not possible to project (for example when the joints form a cycle).
* * *

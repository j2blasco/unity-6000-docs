* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-operator_eq.html

#  [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).operator ==
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Quaternion.html "Go to Quaternion Component in the Manual")
operator ==([Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) lhs, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rhs); 
### Description
Are two quaternions equal to each other?
This function tests whether dot product of two quaternions is close to 1.0.  
  
Note that because quaternions can represent rotations that are up to two full revolutions (720 degrees), this comparison can return `false` even if resulting rotations look the same.
* * *

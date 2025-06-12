* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pose-operator_eq.html

#  [Pose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pose.html).operator ==
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
operator ==([Pose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pose.html) a, [Pose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pose.html) b); 
### Description
Returns true if two poses are equal.
The equals operator returns true if two Poses are equivalent. Equivalent in this sense is determined by calling into the Equal operators of the internal Quaternion and Vector members of the pose. If both Quaternion and Vector members are deemed equal, then the two poses are equivalent. 
* * *

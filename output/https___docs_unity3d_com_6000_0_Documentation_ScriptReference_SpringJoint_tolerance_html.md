* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpringJoint-tolerance.html

#  [SpringJoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpringJoint.html).tolerance
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SpringJoint.html "Go to SpringJoint Component in the Manual")
tolerance; 
### Description
The maximum allowed error between the current spring length and the length defined by [minDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpringJoint-minDistance.html) and [maxDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpringJoint-maxDistance.html).
If the tolerance is set very high the solver might not run and the spring would effectively not exist.  
  
If the tolerance is set close to zero very short spring lengths are possible, but at the increased cost of running the solver more often.
* * *

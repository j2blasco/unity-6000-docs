* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.SetLocalPositionAndRotation.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).SetLocalPositionAndRotation
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html "Go to Transform Component in the Manual")
## Declaration
public void SetLocalPositionAndRotation([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) localPosition, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) localRotation); 
### Description
Sets the position and rotation of the Transform component in local space (i.e. relative to its parent transform).
When setting both the position and rotation of a transform, calling this method is slightly more efficient than assigning to localPosition and localRotation individually.  
  
If the transform has no parent, then calling this is equivalent to calling SetPositionAndRotation.
* * *

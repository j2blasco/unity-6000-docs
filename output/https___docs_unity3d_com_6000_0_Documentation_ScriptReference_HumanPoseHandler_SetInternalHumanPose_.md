* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPoseHandler.SetInternalHumanPose.html

#  [HumanPoseHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPoseHandler.html).SetInternalHumanPose
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
public void SetInternalHumanPose(ref [HumanPose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPose.html) humanPose); 
### Parameters
Parameter | Description  
---|---  
humanPose | The human pose to set. In the human pose, the `bodyPosition` and `bodyRotation` are the position and rotation of the approximate center of mass of the humanoid. This is relative to the humanoid root transform and it is normalized: the local position is divided by `avatar` human scale.  
### Description
Stores the specified human pose as the internal human pose inside the human pose handler.
If the human pose handler is not bound to a transform hierarchy representing a humanoid in the scene, the humanoids's root transform is considered to be the identity transform.
* * *

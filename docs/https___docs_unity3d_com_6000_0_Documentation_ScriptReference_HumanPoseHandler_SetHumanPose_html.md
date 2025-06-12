* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPoseHandler.SetHumanPose.html

#  [HumanPoseHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPoseHandler.html).SetHumanPose
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
public void SetHumanPose(ref [HumanPose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPose.html) humanPose); 
### Parameters
Parameter | Description  
---|---  
humanPose | The human pose to set. In the human pose, the `bodyPosition` and `bodyRotation` are the position and rotation of the approximate center of mass of the humanoid. This is relative to the humanoid root transform and it is normalized: the local position is divided by `avatar` human scale.  
### Description
Stores the specified human pose inside the human pose handler.
If the `HumanPoseHander` was constructed from an `avatar` and a `root`, the human pose is applied to the transform hierarchy representing the humanoid in the scene. If the `HumanPoseHander` was constructed from an `avatar` and `jointPaths`, the human pose is not bound to a transform hierarchy.
* * *

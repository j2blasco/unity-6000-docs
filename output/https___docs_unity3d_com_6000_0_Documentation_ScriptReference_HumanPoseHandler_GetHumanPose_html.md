* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPoseHandler.GetHumanPose.html

#  [HumanPoseHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPoseHandler.html).GetHumanPose
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
public void GetHumanPose(ref [HumanPose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPose.html) humanPose); 
### Parameters
Parameter | Description  
---|---  
humanPose | The output human pose. In the human pose, the `bodyPosition` and `bodyRotation` are the position and rotation of the approximate center of mass of the humanoid in world space. `bodyPosition` is normalized: the position is divided by `avatar` human scale.  
### Description
Computes a human pose from the avatar skeleton, stores the pose in the human pose handler, and returns the human pose.
If the human pose handler was constructed with `jointPaths`, it is not bound to a skeleton transform hierarchy. In this case, `GetHumanPose` returns the internally stored human pose as the output.
* * *

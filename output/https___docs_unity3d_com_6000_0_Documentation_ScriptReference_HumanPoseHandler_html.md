* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPoseHandler.html

# HumanPoseHandler
class in UnityEngine
/
Implemented in:[UnityEngine.AnimationModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AnimationModule.html)
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
### Description
Use this class to create, read, and write the [HumanPose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPose.html) for a humanoid avatar skeleton hierarchy or an avatar pose.
### Constructors
Constructor | Description  
---|---  
[HumanPoseHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPoseHandler-ctor.html) | Creates a human pose handler from an avatar and a root transform and either a list of joint paths.  
### Public Methods
Method | Description  
---|---  
[GetHumanPose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPoseHandler.GetHumanPose.html) | Computes a human pose from the avatar skeleton, stores the pose in the human pose handler, and returns the human pose.  
[GetInternalAvatarPose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPoseHandler.GetInternalAvatarPose.html) | Gets the internal human pose stored in the human pose handler and converts it to an avatar pose.  
[GetInternalHumanPose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPoseHandler.GetInternalHumanPose.html) | Gets the internal human pose stored in the human pose handler.  
[SetHumanPose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPoseHandler.SetHumanPose.html) | Stores the specified human pose inside the human pose handler.  
[SetInternalAvatarPose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPoseHandler.SetInternalAvatarPose.html) | Converts an avatar pose to a human pose and stores it as the internal human pose inside the human pose handler.  
[SetInternalHumanPose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPoseHandler.SetInternalHumanPose.html) | Stores the specified human pose as the internal human pose inside the human pose handler.  
* * *

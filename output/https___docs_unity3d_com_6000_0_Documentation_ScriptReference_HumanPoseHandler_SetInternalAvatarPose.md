* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPoseHandler.SetInternalAvatarPose.html

#  [HumanPoseHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanPoseHandler.html).SetInternalAvatarPose
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
public void SetInternalAvatarPose(NativeArray<float> avatarPose); 
### Parameters
Parameter | Description  
---|---  
avatarPose | The input avatar pose. The avatar pose is expressed as an array of floats. The floats represent the translation and rotation of the joints as local transforms. Each joint local transform is represented by 3 floats for the translation and 4 floats for the rotation (expressed as a quaternion). The joint transform is stored in the array in the same order as the joint paths in the `jointPaths` parameter used to construct the human pose handler. For example, if the human pose handler was constructed with 20 joint paths, the `avatarPose` parameter should be an array of 140 floats.  
### Description
Converts an avatar pose to a human pose and stores it as the internal human pose inside the human pose handler.
If the human pose handler was constructed with a skeleton root transform, this method does nothing.
* * *

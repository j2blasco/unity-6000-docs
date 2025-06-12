* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetBoneTransform.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).GetBoneTransform
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animator.html "Go to Animator Component in the Manual")
## Declaration
public [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) GetBoneTransform([HumanBodyBones](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanBodyBones.html) humanBoneId); 
### Parameters
Parameter | Description  
---|---  
humanBoneId | The human bone to be queried. See the [HumanBodyBones](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanBodyBones.html) enum for a list of possible values.  
### Returns
**Transform** Returns the [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) mapped to the human bone. Returns null if the human bone has no [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html). 
### Description
Retrieves the [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) mapped to a human bone based on its id.
Throws **InvalidOperationException** when Animator.avatar is _null_.  
  
Throws **InvalidOperationException** when Animator.avatar is not a valid avatar.  
  
Throws **InvalidOperationException** when Animator.avatar is not a Humanoid avatar.  
  
Throws **IndexOutOfRangeException** when humanBoneId is not between 0 and HumanBodyBones.LastBone.
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.SetAdditiveReferencePose.html

#  [AnimationUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.html).SetAdditiveReferencePose
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
public static void SetAdditiveReferencePose([AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip, [AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) referenceClip, float time); 
### Parameters
Parameter | Description  
---|---  
clip | The animation clip to use.  
referenceClip | The animation clip containing the reference pose.  
time | The time that when the reference pose occurs in `referenceClip`.  
### Description
Sets the additive reference pose from `referenceClip` at `time` for animation clip `clip`.
By default, an animation clip used in an additive layer uses the pose at time 0 as its reference pose. This is a big limitation as the reference pose need to be in the played clip.  
This function allow you to change this behaviour and use a reference pose from any clip.
* * *

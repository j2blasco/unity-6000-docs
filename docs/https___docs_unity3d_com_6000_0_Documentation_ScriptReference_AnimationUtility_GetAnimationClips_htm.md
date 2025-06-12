* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetAnimationClips.html

#  [AnimationUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.html).GetAnimationClips
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
**Obsolete** GetAnimationClips(Animation) is deprecated. Use GetAnimationClips(GameObject) instead.
## Declaration
public static AnimationClip[] GetAnimationClips([Animation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) component); 
## Declaration
public static AnimationClip[] GetAnimationClips([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject); 
### Description
Retrieves an array of animation clips associated with a GameObject or component. `GetAnimationClips(Animation)` is obsolete and has been replaced with `GetAnimationClips(GameObject)`.
This method retrieves animation clips from the [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) or [Animation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) component. This method works with any component that has implemented the [IAnimationClipSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IAnimationClipSource.html) interface.
* * *

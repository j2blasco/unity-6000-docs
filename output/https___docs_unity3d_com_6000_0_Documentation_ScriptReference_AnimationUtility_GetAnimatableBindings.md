* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetAnimatableBindings.html

#  [AnimationUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.html).GetAnimatableBindings
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
public static EditorCurveBinding[] GetAnimatableBindings([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) targetObject, [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) root); 
### Description
Retrieves the animatable bindings for a specific GameObject.
Use this method to find which can be animated for a GameObject.  
  
The root GameObject does not need to be an actual root, but it must be higher in the hierarchy than the target. The target and root may also be the same GameObject.
* * *

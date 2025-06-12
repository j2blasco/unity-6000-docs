* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.CreateAnimatorControllerAtPathWithClip.html

#  [AnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.html).CreateAnimatorControllerAtPathWithClip
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
public static [Animations.AnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.html) CreateAnimatorControllerAtPathWithClip(string path, [AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip); 
### Parameters
Parameter | Description  
---|---  
path | The path where the AnimatorController will be created.  
clip | The default clip that will be played by the AnimatorController.  
### Description
Creates an AnimatorController at the given path, and automatically create an AnimatorLayer with an AnimatorStateMachine that will add a State with the AnimationClip in it.
This function pushes an Undo operation.
* * *

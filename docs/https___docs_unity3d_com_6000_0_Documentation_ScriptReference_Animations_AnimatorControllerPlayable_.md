* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorControllerPlayable.SetTrigger.html

#  [AnimatorControllerPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorControllerPlayable.html).SetTrigger
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
public void SetTrigger(string name); 
## Declaration
public void SetTrigger(int id); 
### Parameters
Parameter | Description  
---|---  
name | The parameter name.  
id | The parameter ID.  
### Description
Sets the value of the given trigger parameter.
This method allows you to set (i.e. activate) an animation trigger, to cause a change in flow in the state machine of an animator controller. The [Animation Parameters](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationParameters.html) page describes the purpose of the Animator Controller Parameters window. `Trigger` is one of the 4 selectable options. Selecting this adds a `Trigger` to the list of chosen parameters. Once this is added to the selected list it can be named. Unlike `bool`s which have the same `true/false` option, `Trigger`s have a `true` option which automatically returns back to `false`. A typical example might be to have a Jump option. If this option is entered during run-time the character will jump. At the end of the Jump the previous motion (perhaps a walk or run state) will be returned to.
* * *

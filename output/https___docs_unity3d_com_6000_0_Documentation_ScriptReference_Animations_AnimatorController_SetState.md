* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.SetStateEffectiveMotion.html

#  [AnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.html).SetStateEffectiveMotion
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
public void SetStateEffectiveMotion([Animations.AnimatorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.html) state, [Motion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Motion.html) motion); 
## Declaration
public void SetStateEffectiveMotion([Animations.AnimatorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.html) state, [Motion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Motion.html) motion, int layerIndex); 
### Parameters
Parameter | Description  
---|---  
state | The AnimatorState which we want to set the Motion.  
motion | The Motion that will be set.  
layerIndex | The layer to set the Motion.  
### Description
Sets the effective Motion for the AnimatorState. The Motion is either stored in the AnimatorStateMachine or in the AnimatorLayer's ovverrides. Use this function to set the Motion that is effectively used.
* * *

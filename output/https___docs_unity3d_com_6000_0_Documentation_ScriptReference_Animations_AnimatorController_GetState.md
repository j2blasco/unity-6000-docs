* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.GetStateEffectiveBehaviours.html

#  [AnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.html).GetStateEffectiveBehaviours
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
public StateMachineBehaviour[] GetStateEffectiveBehaviours([Animations.AnimatorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.html) state, int layerIndex); 
### Parameters
Parameter | Description  
---|---  
state | The AnimatorState which we want the Behaviour list.  
layerIndex | The layer that is queried.  
### Description
Gets the effective state machine behaviour list for the AnimatorState. Behaviours are either stored in the AnimatorStateMachine or in the AnimatorLayer's ovverrides. Use this function to get Behaviour list that is effectively used.
* * *

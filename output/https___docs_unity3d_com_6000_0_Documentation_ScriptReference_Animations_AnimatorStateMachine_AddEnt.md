* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.AddEntryTransition.html

#  [AnimatorStateMachine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.html).AddEntryTransition
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
public [Animations.AnimatorTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorTransition.html) AddEntryTransition([Animations.AnimatorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.html) destinationState); 
## Declaration
public [Animations.AnimatorTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorTransition.html) AddEntryTransition([Animations.AnimatorStateMachine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.html) destinationStateMachine); 
### Parameters
Parameter | Description  
---|---  
destinationState | The destination [AnimatorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.html) state.  
destinationStateMachine | The destination [AnimatorStateMachine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.html) state machine.  
### Description
Utility function to add an incoming transition to the exit of it's parent state machine.
The transition asset that is created is added as a sub asset of the state.  
An example showing usage of this API can be found at the [AnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.html) page.
* * *

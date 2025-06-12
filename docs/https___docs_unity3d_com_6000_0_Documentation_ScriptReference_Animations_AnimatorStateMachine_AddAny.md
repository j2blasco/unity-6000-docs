* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.AddAnyStateTransition.html

#  [AnimatorStateMachine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.html).AddAnyStateTransition
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
public [Animations.AnimatorStateTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition.html) AddAnyStateTransition([Animations.AnimatorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.html) destinationState); 
## Declaration
public [Animations.AnimatorStateTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition.html) AddAnyStateTransition([Animations.AnimatorStateMachine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.html) destinationStateMachine); 
### Parameters
Parameter | Description  
---|---  
destinationState | The destination state.  
destinationStateMachine | The destination statemachine.  
### Description
Utility function to add an AnyState transition to the specified state or statemachine.
The transition asset that is created is added as a sub asset of the state machine. Its important that AnyStateTransitions are added to the root state machine. AnyStateTranistions added to a sub state machine will be discarded at runtime. This function pushes an Undo operation.
* * *

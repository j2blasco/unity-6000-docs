* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.AddTransition.html

#  [AnimatorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.html).AddTransition
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
public [Animations.AnimatorStateTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition.html) AddTransition([Animations.AnimatorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.html) destinationState); 
## Declaration
public [Animations.AnimatorStateTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition.html) AddTransition([Animations.AnimatorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.html) destinationState, bool defaultExitTime); 
### Parameters
Parameter | Description  
---|---  
defaultExitTime | If true, the exit time will be the equivalent of 0.25 second.  
destinationState | The destination state.  
### Description
Utility function to add an outgoing transition to the destination state.
The transition asset that is created is added as a sub asset of the state. This function pushes an Undo operation.
* * *
## Declaration
public [Animations.AnimatorStateTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition.html) AddTransition([Animations.AnimatorStateMachine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.html) destinationStateMachine); 
## Declaration
public [Animations.AnimatorStateTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition.html) AddTransition([Animations.AnimatorStateMachine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.html) destinationStateMachine, bool defaultExitTime); 
### Parameters
Parameter | Description  
---|---  
defaultExitTime | If true, the exit time will be the equivalent of 0.25 second.  
destinationStateMachine | The destination state machine.  
### Description
Utility function to add an outgoing transition to the destination state machine.
The transition asset that is created is added as a sub asset of the state. This function pushes an Undo operation.
* * *
## Declaration
public void AddTransition([Animations.AnimatorStateTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition.html) transition); 
### Parameters
Parameter | Description  
---|---  
transition | The transition to add.  
### Description
Utility function to add an outgoing transition.
This function pushes an Undo operation.
* * *

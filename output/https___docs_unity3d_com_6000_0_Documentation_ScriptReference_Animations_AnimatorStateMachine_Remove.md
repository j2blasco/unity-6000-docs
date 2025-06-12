* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.RemoveState.html

#  [AnimatorStateMachine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.html).RemoveState
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
public void RemoveState([Animations.AnimatorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.html) state); 
### Parameters
Parameter | Description  
---|---  
state | The state to remove.  
### Description
Utility function to remove a state from the state machine.
If the state is a sub asset of the state machine, it will be deleted. This function pushes an Undo operation.
* * *

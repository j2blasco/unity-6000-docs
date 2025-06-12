* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateMachineExit.html

#  [StateMachineBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.html).OnStateMachineExit
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
public void OnStateMachineExit([Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator, int stateMachinePathHash); 
### Parameters
Parameter | Description  
---|---  
animator | The Animator evaluating the state machine.  
stateMachinePathHash | The hash of the full path to the state machine.  
### Description
Invoked on the last update frame when taking a transition out of a StateMachine. Implement this message to influence the exit transition out of the sub-state machine
**Notes** :  
- This message will only be invoked when a State Machine exit transition is taken. It will not be invoked if a direct transition to a state machine sub-state is taken.  
- Since this message is invoked during the evaluation of the state machine and can influence the transitions taken, implementing this message in your state machine prevents multithreaded state machine evaluation and may be a performance concern. 
* * *

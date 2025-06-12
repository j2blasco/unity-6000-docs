* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateEnter.html

#  [StateMachineBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.html).OnStateEnter(Animator animator, AnimatorStateInfo animatorStateInfo, int layerIndex)
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
### Parameters
Parameter | Description  
---|---  
animator | The Animator evaluating this state machine.  
animatorStateInfo | Information about the entered state.  
layerIndex | The current layer being evaluated.  
### Description
Invoked on the first update frame when a state machine evaluates this state. Implement this message to react to a new state starting.
OnStateEnter is invoked when a transition to a state is initiated. It will be invoked after [OnStateUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateUpdate.html) of the current state.   
**Note** : OnStateEnter may be invoked multiple times on the same state if that state is synchronized on multiple layers. 
* * *

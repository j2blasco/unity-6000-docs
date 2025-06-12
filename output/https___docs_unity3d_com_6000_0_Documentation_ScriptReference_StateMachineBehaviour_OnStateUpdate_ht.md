* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateUpdate.html

#  [StateMachineBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.html).OnStateUpdate(Animator animator, AnimatorStateInfo animatorStateInfo, int layerIndex)
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
animatorStateInfo | Information about the state being evaluated.  
layerIndex | The current layer being evaluated.  
### Description
Invoked on each update frame except for the first and last frame. Implement this message to execute custom logic on a state by state basis.
OnStateUpdate is invoked every frame for the currently evaluated state, as well the next state and the interrupted state if applicable.  
**Note** : OnStateUpdate may be invoked multiple times on the same state if that state is synchronized on multiple layers. 
* * *

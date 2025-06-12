* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.AddEffectiveStateMachineBehaviour.html

#  [AnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.html).AddEffectiveStateMachineBehaviour
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
public T AddEffectiveStateMachineBehaviour([Animations.AnimatorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.html) state, int layerIndex); 
### Parameters
Parameter | Description  
---|---  
state | The AnimatorState to add the Behaviour to.  
layerIndex | The layer index.  
### Description
Adds a state machine behaviour class of a specific type to the AnimatorState for layer layerIndex. This method should be used when you are dealing with synchronized layer and would like to add a state machine behaviour on a synchronized layer. Note that there is no corresponding "Remove" method. To remove a state machine behaviour, use [Object.Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html).
* * *
## Declaration
public [StateMachineBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.html) AddEffectiveStateMachineBehaviour(Type stateMachineBehaviourType, [Animations.AnimatorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.html) state, int layerIndex); 
### Parameters
Parameter | Description  
---|---  
stateMachineBehaviourType | The type of state machine behaviour to add.  
state | The AnimatorState to add the Behaviour to.  
layerIndex | The layer index.  
### Description
The non-generic version of this method.
* * *

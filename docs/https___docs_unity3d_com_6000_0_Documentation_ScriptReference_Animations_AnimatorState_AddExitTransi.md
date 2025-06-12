* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.AddExitTransition.html

#  [AnimatorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.html).AddExitTransition
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
public [Animations.AnimatorStateTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition.html) AddExitTransition(); 
## Declaration
public [Animations.AnimatorStateTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition.html) AddExitTransition(bool defaultExitTime); 
### Parameters
Parameter | Description  
---|---  
defaultExitTime | If true, the exit time will be the equivalent of 0.25 second.  
### Returns
**AnimatorStateTransition** The [AnimatorStateTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition.html) that was added. 
### Description
Utility function to add an outgoing transition to the exit of the state's parent state machine.
The transition asset that is created is added as a sub asset of the state.  
An example showing usage of this API can be found at the [AnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.html) page.
* * *

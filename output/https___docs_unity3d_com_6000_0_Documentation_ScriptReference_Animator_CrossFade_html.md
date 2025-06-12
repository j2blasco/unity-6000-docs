* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.CrossFade.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).CrossFade
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animator.html "Go to Animator Component in the Manual")
## Declaration
public void CrossFade(string stateName, float normalizedTransitionDuration, int layer = -1, float normalizedTimeOffset = float.NegativeInfinity, float normalizedTransitionTime = 0.0f); 
## Declaration
public void CrossFade(int stateHashName, float normalizedTransitionDuration, int layer = -1, float normalizedTimeOffset = 0.0f, float normalizedTransitionTime = 0.0f); 
### Parameters
Parameter | Description  
---|---  
stateName | The name of the state.  
stateHashName | The hash name of the state.  
normalizedTransitionDuration | The duration of the transition (normalized).  
layer | The layer where the crossfade occurs.  
normalizedTimeOffset | The time of the state (normalized).  
normalizedTransitionTime | The time of the transition (normalized).  
### Description
Creates a crossfade from the current state to any other state using normalized times.
When you specify a state name, or the string used to generate a hash, it should include the name of the parent layer. For example, if you have a `Run` state in the `Base Layer`, the name is `Base Layer.Run`.  
  
Additional resources: [Animator.CrossFadeInFixedTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.CrossFadeInFixedTime.html) for times in seconds.
* * *

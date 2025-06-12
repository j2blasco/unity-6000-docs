* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.GetPropagateSetTime.html

#  [PlayableExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.html).GetPropagateSetTime
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
public static bool GetPropagateSetTime(U playable); 
### Parameters
Parameter | Description  
---|---  
playable | The [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) used by this operation.  
### Returns
**bool** True if time propagation is enabled. 
### Description
Returns the time propagation behavior of this [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html).
When enabled, the playable will propagate its local time to its inputs.
When disabled, the playable will not propagate its local time to its inputs.
By default, this is disabled. It can be used to automatically synchronize the local time between an input and an output.
Use this templated extension method on any type that inherits from [IPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.IPlayable.html).
* * *

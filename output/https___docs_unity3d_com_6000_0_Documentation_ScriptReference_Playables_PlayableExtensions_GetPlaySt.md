* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.GetPlayState.html

#  [PlayableExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.html).GetPlayState
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
public static [Playables.PlayState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayState.html) GetPlayState(U playable); 
### Parameters
Parameter | Description  
---|---  
playable | The [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) used by this operation.  
### Returns
**PlayState** The current PlayState of the [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html). 
### Description
Returns the current PlayState of the [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html).
[PlayState.Playing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayState.Playing.html): The local time of this [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) will be updated during the evaluation of the [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html).  
[PlayState.Paused](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayState.Paused.html): The local time of this [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) will not be updated during the evaluation of the [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html).  
PlayState.Delayed: The delay is elapsed during the evaluation of the [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html), the [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) will not start as long as there is still a delay.  
  
Use this templated extension method on any type that inherits from [IPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.IPlayable.html).
* * *

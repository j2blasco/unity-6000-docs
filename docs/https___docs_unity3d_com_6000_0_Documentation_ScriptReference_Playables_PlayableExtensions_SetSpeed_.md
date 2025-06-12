* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.SetSpeed.html

#  [PlayableExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.html).SetSpeed
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
public static void SetSpeed(U playable, double value); 
### Parameters
Parameter | Description  
---|---  
playable | The [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) used by this operation.  
value | The new speed.  
### Description
Changes the speed multiplier that is applied to the the current [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html).
This affects the speed at which the local time is incremented when the [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) is playing.
Use this templated extension method on any type that inherits from [IPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.IPlayable.html).
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.IsDone.html

#  [PlayableExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.html).IsDone
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
public static bool IsDone(U playable); 
### Parameters
Parameter | Description  
---|---  
playable | The [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) used by this operation.  
### Returns
**bool** True if the playable has completed its operation, false otherwise. 
### Description
Returns a flag indicating that a playable has completed its operation.
If the duration of the playable is set, when the time of the playable reaches its duration during playback this flag will be set to true.
Use this templated extension method on any type that inherits from [IPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.IPlayable.html).
* * *

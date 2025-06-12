* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.SetScheduledStartTime.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).SetScheduledStartTime
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html "Go to AudioSource Component in the Manual")
## Declaration
public void SetScheduledStartTime(double time); 
### Parameters
Parameter | Description  
---|---  
time | Time in seconds.  
### Description
Changes the time at which a sound that has already been scheduled to play will start.
Notice that depending on the timing not all rescheduling requests can be fulfilled.  
  
One interesting use case for this is stinger sound effects that are initiated by game events, but that you also want to be synchronized to specific beats in music. Then this function can be used to defer the stinger until the next musical transition.  
  
**Note:** In general it is better to use [PlayScheduled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.PlayScheduled.html) to cue up audio. Only use SetScheduledStartTime if you have scheduled an audio clip to play in the future and you need to change the time at which it starts. Calling SetScheduledStartTime will not cause an un-scheduled audio clip to play.  
  
Additional resources: [PlayScheduled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.PlayScheduled.html).
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-controlledAudioTrackMaxCount.html

#  [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).controlledAudioTrackMaxCount
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
controlledAudioTrackMaxCount; 
### Description
Maximum number of audio tracks that can be controlled. (Read Only)
When playing audio from a URL, the number of audio tracks is not known in advance. It is up to the user to specify the number of controlled audio tracks through [VideoPlayer.controlledAudioTrackCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-controlledAudioTrackCount.html). Other tracks will be ignored and silenced. In this scenario, [VideoPlayer.audioTrackCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-audioTrackCount.html) will be set to the actual number of tracks during playback, after preparation is complete.  
  
Additional resources: [VideoPlayer.Prepare](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Prepare.html).
* * *

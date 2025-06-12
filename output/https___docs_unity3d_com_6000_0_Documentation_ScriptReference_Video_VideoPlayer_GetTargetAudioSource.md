* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.GetTargetAudioSource.html

#  [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).GetTargetAudioSource
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
public [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) GetTargetAudioSource(ushort trackIndex); 
### Parameters
Parameter | Description  
---|---  
trackIndex | Index of the audio track for which the [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) is wanted.  
### Returns
**AudioSource** The source associated with the audio track. 
### Description
Gets the [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) that will receive audio samples for the specified track if [VideoPlayer.audioOutputMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-audioOutputMode.html) is set to [VideoAudioOutputMode.AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoAudioOutputMode.AudioSource.html).
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.GetAudioChannelCount.html

#  [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).GetAudioChannelCount
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
public ushort GetAudioChannelCount(ushort trackIndex); 
### Parameters
Parameter | Description  
---|---  
trackIndex | Index for the audio track being queried.  
### Returns
**ushort** Number of audio channels. 
### Description
The number of audio channels in the specified audio track.
For URL sources, this will only be set once the source preparation is completed. See [VideoPlayer.Prepare](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Prepare.html).
* * *

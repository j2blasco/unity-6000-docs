* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.GetAudioSampleRate.html

#  [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).GetAudioSampleRate
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
public uint GetAudioSampleRate(ushort trackIndex); 
### Parameters
Parameter | Description  
---|---  
trackIndex | Index of the audio track to query.  
### Returns
**uint** The sampling rate in Hertz. 
### Description
Gets the audio track sampling rate in Hertz.
For URL sources, this will only be set once the source preparation is completed. See [VideoPlayer.Prepare](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Prepare.html).
* * *

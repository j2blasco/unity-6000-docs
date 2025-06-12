* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaEncoder.AddSamples.html

#  [MediaEncoder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaEncoder.html).AddSamples
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
public bool AddSamples(ushort trackIndex, NativeArray<float> interleavedSamples); 
## Declaration
public bool AddSamples(NativeArray<float> interleavedSamples); 
### Parameters
Parameter | Description  
---|---  
trackIndex | Index of the track to which sample frames will be added.  
interleavedSamples | Sample frames to add. Samples are expected to be interleaved.  
### Returns
**bool** True if the operation succeeded. False otherwise. 
### Description
Appends sample frames to the specified audio track.
Keep the number of video frames and audio samples aligned so that each track is syncrhonized as much as possible. For instance, a file with 30FPS video and 48KHz video, each addition of one video frame should be followed by the addition of a buffer of 1600 sample frames.
* * *

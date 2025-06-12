* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClipLoadType.html

# AudioClipLoadType
enumeration
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
### Description
Determines how the audio clip is loaded in.
Determines whether the audio clip will be either loaded in memory in compressed form, such that every playback will decode the data on the fly ("CompressedInMemory"), decompressed at Scene startup such that the clip can be played back at very low CPU usage and the audio data in it can be modified ("DecompressOnLoad"), or streamed directly from the disk which will typically result in the lowest memory usage, as only the data for a short stream buffer needs to be kept in memory ("Streaming").
### Properties
Property | Description  
---|---  
[DecompressOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClipLoadType.DecompressOnLoad.html) | The audio data is decompressed when the audio clip is loaded.  
[CompressedInMemory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClipLoadType.CompressedInMemory.html) | The audio data of the clip will be kept in memory in compressed form.  
[Streaming](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClipLoadType.Streaming.html) | Streams audio data from disk.  
* * *

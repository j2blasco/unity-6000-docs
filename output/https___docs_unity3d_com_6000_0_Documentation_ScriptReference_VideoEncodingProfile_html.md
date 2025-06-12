* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoEncodingProfile.html

# VideoEncodingProfile
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
Use the options in this enumeration to change the encoder profile.
H.264 profiles (Baseline, Main, and High) are compression and encoding standards that determine how the [MediaEncoder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaEncoder.html) compresses and encodes video files during recording. You can use the `MediaEncoder` to encode clips and choose the encoding profile via C#. The encoding profile you select influences the compatibility and compression efficiency of the H.264 codec. To record video, you can use the [Unity Recorder](https://docs.unity3d.com/Packages/com.unity.recorder@5.1/manual/index.html), which uses the `MediaEncoder` in its implementation, or you can implement your own custom recording logic to work directly with the `MediaEncoder` API.  
  
For a code example, refer to [H264EncoderAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.H264EncoderAttributes.html).  
  
This enum isn’t exposed in [VideoClipImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.html), so when you transcode video clips to H.264 during an import, Unity uses the baseline profile for maximum stability and compatibility.
### Properties
Property | Description  
---|---  
[H264Baseline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoEncodingProfile.H264Baseline.html) | Encode video with the baseline profile.  
[H264Main](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoEncodingProfile.H264Main.html) | Encode video using the main profile.  
[H264High](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoEncodingProfile.H264High.html) | Encode video with the high profile.  
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackEncoderAttributes-frameRate.html

#  [VideoTrackEncoderAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackEncoderAttributes.html).frameRate
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
[Media.MediaRational](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaRational.html) frameRate; 
### Description
The frame rate for the encoded video, in frames per second, expressed as a fraction.
To indicate that the track uses a variable frame rate (VFR), specify a frame rate of 0, or an invalid frame rate. In VFR mode, there is no pre-defined frame duration, which means that frames that you add using [MediaEncoder.AddFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaEncoder.AddFrame.html) must use the overload that receives a [MediaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaTime.html).
* * *

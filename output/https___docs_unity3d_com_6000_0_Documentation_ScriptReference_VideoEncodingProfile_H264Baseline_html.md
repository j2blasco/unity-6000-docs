* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoEncodingProfile.H264Baseline.html

#  [VideoEncodingProfile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoEncodingProfile.html).H264Baseline
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
Encode video with the baseline profile.
This is the most basic level of the encoder profiles. The decoding process for this profile is less complex, which is suitable for devices with lightweight processing. This profile doesn’t include advanced features, such as B-frames or Context-Adaptive Binary Arithmetic Coding (CABAC) which sometimes can cause bugs. Therefore, the baseline profile code is usually safer and less prone to bugs. The simpler the profile, the less the compression. As the baseline profile is the simplest of all three profiles, compression with this profile yields slightly bigger files. Use this profile for simpler devices with limited processing power, like mobile phones or embedded systems.
* * *

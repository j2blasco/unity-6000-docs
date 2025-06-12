* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-hdrBitDepth.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).hdrBitDepth
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html "Go to PlayerSettings Component in the Manual")
[HDRDisplayBitDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDRDisplayBitDepth.html) hdrBitDepth; 
### Description
The number of bits in each color channel for swap chain buffers.
The bit count defines the method Unity uses to render content to the display. When set to `10`, Unity uses the R10G10B10A2 buffer format, Rec2020 primaries, and ST2084 PQ encoding. When set to `16`, Unity uses the R16G16B16A16 buffer format, Rec709 primaries, and linear color (no encoding).
* * *

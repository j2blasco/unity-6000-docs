* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-maxFullFrameToneMapLuminance.html

#  [HDROutputSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings.html).maxFullFrameToneMapLuminance
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
maxFullFrameToneMapLuminance; 
### Description
Maximum input luminance at which gradation is preserved even when the entire screen is bright.
Measured in nits. This value is -1 if Unity cannot obtain a value from the HDR display. Accessing this member results in an exception if HDR is not available on the display. Use [HDROutputSettings.available](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-available.html) for the display to check that HDR is available.
* * *

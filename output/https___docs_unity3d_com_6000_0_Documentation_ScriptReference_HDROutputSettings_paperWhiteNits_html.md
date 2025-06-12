* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-paperWhiteNits.html

#  [HDROutputSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings.html).paperWhiteNits
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
paperWhiteNits; 
### Description
The base luminance of a white paper surface in nits or candela per square meter (cd/m2).
This value is used if [HDROutputSettings.automaticHDRTonemapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-automaticHDRTonemapping.html) is true. The higher this value, the brighter the resulting image appears on the HDR display.  
  
Unity only uses this value if [HDROutputSettings.automaticHDRTonemapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-automaticHDRTonemapping.html) is true and HDR is active on the display.  
  
Accessing this member results in an exception if HDR is not available on the display. Use [HDROutputSettings.available](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-available.html) for the display to check that HDR is available.
* * *

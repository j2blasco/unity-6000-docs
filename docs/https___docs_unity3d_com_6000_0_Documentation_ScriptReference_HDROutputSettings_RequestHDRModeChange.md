* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings.RequestHDRModeChange.html

#  [HDROutputSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings.html).RequestHDRModeChange
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
public void RequestHDRModeChange(bool enabled); 
### Parameters
Parameter | Description  
---|---  
enabled | Indicates whether HDR should be enabled.  
### Description
Use this function to request a change in the HDR Output Mode and in the value of [HDROutputSettings.active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-active.html).
When calling this function, Unity automatically sets the [HDROutputSettings.HDRModeChangeRequested](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings.HDRModeChangeRequested.html) property to `true` until the HDR Output Mode change completes.  
  
This functionality could be used to implement an in application menu allowing users to swap in or our of HDR display mode.  
  
Some platforms cannot swap in or out of HDR display mode at runtime. See [SystemInfo.hdrDisplaySupportFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-hdrDisplaySupportFlags.html) for more information.  
  
Accessing this member results in an exception if HDR is not available on the display. Use [HDROutputSettings.available](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-available.html) for the display to check that HDR is available.
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.TryGetDisplayRefreshRate.html

#  [XRDisplaySubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.html).TryGetDisplayRefreshRate
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
public bool TryGetDisplayRefreshRate(out float displayRefreshRate); 
### Parameters
Parameter | Description  
---|---  
hmdRefreshRate | Outputs the display refresh rate in Hz.  
### Returns
**bool** Returns true if the display refresh rate is available. Returns false if that rate is unavailable. 
### Description
Retrieves the refresh rate of the display as reported by the XR Plugin.
The XR plugin uses the display refresh rate as the target frame rate. This can be useful information for synchronizing fixed updates.  
  
Statistics are only available for SDKs that support this method, and they can vary based on hardware, the SDK, and the frame. You should always check the return value of this method before you use the statistic value from the out parameter.
* * *

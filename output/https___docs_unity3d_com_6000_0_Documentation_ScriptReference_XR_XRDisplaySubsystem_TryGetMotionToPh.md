* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.TryGetMotionToPhoton.html

#  [XRDisplaySubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.html).TryGetMotionToPhoton
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
public bool TryGetMotionToPhoton(out float motionToPhoton); 
### Parameters
Parameter | Description  
---|---  
motionToPhoton | Outputs the motion-to-photon value.  
### Returns
**bool** Returns true if the motion-to-photon value is available. Returns false otherwise. 
### Description
Retrieves the motion-to-photon value as reported by the XR Plugin.
The motion-to-photon represents latency. This latency is the difference between the last predicted tracking information and the moment that the scan-line of the target frame lights up on the display. You can use this to determine application latency.  
  
Statistics are only available for SDKs that support this method, and they can vary based on hardware, the SDK, and the frame. You should always check the return value of this method before you use the statistic value from the out parameter.
* * *

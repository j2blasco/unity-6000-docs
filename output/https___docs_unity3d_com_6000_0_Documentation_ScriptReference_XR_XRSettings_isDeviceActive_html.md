* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRSettings-isDeviceActive.html

#  [XRSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRSettings.html).isDeviceActive
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
isDeviceActive; 
### Description
Read-only value that can be used to determine if the XR device is active.
When true, Unity accepts input from the device and attempts to render to the device's display(s). Note that this returns true even if the device is not currently rendering due to lack of user presence (see XRDevice.userPresence). This can become false if a device is disconnected, could not be initialized (see XRSettings.LoadDeviceByName), or [XRSettings.enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRSettings-enabled.html) is set to false.  
  
XR output is automatically mirrored to the main display (if applicable). This can be controlled with [XRSettings.showDeviceView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRSettings-showDeviceView.html).  
  
The main window is still controlled by [Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html) and related APIs.
* * *

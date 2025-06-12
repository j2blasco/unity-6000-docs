* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem-scaleOfAllViewports.html

#  [XRDisplaySubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.html).scaleOfAllViewports
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
scaleOfAllViewports; 
### Description
Controls how much of the allocated display texture should be used for rendering.
Valid range is 0.0 to 1.0. This value can be changed at runtime without reallocating textures, which makes it useful for dynamically adjusting render resolution. Changes to this value take effect the next time the scene begins rendering (after LateUpdate).  
  
Some display providers might ignore this value or clamp it.  
  
This value is not supported with the legacy deferred renderer. If you attempt to change the value in the presence of camera that uses deferred rendering, Unity will ignore it and log a warning.
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTimingManager.html

# FrameTimingManager
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
The FrameTimingManager allows the user to capture and access FrameTiming data for multiple frames.
The FrameTimingManager is always active on Development Player builds. To use this feature for other build types, go to **Edit** > **Project Settings** > **Player** and enable the **Frame Timing Stats** property. The FrameTimingManager also depends on the **Dynamic Resolution** feature and so is only supported on platforms that support **Dynamic Resolution**.
### Static Methods
Method | Description  
---|---  
[CaptureFrameTimings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTimingManager.CaptureFrameTimings.html) | This function triggers the FrameTimingManager to capture a snapshot of FrameTiming's data, that can then be accessed by the user.  
[GetCpuTimerFrequency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTimingManager.GetCpuTimerFrequency.html) | This returns the frequency of CPU timer on the current platform, used to interpret timing results. If the platform does not support returning this value it will return 0.  
[GetGpuTimerFrequency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTimingManager.GetGpuTimerFrequency.html) | This returns the frequency of GPU timer on the current platform, used to interpret timing results. If the platform does not support returning this value it will return 0.  
[GetLatestTimings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTimingManager.GetLatestTimings.html) | Allows the user to access the currently captured FrameTimings.  
[GetVSyncsPerSecond](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTimingManager.GetVSyncsPerSecond.html) | This returns the number of vsyncs per second on the current platform, used to interpret timing results. If the platform does not support returning this value it will return 0.  
[IsFeatureEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTimingManager.IsFeatureEnabled.html) | Check if frame timing statistics are enabled.  
* * *

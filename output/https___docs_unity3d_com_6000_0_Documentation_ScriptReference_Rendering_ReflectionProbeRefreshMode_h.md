* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeRefreshMode.html

# ReflectionProbeRefreshMode
enumeration
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
An enum describing the way a real-time reflection probe refreshes in the Player.
### Properties
Property | Description  
---|---  
[OnAwake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeRefreshMode.OnAwake.html) | Causes the probe to update only on the first frame it becomes visible. The probe will no longer update automatically, however you may subsequently use RenderProbe to refresh the probeAdditional resources: ReflectionProbe.RenderProbe.  
[EveryFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeRefreshMode.EveryFrame.html) | Causes Unity to update the probe's cubemap every frame. Note that updating a probe is very costly. Setting this option on too many probes could have a significant negative effect on frame rate. Use time-slicing to help improve performance.Additional resources: ReflectionProbeTimeSlicingMode.  
[ViaScripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeRefreshMode.ViaScripting.html) | Sets the probe to never be automatically updated by Unity while your game is running. Use this to completely control the probe refresh behavior by script.Additional resources: ReflectionProbe.RenderProbe.  
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RealtimeGICPUUsage.html

# RealtimeGICPUUsage
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
How much CPU usage to assign to the final lighting calculations at runtime.
How many CPU worker threads to create for Enlighten Realtime Global Illumination lighting calculations in the Player. Increasing this makes the system react faster to changes in lighting at a cost of using more CPU time. The higher the CPU Usage value, the more worker threads are created for solving Enlighten Realtime Global Illumination.  
  
**Please note** that some platforms will allow all CPUs to be occupied by worker threads whilst some have a max limit:  
**Android:** If the device is a bigLittle architecture, only the little CPUs will be used, otherwise it is CPUs - 1.  

### Properties
Property | Description  
---|---  
[Low](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RealtimeGICPUUsage.Low.html) | 25% of the allowed CPU threads are used as worker threads.  
[Medium](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RealtimeGICPUUsage.Medium.html) | 50% of the allowed CPU threads are used as worker threads.  
[High](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RealtimeGICPUUsage.High.html) | 75% of the allowed CPU threads are used as worker threads.  
[Unlimited](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RealtimeGICPUUsage.Unlimited.html) | 100% of the allowed CPU threads are used as worker threads.  
* * *

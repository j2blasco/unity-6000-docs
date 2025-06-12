* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameDebugger.html

# FrameDebugger
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
Controls the [Frame Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger.html) from a script.
The Frame Debugger lets you freeze playback for a running game on a particular frame and view the individual draw calls that are used to render that frame. In some cases it can be useful to know whether the Frame Debugger is currently active; you can use [FrameDebugger.enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameDebugger-enabled.html) to query that. Most common use case is to pause or disable some rendering techniques or effects that alter their behavior every frame. For example, various graphics techniques that jitter the camera projection every frame would likely benefit from disabling the jitter while the Frame Debugger is active.  
  
Additional resources: [Frame Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger.html) documentation.
### Static Properties
Property | Description  
---|---  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameDebugger-enabled.html) | Queries whether the Frame Debugger is enabled.  
* * *

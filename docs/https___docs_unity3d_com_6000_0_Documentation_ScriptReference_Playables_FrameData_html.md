* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData.html

# FrameData
struct in UnityEngine.Playables
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
This structure contains the frame information a [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) receives in Playable.PrepareFrame.
### Properties
Property | Description  
---|---  
[deltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData-deltaTime.html) | The interval between this frame and the preceding frame. The interval is unscaled and expressed in seconds.  
[effectiveParentSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData-effectiveParentSpeed.html) | The accumulated speed of the parent Playable during the PlayableGraph traversal.  
[effectivePlayState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData-effectivePlayState.html) | The accumulated play state of this playable.  
[effectiveSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData-effectiveSpeed.html) | The accumulated speed of the Playable during the PlayableGraph traversal.  
[effectiveWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData-effectiveWeight.html) | The accumulated weight of the Playable during the PlayableGraph traversal.  
[evaluationType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData-evaluationType.html) | Indicates the type of evaluation that caused PlayableGraph.PrepareFrame to be called.  
[frameId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData-frameId.html) | The current frame identifier.  
[output](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData-output.html) | The PlayableOutput that initiated this graph traversal.  
[seekOccurred](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData-seekOccurred.html) | Indicates that the local time was explicitly set.  
[timeHeld](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData-timeHeld.html) | Indicates the local time did not advance because it has reached the duration and the extrapolation mode is set to Hold.  
[timeLooped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData-timeLooped.html) | Indicates the local time wrapped because it has reached the duration and the extrapolation mode is set to Loop.  
[weight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData-weight.html) | The weight of the current Playable.  
* * *

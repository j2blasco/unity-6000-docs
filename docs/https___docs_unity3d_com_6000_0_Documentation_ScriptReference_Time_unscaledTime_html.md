* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-unscaledTime.html

#  [Time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html).unscaledTime
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
unscaledTime; 
### Description
The timeScale-independent time for this frame (Read Only). This is the time in seconds since the start of the game.
When called from inside MonoBehaviour's [FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.FixedUpdate.html), it returns [Time.fixedUnscaledTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedUnscaledTime.html).  
  
Unlike [Time.realtimeSinceStartup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-realtimeSinceStartup.html), this returns the same value if called multiple times in a single frame and when the Editor is paused. Unlike [Time.time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) this value is not affected by [Time.timeScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html) and [Time.maximumDeltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-maximumDeltaTime.html).  
  
See [Time and Frame Rate Management](https://docs.unity3d.com/6000.0/Documentation/Manual/managing-time-and-frame-rate.html) in the User Manual for more information about how this property relates to the other Time properties.
* * *

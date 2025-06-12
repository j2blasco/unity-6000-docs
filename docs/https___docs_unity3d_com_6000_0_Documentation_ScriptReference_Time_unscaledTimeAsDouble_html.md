* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-unscaledTimeAsDouble.html

#  [Time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html).unscaledTimeAsDouble
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
unscaledTimeAsDouble; 
### Description
The double precision timeScale-independent time for this frame (Read Only). This is the time in seconds since the start of the game.
Double precision version of [unscaledTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-unscaledTime.html). This offers more precision than a float or single value, particularly over extended periods of real-world time. In almost all cases, use the `unscaledTimeAsDouble` equivalent over [unscaledTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-unscaledTime.html).  
  
When called from inside MonoBehaviour's [FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.FixedUpdate.html), it returns the unscaled fixed time.  
  
Returns the same value if called multiple times in a single frame. Unlike [timeAsDouble](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeAsDouble.html) this value is not affected by [timeScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html).
* * *

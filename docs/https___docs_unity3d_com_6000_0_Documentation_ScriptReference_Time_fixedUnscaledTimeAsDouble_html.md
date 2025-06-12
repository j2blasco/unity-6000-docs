* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedUnscaledTimeAsDouble.html

#  [Time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html).fixedUnscaledTimeAsDouble
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
fixedUnscaledTimeAsDouble; 
### Description
The double precision timeScale-independent time at the beginning of the last [FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.FixedUpdate.html) (Read Only). This is the time in seconds since the start of the game.
Returns the same value if called multiple times in a single frame. Unlike [fixedTimeAsDouble](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedTimeAsDouble.html) this value is not affected by [timeScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html). Double precision version of [fixedUnscaledTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedUnscaledTime.html). This offers more precision than a float or single value, particularly over extended periods of real-world time. In almost all cases, you should use the [fixedUnscaledTimeAsDouble](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedUnscaledTimeAsDouble.html) equivalent over [fixedUnscaledTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedUnscaledTime.html).
* * *

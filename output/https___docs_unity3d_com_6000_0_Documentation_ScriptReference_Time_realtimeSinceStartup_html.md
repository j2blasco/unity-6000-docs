* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-realtimeSinceStartup.html

#  [Time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html).realtimeSinceStartup
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
realtimeSinceStartup; 
### Description
The real time in seconds since the game started (Read Only).
In most cases, use [Time.realtimeSinceStartupAsDouble](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-realtimeSinceStartupAsDouble.html), which offers more precision, particularly over extended periods of real-world time. Refer to its documentation for information about both properties. Use `Time.realtimeSinceStartup` with other single-precision properties that return float instead of double such as `fixedTime`, `fixedUnscaledTime`, `time`, `timeSinceLevelLoad`, and `unscaledTime`. 
* * *

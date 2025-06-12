* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedTimeAsDouble.html

#  [Time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html).fixedTimeAsDouble
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
fixedTimeAsDouble; 
### Description
The double precision time since the last [FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.FixedUpdate.html) started (Read Only). This is the time in seconds since the start of the game.
Fixed time is updated in regular intervals (equal to [fixedDeltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html)) until the [timeAsDouble](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeAsDouble.html) property is reached. This property is the double precision version of [fixedTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedTime.html). This offers more precision than a float or single value, particularly over extended periods of real-world time. In almost all cases, you should use the [fixedTimeAsDouble](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedTimeAsDouble.html) equivalent over [fixedTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedTime.html).
* * *

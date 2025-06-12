* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-captureFramerate.html

#  [Time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html).captureFramerate
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
captureFramerate; 
### Description
The reciprocal of [Time.captureDeltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-captureDeltaTime.html).
`captureFramerate` is the equivalent of (1.0 / [Time.captureDeltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-captureDeltaTime.html)) rounded to the nearest integer.  
  
Setting `captureFramerate` also sets [Time.captureDeltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-captureDeltaTime.html) to the equivalent inverse.  
  
Note that a value of zero for `captureFramerate` is equivalent to value of zero for `captureDeltaTime`.
* * *

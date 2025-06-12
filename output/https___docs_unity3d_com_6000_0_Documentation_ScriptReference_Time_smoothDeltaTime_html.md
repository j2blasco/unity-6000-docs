* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-smoothDeltaTime.html

#  [Time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html).smoothDeltaTime
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
smoothDeltaTime; 
### Description
A smoothed out Time.deltaTime (Read Only).
This value is equal to [Time.deltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html) when it is constant (i.e. smooth frame rate). When deltaTime varies between frames (e.g. on a frame hitch), this value increases or decreases gradually towards deltaTime over multiple frames.  
  
See [Time and Frame Rate Management](https://docs.unity3d.com/6000.0/Documentation/Manual/managing-time-and-frame-rate.html) in the User Manual for more information about how this property relates to the other Time properties.
* * *

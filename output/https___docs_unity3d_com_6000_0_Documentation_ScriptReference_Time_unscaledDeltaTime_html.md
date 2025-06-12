* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-unscaledDeltaTime.html

#  [Time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html).unscaledDeltaTime
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
unscaledDeltaTime; 
### Description
The timeScale-independent interval in seconds from the last frame to the current one (Read Only).
When called from inside MonoBehaviour's [FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.FixedUpdate.html), it returns the unscaled fixed framerate delta time.  
  
Unlike [deltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html) this value is not affected by [timeScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html).  
  
See [Time and Frame Rate Management](https://docs.unity3d.com/6000.0/Documentation/Manual/managing-time-and-frame-rate.html) in the User Manual for more information about how this property relates to the other Time properties.
* * *

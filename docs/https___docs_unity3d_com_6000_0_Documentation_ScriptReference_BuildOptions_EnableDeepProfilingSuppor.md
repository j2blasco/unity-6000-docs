* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.EnableDeepProfilingSupport.html

#  [BuildOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.html).EnableDeepProfilingSupport
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
Enables Deep Profiling support in the Player.
Deep profiling allows to instrument all C# method calls.  
  
**Note:** Enabling the `EnableDeepProfilingSupport` option might significantly slow down the Player, compared to one built with this option disabled. When enabled, additional checks are inserted at the beginning and end of every C# method. These checks continually test if the Player is currently profiled in Deep Profile mode or not, which adds some overhead to their execution time. If the Player is indeed profiled in Deep Profile mode, the method execution time is recorded, which adds some additional overhead. The overhead will not be fully attributed to the method that has been instrumented like this, but will affect the recorded execution time of the calling method as well.
* * *

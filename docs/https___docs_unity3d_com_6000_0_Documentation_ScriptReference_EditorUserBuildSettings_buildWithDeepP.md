* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings-buildWithDeepProfilingSupport.html

#  [EditorUserBuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings.html).buildWithDeepProfilingSupport
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
buildWithDeepProfilingSupport; 
### Description
Enables Deep Profiling support in the Player.
Allow the Profiler to process all your script code and record every function call, returning detailed profiling data.  
  
**Note:** A Player might run significantly slower if `EnableDeepProfilingSupport` is enabled.  
  
When this option is enabled, additional checks are inserted at the beginning and end of every C# Method. These checks will continually test if the Player is currently profiled in Deep Profile mode or not, which adds some overhead to their execution time. If the Player is indeed profiled in Deep Profile mode, the time to execute the method is going to be recorded, which adds some additional overhead. The overhead will not be fully attributed to the method that has been instrumented like this, but will affect the recorded execution time of the calling method as well. You can also set this property in the Unity Editor using the [Deep Profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles-reference.html#shared-build-settings) setting on the **Build Profiles** window.  
  
Additional resources: [BuildOptions.EnableDeepProfilingSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.EnableDeepProfilingSupport.html).
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector-incrementalTimeSliceNanoseconds.html

#  [GarbageCollector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.html).incrementalTimeSliceNanoseconds
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
incrementalTimeSliceNanoseconds; 
### Description
The target duration of a collection step when performing incremental garbage collection.
When you enable incremental garbage collection, the garbage collector spreads the amount of work required to free unused memory across a number of steps. In any single step, the garbage collector limits itself to the length of time specified by `incrementalTimeSliceNanoseconds`. By spreading out the workload, incremental garbage collection can help your game achieve a smoother frame rate (when garbage-collection hiccups are a problem). Use the [Profiler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) to help identify whether garbage collection has an effect on frame rate smoothness.  
  
The garbage collector might still choose to perform a regular, non-incremental collection cycle if your application runs low on memory or if the incremental steps cannot keep up with the garbage collection workload. Setting too short a time slice can be counterproductive in this regard and because each garbage collection step has a small amount of overhead. The default value of 3 ms (3000000 nanoseconds) is a good starting point and the selected duration should be always be significantly shorter than your target frame rate.  
  
If you turn on Vsync by setting [QualitySettings.vSyncCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-vSyncCount.html) greater than 0 or specify a frame rate with [Application.targetFrameRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-targetFrameRate.html), Unity automatically uses any extra time remaining at the end of each frame for incremental garbage collection, regardless of the value of [incrementalTimeSliceNanoseconds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector-incrementalTimeSliceNanoseconds.html).  
  
**Note** : The garbage collector uses the underlying platform timer, which can have a resolution as low as a whole millisecond. In other words, changing the value by a few nanoseconds might have no effect.  
  
Enable incremental garbage collection in the [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html) for a project. You can check whether incremental garbage collection is enabled with [IsIncremental](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.IsIncremental.html).  
  
You can manually trigger an incremental garbage collection step with [CollectIncremental](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.CollectIncremental.html). 
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector-isIncremental.html

#  [GarbageCollector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.html).isIncremental
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
isIncremental; 
### Description
Reports whether incremental garbage collection is enabled.
`IsIncremental` is true if incremental garbage collection is enabled in the project [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html) and supported on the currently running platform. The value is false otherwise.  
  
Set the target length of an incremental collection step with [incrementalTimeSliceNanoseconds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector-incrementalTimeSliceNanoseconds.html). Manually trigger an incremental garbage collection step with [CollectIncremental](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.CollectIncremental.html).  
  
Additional resources: [PlayerSettings.gcIncremental](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-gcIncremental.html).
* * *

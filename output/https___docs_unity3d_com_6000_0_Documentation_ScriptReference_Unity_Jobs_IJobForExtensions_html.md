* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobForExtensions.html

# IJobForExtensions
class in Unity.Jobs
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Contains extension methods for [IJobFor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobFor.html) job types.
### Static Methods
Method | Description  
---|---  
[EarlyJobInit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobForExtensions.EarlyJobInit.html) | Gathers and caches reflection data for the internal job system's managed bindings.  
[Run](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobForExtensions.Run.html) | Performs the job's Execute method immediately on the main thread.  
[RunByRef](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobForExtensions.RunByRef.html) | Performs the job's Execute method immediately on the main thread by reference.  
[Schedule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobForExtensions.Schedule.html) | Schedules the job to execute on a single worker thread.  
[ScheduleByRef](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobForExtensions.ScheduleByRef.html) | Schedules the job to execute on a single worker thread by reference.  
[ScheduleParallel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobForExtensions.ScheduleParallel.html) | Schedules the job to execute concurrently on a number of worker threads.  
[ScheduleParallelByRef](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobForExtensions.ScheduleParallelByRef.html) | Schedules the job to execute concurrently on a number of worker threads by reference.  
* * *

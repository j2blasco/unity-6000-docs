* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html

# JobHandle
struct in Unity.Jobs
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
Represents a handle to a job, which uniquely identifies a job scheduled in the job system.
### Properties
Property | Description  
---|---  
[IsCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.IsCompleted.html) | Determines if a task is running.  
### Public Methods
Method | Description  
---|---  
[Complete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.Complete.html) | Ensures that a job has completed.  
### Static Methods
Method | Description  
---|---  
[CheckFenceIsDependencyOrDidSyncFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.CheckFenceIsDependencyOrDidSyncFence.html) | CheckFenceIsDependencyOrDidSyncFence.   
[CombineDependencies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.CombineDependencies.html) | Combines multiple dependencies into a single dependency.  
[CompleteAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.CompleteAll.html) | Ensures that all jobs have completed.  
[ScheduleBatchedJobs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.ScheduleBatchedJobs.html) | Makes Schedule methods available to worker threads.   
* * *

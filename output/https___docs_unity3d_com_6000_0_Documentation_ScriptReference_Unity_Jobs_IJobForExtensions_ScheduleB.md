* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobForExtensions.ScheduleByRef.html

#  [IJobForExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobForExtensions.html).ScheduleByRef
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
## Declaration
public static [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) ScheduleByRef(ref T jobData, int arrayLength, [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) dependency); 
### Parameters
Parameter | Description  
---|---  
jobData | The job and data to schedule.  
arrayLength | The number of iterations to execute the for loop over.  
dependency | The [JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) of the job's dependency. You can use dependencies to make sure that a job executes on worker threads after the dependency has completed execution and two jobs that read or write to same data don't run in parallel.  
### Returns
**JobHandle** The [JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) of the scheduled job. You can use the `JobHandle` as a dependency for a later job or to make sure that the job completes on the main thread. 
### Description
Schedules the job to execute on a single worker thread by reference.
Additional resources: [IJobFor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobFor.html).
* * *

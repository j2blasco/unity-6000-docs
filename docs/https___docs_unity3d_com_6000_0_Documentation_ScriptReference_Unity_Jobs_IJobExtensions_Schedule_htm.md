* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobExtensions.Schedule.html

#  [IJobExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobExtensions.html).Schedule
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
public static [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) Schedule(T jobData, [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) dependsOn); 
### Parameters
Parameter | Description  
---|---  
jobData | The job and data to schedule.  
dependsOn | The dependency of the job. Dependencies ensure that a job executes on worker threads after the dependency has completed execution, and that two jobs reading or writing to same data do not run in parallel.  
### Returns
**JobHandle** The handle identifying the scheduled job, which you can use as a dependency for a later job or to ensure completion on the main thread. 
### Description
Schedules the job for execution on a worker thread.
Additional resources: [IJob](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJob.html).
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.IJobParallelForTransformExtensions.Schedule.html

#  [IJobParallelForTransformExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.IJobParallelForTransformExtensions.html).Schedule
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
public static [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) Schedule(T jobData, [Jobs.TransformAccessArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccessArray.html) transforms, [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) dependsOn); 
### Parameters
Parameter | Description  
---|---  
jobData | The job to schedule.  
transforms | The [TransformAccessArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccessArray.html) to run the job on.  
dependsOn | A JobHandle containing any jobs that must finish executing before this job begins. You can combine multiple jobs with [JobHandle.CombineDependencies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.CombineDependencies.html). Use dependencies to ensure that two jobs that read or write to the same data don't run in parallel.  
### Returns
**JobHandle** The handle identifying the scheduled job, which you can use as a dependency for a later job or to ensure completion on the main thread. 
### Description
Schedules an [IJobParallelForTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.IJobParallelForTransform.html) job with read-write access to the transform data.
This method parallelizes access to transforms in different hierarchies. Transforms with a shared root object are always processed on the same thread. All transforms are guaranteed to be valid when this scheduling mode is used. Invalid transform references in the input array are ignored.
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.CombineDependencies.html

#  [JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html).CombineDependencies
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
public static [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) CombineDependencies([Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) job0, [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) job1); 
## Declaration
public static [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) CombineDependencies([Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) job0, [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) job1, [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) job2); 
## Declaration
public static [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) CombineDependencies(NativeArray<JobHandle> jobs); 
## Declaration
public static [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) CombineDependencies(NativeSlice<JobHandle> jobs); 
### Description
Combines multiple dependencies into a single dependency.
All job schedule methods for [IJob](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJob.html) or [IJobParallelFor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobParallelFor.html) job types take a single dependency. Sometimes you might need to express dependencies against multiple running jobs at the same time. Use this method to combine a set of dependencies into a single dependency that can be passed to a job.
```
// Schedule 3 jobs, jobs a and b can run in parallel to each other,
// job c will only run once both jobA and jobB has completed  
  
// Schedule job a
var jobA = new MyJob(...);
var jobAHandle = jobA.Schedule();  
  
// Schedule job b
var jobB = new MyJob(...);
var jobBHandle = jobB.Schedule();  
  
// For job c, combine dependencies of job a and b
// Then use that for scheduling the next job
var jobC = new DependentJob(...);
var dependency = JobHandle.CombineDependencies[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.CombineDependencies.html)(jobAHandle, jobBHandle);
jobC.Schedule(dependency);

```

* * *

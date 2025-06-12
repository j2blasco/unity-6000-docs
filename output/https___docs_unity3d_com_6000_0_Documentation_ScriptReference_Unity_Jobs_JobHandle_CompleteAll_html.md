* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.CompleteAll.html

#  [JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html).CompleteAll
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
public static void CompleteAll(ref [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) job0, ref [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) job1); 
## Declaration
public static void CompleteAll(ref [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) job0, ref [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) job1, ref [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) job2); 
## Declaration
public static void CompleteAll(NativeArray<JobHandle> jobs); 
### Description
Ensures that all jobs have completed.
The job system automatically prioritizes all the given jobs and any of its dependencies to run first in the queue, then attempts to execute all the jobs if they aren't executing on the worker threads yet. It completes as soon as all referenced jobs have completed.
* * *

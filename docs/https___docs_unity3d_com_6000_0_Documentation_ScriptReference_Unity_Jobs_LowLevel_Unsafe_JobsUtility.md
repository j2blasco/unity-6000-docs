* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.LowLevel.Unsafe.JobsUtility.ThreadIndex.html

#  [JobsUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.LowLevel.Unsafe.JobsUtility.html).ThreadIndex
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
ThreadIndex; 
### Description
Gets the index for the current thread when executing a job, otherwise 0. 
When multiple threads are executing jobs, no two threads have the same index. The range of this property is `[0, Unity.Jobs.LowLevel.Unsafe.JobsUtility.ThreadIndexCount)`. The value returned when used from within a job is the same as the value stored in job members decorated with `[Unity.Collections.LowLevel.Unsafe.NativeSetThreadIndexAttribute]`. SA: Unity.Jobs.LowLevel.Unsafe.JobsUtility.ThreadIndexCount
* * *

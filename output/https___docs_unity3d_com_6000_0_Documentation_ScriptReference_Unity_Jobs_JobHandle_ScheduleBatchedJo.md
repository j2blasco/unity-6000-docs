* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.ScheduleBatchedJobs.html

#  [JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html).ScheduleBatchedJobs
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
public static void ScheduleBatchedJobs(); 
### Description
Makes Schedule methods available to worker threads. 
By default, jobs are only put on a local queue when using job Schedule methods. `ScheduleBatchedJobs` makes them available to the worker threads to execute. The job system intentionally delays job execution until you call `ScheduleBatchedJobs` manually because the cost of waking up worker threads can be expensive. It's best practic to delay waking up worker threads until a few jobs have been scheduled. If you're scheduling jobs in a loop, wait to schedule the jobs until the end of the loop. If you do significant amounts of work on the main thread between scheduling jobs, then it can make sense to `ScheduleBatchedJobs` between each job.
* * *

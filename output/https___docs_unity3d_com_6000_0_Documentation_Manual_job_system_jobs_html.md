* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/job-system-jobs.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Code optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-optimization.html)
  * [Write multithreaded code with the job system](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system.html)
  * Jobs overview


[](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system-overview.html)
Job system overview
[](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system-creating-jobs.html)
Create and run a job
# Jobs overview
A job is a small unit of work that does one specific task. A job receives parameters and operates on data, similar to how a method call behaves. Jobs can be self-contained, or they can depend on other jobs to complete before they can run. In Unity, a job refers to any struct that implements [the `IJob` interface.](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJob.html)
Only the main thread can schedule and complete jobs. It can’t access the content of any running jobs, and two jobs can’t access the contents of a job at the same time. To ensure efficient running of jobs, you can make them dependent on each other. Unity’s job system allows you to create complex dependency chains to ensure that your jobs complete in the correct order.
## Job types
  * [IJob](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJob.html): Runs a single task on a job thread.
  * [IJobParallelFor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobParallelFor.html): Runs a task in parallel. Each worker thread that runs in parallel has an exclusive index to access shared data between worker threads safely.
  * [IJobParallelForTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.IJobParallelForTransform.html): Runs a task in parallel. Each worker thread running in parallel has an exclusive Transform from the transform hierarchy to operate on.
  * [IJobFor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobFor.html): The same as `IJobParallelFor`, but allows you to schedule the job so that it doesn’t run in parallel.


## Additional resources
  * [Create a job](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system-creating-jobs.html)
  * [Job dependencies](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system-job-dependencies.html)
  * [Parallel jobs](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system-parallel-for-jobs.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system-overview.html)
Job system overview
[](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system-creating-jobs.html)
Create and run a job

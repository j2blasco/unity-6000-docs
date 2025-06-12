* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobParallelFor.html

# IJobParallelFor
interface in Unity.Jobs
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
Interface that represents a job that performs the same independent operation for each element of a native container or for a fixed number of iterations.
When you schedule an `IJobParallelFor` job, its `Execute(int index)` method is invoked on multiple worker threads in parallel to each other.  
  
`Execute(int index)` is executed once for each index from 0 to the provided length. Each iteration must be independent from other iterations and the safety system enforces this rule for you. The indices have no guaranteed order and are executed on multiple cores in parallel.  
  
Unity automatically splits the work into chunks no less than the provided `batchSize`, and schedules an appropriate number of jobs based on the number of worker threads, the length of the array, and the batch size. Choose the batch size depending on the amount of work performed in the job. A simple job, for example adding a couple of Vector3 to each other should have a batch size of 32 to 128. However if the work performed is very expensive then it's best practice to use a small batch size, for example a batch size of 1. IJobParallelFor uses atomic operations to perform work stealing. Batch sizes can be small but they are not for free.  
  
You can use the returned `JobHandle` to make sure that the job has completed, or you can pass it to other jobs as a dependency to make sure that the jobs are executed one after another on the worker threads.
```
using UnityEngine;
using Unity.Collections;
using Unity.Jobs;  
  
class ApplyVelocityParallelForSample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    struct VelocityJob : IJobParallelFor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobParallelFor.html)
    {
        // Jobs declare all data that will be accessed in the job
        // By declaring it as read only, multiple jobs are allowed to access the data in parallel
        [ReadOnly[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.html)]
        public NativeArray<Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)> velocity;  
  
        // By default containers are assumed to be read & write
        public NativeArray<Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)> position;  
  
        // Delta time must be copied to the job since jobs generally don't have concept of a frame.
        // The main thread waits for the job same frame or next frame, but the job should do work deterministically
        // independent on when the job happens to run on the worker threads.
        public float deltaTime;  
  
        // The code actually running on the job
        public void Execute(int i)
        {
            // Move the positions based on delta time and velocity
            position[i] = position[i] + velocity[i] * deltaTime;
        }
    }  
  
    public void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        var position = new NativeArray<Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)>(500, Allocator.Temp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Temp.html));  
  
        var velocity = new NativeArray<Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)>(500, Allocator.Temp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Temp.html));
        for (var i = 0; i < velocity.Length; i++)
            velocity[i] = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 10, 0);  
  
        // Initialize the job data
        var job = new VelocityJob()
        {
            deltaTime = Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html),
            position = position,
            velocity = velocity
        };  
  
        // Schedule a parallel-for job. First parameter is how many for-each iterations to perform.
        // The second parameter is the batch size,
        // essentially the no-overhead innerloop that just invokes Execute(i) in a loop.
        // When there is a lot of work in each iteration then a value of 1 can be sensible.
        // When there is very little work values of 32 or 64 can make sense.
        JobHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) jobHandle = job.Schedule(position.Length, 64);  
  
        // Ensure the job has completed.
        // It is not recommended to Complete a job immediately,
        // since that reduces the chance of having other jobs run in parallel with this one.
        // You optimally want to schedule a job early in a frame and then wait for it later in the frame.
        jobHandle.Complete();  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(job.position[0]);  
  
        // Native arrays must be disposed manually.
        position.Dispose();
        velocity.Dispose();
    }
}

```

### Public Methods
Method | Description  
---|---  
[Execute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobParallelFor.Execute.html) | Performs work against a specific iteration index.  
* * *

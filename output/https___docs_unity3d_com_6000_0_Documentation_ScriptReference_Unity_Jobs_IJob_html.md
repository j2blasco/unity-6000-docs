* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJob.html

# IJob
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
An interface that allows you to schedule a single job that runs in parallel to other jobs and the main thread.
After a job is scheduled, the job's Execute method is invoked on a worker thread. You can use the returned [JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) to make sure that the job has completed. You can also pass the JobHandle to other jobs as a dependency, which ensures that jobs are executed one after another on the worker threads.  
  
Additional resources: [IJobForExtensions.Schedule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobForExtensions.Schedule.html)
```
using UnityEngine;
using Unity.Collections;
using Unity.Jobs;  
  
class ApplyVelocitySample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    struct VelocityJob : IJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJob.html)
    {
        // Jobs declare all data that will be accessed in the job
        // By declaring it as read only, multiple jobs are allowed to access the data in parallel
        [ReadOnly[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.html)]
        public NativeArray<Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)> velocity;  
  
        // By default containers are assumed to be read & write
        public NativeArray<Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)> position;  
  
        // Delta time must be copied to the job since jobs generally don't have concept of a frame.
        // The main thread waits for the job on the same frame or the next frame, but the job should
        // perform work in a deterministic and independent way when running on worker threads.
        public float deltaTime;  
  
        // The code actually running on the job
        public void Execute()
        {
            // Move the positions based on delta time and velocity
            for (var i = 0; i < position.Length; i++)
                position[i] = position[i] + velocity[i] * deltaTime;
        }
    }  
  
    public void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        var position = new NativeArray<Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)>(500, Allocator.Persistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html));  
  
        var velocity = new NativeArray<Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)>(500, Allocator.Persistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html));
        for (var i = 0; i < velocity.Length; i++)
            velocity[i] = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 10, 0);  
  

        // Initialize the job data
        var job = new VelocityJob()
        {
            deltaTime = Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html),
            position = position,
            velocity = velocity
        };  
  
        // Schedule the job, returns the JobHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) which can be waited upon later on
        JobHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) jobHandle = job.Schedule();  
  
        // Ensure the job has completed
        // It is not recommended to Complete a job immediately,
        // since that gives you no actual parallelism.
        // You optimally want to schedule a job early in a frame and then wait for it later in the frame.
        jobHandle.Complete();  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(job.position[0]);  
  
        // Native arrays must be disposed manually
        position.Dispose();
        velocity.Dispose();
    }
}

```

### Public Methods
Method | Description  
---|---  
[Execute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJob.Execute.html) | Implement this method to perform work on a worker thread.  
* * *

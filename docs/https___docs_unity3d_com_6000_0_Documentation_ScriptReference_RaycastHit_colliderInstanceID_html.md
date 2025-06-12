* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-colliderInstanceID.html

#  [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html).colliderInstanceID
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
colliderInstanceID; 
### Description
Instance ID of the [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) that was hit.
Provides a reference to the collider that was hit in a way that is accessible from jobs. For more information on creating jobs see [Create Jobs](https://docs.unity3d.com/6000.0/Documentation/Manual/JobSystemCreatingJobs.html).
```
using Unity.Collections;
using Unity.Jobs;
using UnityEngine;  
  
public class BatchExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public struct CollisionJob : IJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJob.html)
    {
        public int colliderID;
        public NativeArray<RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html)> results;  
  
        public void Execute()
        {
            // This is where we check what we collided with and do any appropriate actions
            // If you tried accessing RaycastHit.collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-collider.html) you would get an error
            if (colliderID == results[0].colliderInstanceID)
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Detected the a hit with the requested collider");
        }
    }
    void Start()
    {
        // We create the raycast command buffer and an array to store the RaycastHits
        NativeArray<RaycastCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastCommand.html)> commands = new NativeArray<RaycastCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastCommand.html)>(1, Allocator.TempJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.TempJob.html));
        NativeArray<RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html)> results = new NativeArray<RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html)>(1, Allocator.TempJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.TempJob.html));  
  
        var boxCollider = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)().AddComponent<BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html)>();  
  
        // Create a new command for the buffer, pointing at the collider we created
        commands[0] = new RaycastCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastCommand.html)(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * 2, Vector3.down[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-down.html));  
  
        // Schedule the commands in the buffer and store results in the 'results' array
        var batchHandle = RaycastCommand.ScheduleBatch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastCommand.ScheduleBatch.html)(commands, results, 1, 1);  
  
        // This job is for doing something on the other thread when the collider of interest was hit
        var job = new CollisionJob();
        job.colliderID = boxCollider.GetInstanceID();
        job.results = results;  
  
        //Schedule the job to start after batchHandle has finished
        var jobHandle = job.Schedule(batchHandle);
        jobHandle.Complete();  
  
        commands.Dispose();
        results.Dispose();
    }
}

```

* * *

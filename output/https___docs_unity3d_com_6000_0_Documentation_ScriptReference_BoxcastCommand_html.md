* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxcastCommand.html

# BoxcastCommand
struct in UnityEngine
/
Implemented in:[UnityEngine.PhysicsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.PhysicsModule.html)
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
Use this struct to set up a box cast command to be performed asynchronously during a job.
When you use this struct to schedule a batch of box casts, the box casts will are performed asynchronously and in parallel. The results of each box cast is written to the results buffer. Since the results are written asynchronously, you cannot accesss the results buffer until the job is completed.  
  
The results for a command at index N in the command buffer are stored at index N * maxHits in the results buffer.  
  
Boxcast command also allows you to control whether or not Trigger colliders and back-face triangles generate a hit. Use [QueryParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters.html) to control hit flags.  
  
Note: Only BatchQuery.ExecuteBoxcastJob is logged into the profiler. Query count information is not logged.  
  
Additional resources: Physics.Boxcast.
```
using Unity.Collections;
using Unity.Jobs;
using UnityEngine;  
  
public class BoxcastCommandExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Perform a single boxcast using BoxcastCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxcastCommand.html) and wait for it to complete
        // Set up the command and result buffers
        var results = new NativeArray<RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html)>(2, Allocator.TempJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.TempJob.html));
        var commands = new NativeArray<BoxcastCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxcastCommand.html)>(1, Allocator.TempJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.TempJob.html));  
  
        // Set the data of the first command
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) halfExtents = Vector3.one[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-one.html) * 0.5f;
        Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) orientation = Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html);
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction = Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html);  
  
        commands[0] = new BoxcastCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxcastCommand.html)(center, halfExtents, orientation, direction, QueryParameters.Default[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters.Default.html));  
  
        // Schedule the batch of boxcasts
        var handle = BoxcastCommand.ScheduleBatch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxcastCommand.ScheduleBatch.html)(commands, results, 1, 2, default(JobHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html)));  
  
        // Wait for the batch processing job to complete
        handle.Complete();  
  
        // If batchedHit.collider is not null there was a hit
        foreach (var hit in results)
        {
            if (hit.collider != null)
            {
                // Do something with results
            }
        }  
  
        // Dispose the buffers
        results.Dispose();
        commands.Dispose();
    }
}

```

### Properties
Property | Description  
---|---  
[center](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxcastCommand-center.html) | The center of the box.  
[direction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxcastCommand-direction.html) | The direction in which to sweep the box.  
[distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxcastCommand-distance.html) | The maximum distance of the sweep.  
[halfExtents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxcastCommand-halfExtents.html) | The half size of the box in each dimension.  
[orientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxcastCommand-orientation.html) | The rotation of the box.  
[physicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxcastCommand-physicsScene.html) | The physics scene this command is run in.  
[queryParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxcastCommand-queryParameters.html) | Structure for specifying additional parameters for a batch query such as layer mask, hit triggers and hit backfaces.  
### Constructors
Constructor | Description  
---|---  
[BoxcastCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxcastCommand-ctor.html) | Creates a BoxcastCommand.  
### Static Methods
Method | Description  
---|---  
[ScheduleBatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxcastCommand.ScheduleBatch.html) | Schedules a batch of boxcasts to be performed in a job.  
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpherecastCommand.html

# SpherecastCommand
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
Use this struct to set up a sphere cast command that is performed asynchronously during a job.
When you use this struct to schedule a batch of sphere casts, the sphere casts are performed asynchronously and in parallel. The results of each sphere casts are written to the results buffer. Since the results are written asynchronously, you cannot access the results buffer until the job is completed.  
  
The results for a command at index N in the command buffer are stored at index N * maxHits in the results buffer.  
  
Spherecast command also allows you to control whether or not Trigger colliders and back-face triangles generate a hit. Use [QueryParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters.html) to control hit flags.  
  
Note: Only BatchQuery.ExecuteSpherecastJob is logged into the profiler. Query count information is not logged.  
  
Additional resources: Physics.Spherecast.
```
using Unity.Collections;
using Unity.Jobs;
using UnityEngine;  
  
public class SpherecastExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Perform a single sphere cast using SpherecastCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpherecastCommand.html) and wait for it to complete
        // Set up the command and result buffers
        var results = new NativeArray<RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html)>(2, Allocator.TempJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.TempJob.html));
        var commands = new NativeArray<SpherecastCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpherecastCommand.html)>(1, Allocator.TempJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.TempJob.html));  
  
        // Set the data of the first command
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) origin = Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html) * -10;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction = Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html);
        float radius = 0.5f;  
  
        commands[0] = new SpherecastCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpherecastCommand.html)(origin, radius, direction, QueryParameters.Default[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters.Default.html));  
  
        // Schedule the batch of sphere casts
        var handle = SpherecastCommand.ScheduleBatch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpherecastCommand.ScheduleBatch.html)(commands, results, 1, 2, default(JobHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html)));  
  
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
[direction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpherecastCommand-direction.html) | The direction of the sphere cast.  
[distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpherecastCommand-distance.html) | The maximum distance the sphere should check for collisions.  
[origin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpherecastCommand-origin.html) | The starting point of the sphere cast in world coordinates.  
[physicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpherecastCommand-physicsScene.html) | The physics scene this command is run in.  
[queryParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpherecastCommand-queryParameters.html) | Structure for specifying additional parameters for a batch query such as layer mask, hit triggers and hit backfaces.  
[radius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpherecastCommand-radius.html) | The radius of the casting sphere.  
### Constructors
Constructor | Description  
---|---  
[SpherecastCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpherecastCommand-ctor.html) | Creates a SpherecastCommand.  
### Static Methods
Method | Description  
---|---  
[ScheduleBatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpherecastCommand.ScheduleBatch.html) | Schedules a batch of sphere casts to perform in a job.  
* * *

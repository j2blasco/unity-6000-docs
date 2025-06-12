* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastCommand.html

# RaycastCommand
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
Struct used to set up a raycast command to be performed asynchronously during a job.
When you use this struct to schedule a batch of raycasts, they will be performed asynchronously and in parallel to each other. The results of the raycasts are written to the results buffer. Since the results are written asynchronously the results buffer cannot be accessed until the job has been completed.  
  
The results for a command at index N in the command buffer are stored at index N * maxHits in the results buffer.  
  
If maxHits is larger than the actual number of results for the command the result buffer will contain some invalid results which did not hit anything. The first invalid result is identified by the collider being null. The second and later invalid results are not written to by the raycast command so their colliders are not guaranteed to be null. When iterating over the results the loop should stop when the first invalid result is found.  
  
Raycast command also controls whether or not Trigger colliders and back-face triangles generate a hit. If hitMultipleFaces is set to true, Raycast command returns multiple hits per Mesh. You should adjust maxHits and result array size accordingly to store all hits. For solid objects (Sphere, Capsule, Box, Convex), this returns a maximum of one result. Use [QueryParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters.html) to control hit flags.  
  
Note: Only BatchQuery.ExecuteRaycastJob is logged into the profiler. Query count information is not logged.  
  
Additional resources: [Physics.Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html), [Physics.RaycastAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.RaycastAll.html).
```
using Unity.Collections;
using Unity.Jobs;
using UnityEngine;  
  
public class RaycastExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private void Start()
    {
        // Perform a single raycast using RaycastCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastCommand.html) and wait for it to complete
        // Setup the command and result buffers
        var results = new NativeArray<RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html)>(2, Allocator.TempJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.TempJob.html));  
  
        var commands = new NativeArray<RaycastCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastCommand.html)>(1, Allocator.TempJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.TempJob.html));  
  
        // Set the data of the first command
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) origin = Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html) * -10;  
  
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction = Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html);  
  
        commands[0] = new RaycastCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastCommand.html)(origin, direction, QueryParameters.Default[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters.Default.html));  
  
        // Schedule the batch of raycasts.
        JobHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) handle = RaycastCommand.ScheduleBatch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastCommand.ScheduleBatch.html)(commands, results, 1, 2, default(JobHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html)));  
  
        // Wait for the batch processing job to complete
        handle.Complete();  
  
        // Copy the result. If batchedHit.collider is null there was no hit
        foreach (var hit in results)
        {
            if (hit.collider != null)
            {
                // If hit.collider is not null means there was a hit
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
[direction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastCommand-direction.html) | The direction of the ray.  
[distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastCommand-distance.html) | The maximum distance the ray should check for collisions.  
[from](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastCommand-from.html) | The starting point of the ray in world coordinates.  
[physicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastCommand-physicsScene.html) | The physics scene this command is run in.  
[queryParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastCommand-queryParameters.html) | Structure for specifying additional parameters for a batch query such as layer mask, hit multiple mesh faces, hit triggers and hit backfaces.  
### Constructors
Constructor | Description  
---|---  
[RaycastCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastCommand-ctor.html) | Create a RaycastCommand.  
### Static Methods
Method | Description  
---|---  
[ScheduleBatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastCommand.ScheduleBatch.html) | Schedule a batch of raycasts to perform in a job.  
* * *

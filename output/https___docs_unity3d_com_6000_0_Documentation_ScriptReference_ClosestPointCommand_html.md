* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClosestPointCommand.html

# ClosestPointCommand
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
Struct used to set up a closest point command to be performed asynchronously during a job.  
  
When you use this struct to schedule a batch of closest commands, they are performed asynchronously and in parallel to each other. The results of the closest points are written to the results buffer. Because the results are written asynchronously, the results buffer cannot be accessed until the job has been completed.  
  
The result for a command at index N in the command buffer is stored at index N in the results buffer.
Additional resources: [Physics.ClosestPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.ClosestPoint.html).
```
using Unity.Collections;
using Unity.Jobs;
using UnityEngine;  
  
public class ClosestPoint : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private void Start()
    {
        var collider = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)().AddComponent<BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html)>();
        // Perform a single closest point using ClosestPointCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClosestPointCommand.html) and wait for it to complete
        // Set up the command and result buffers
        var results = new NativeArray<Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)>(1, Allocator.TempJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.TempJob.html));  
  
        var commands = new NativeArray<ClosestPointCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClosestPointCommand.html)>(1, Allocator.TempJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.TempJob.html));  
  
        commands[0] = new ClosestPointCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClosestPointCommand.html)(Vector3.one[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-one.html) * 5, collider.GetInstanceID(), Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html), collider.transform.lossyScale);  
  
        // Schedule the batch of closest points
        JobHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) handle = ClosestPointCommand.ScheduleBatch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClosestPointCommand.ScheduleBatch.html)(commands, results, 1, default(JobHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html)));  
  
        // Wait for the batch processing job to complete
        handle.Complete();  
  
        // Copy the result. If the point is inside of the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html), it is returned as a result
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) closestPoint = results[0];  
  
        // Dispose of the buffers
        results.Dispose();
        commands.Dispose();
    }
}

```

### Properties
Property | Description  
---|---  
[colliderInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClosestPointCommand-colliderInstanceID.html) | The ID of the Collider that you find the closest point on.  
[point](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClosestPointCommand-point.html) | Location you want to find the closest point to.  
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClosestPointCommand-position.html) | The position of the Collider.  
[rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClosestPointCommand-rotation.html) | The rotation of the Collider.  
[scale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClosestPointCommand-scale.html) | The global scale of the Collider.  
### Constructors
Constructor | Description  
---|---  
[ClosestPointCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClosestPointCommand-ctor.html) | Create a ClosestPointCommand using Instance ID of the Collider.  
### Static Methods
Method | Description  
---|---  
[ScheduleBatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClosestPointCommand.ScheduleBatch.html) | Schedule a batch of closest points which are performed in a job.  
* * *

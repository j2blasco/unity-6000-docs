* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapSphereCommand.html

# OverlapSphereCommand
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
Struct used to setup an overlap sphere command to be performed asynchronously during a job.
When you use this struct to schedule a batch of overlap sphere commands, the commands are performed asynchronously. The results of the overlap sphere are written to the results buffer. Because the results are written asynchronously, the results buffer can't be accessed until the job is complete.  
  
The results for a command at index N in the command buffer are stored at index N * maxHits in the results buffer.  
  
If maxHits is larger than the actual number of results for the command the result buffer will contain some invalid results which did not hit anything. The first invalid result is identified by the collider instance ID being 0. The second and later invalid results are not written to the overlap sphere command so their collider instance IDs are not guaranteed to be 0. When iterating over the results the loop should stop when the first invalid result is found.  
  
Overlap sphere command also controls whether or not Trigger colliders generate a hit. You should adjust maxHits and result array size accordingly to store all hits. Use [QueryParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters.html) to control hit flags. [QueryParameters.hitBackfaces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters-hitBackfaces.html) and [QueryParameters.hitMultipleFaces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters-hitMultipleFaces.html) flags are not supported and won’t have any impact on overlap results.  
  
Note: Only BatchQuery.ExecuteOverlapSphere is logged into the profiler. Query count information is not logged.  
  
Additional resources: [Physics.OverlapSphere](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.OverlapSphere.html), [ColliderHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderHit.html).
```
using Unity.Collections;
using UnityEngine;  
  
public class SphereOverlap : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //Print names of GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) inside the sphere
    void BatchOverlapSphere()
    {
        var commands = new NativeArray<OverlapSphereCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapSphereCommand.html)>(1, Allocator.TempJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.TempJob.html));
        var results = new NativeArray<ColliderHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderHit.html)>(3, Allocator.TempJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.TempJob.html));  
  
        commands[0] = new OverlapSphereCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapSphereCommand.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), 10f, QueryParameters.Default[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters.Default.html));  
  
        OverlapSphereCommand.ScheduleBatch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapSphereCommand.ScheduleBatch.html)(commands, results, 1, 3).Complete();  
  
        foreach (var hit in results)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(hit.collider.name);  
  
        commands.Dispose();
        results.Dispose();
    }
}

```

### Properties
Property | Description  
---|---  
[physicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapSphereCommand-physicsScene.html) | The physics scene the command is run in.  
[point](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapSphereCommand-point.html) | The center of the sphere.  
[queryParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapSphereCommand-queryParameters.html) | Structure for specifying additional parameters for a batch query such as layer mask or hit triggers.  
[radius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapSphereCommand-radius.html) | The radius of the sphere.  
### Constructors
Constructor | Description  
---|---  
[OverlapSphereCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapSphereCommand-ctor.html) | Create an OverlapSphereCommand.  
### Static Methods
Method | Description  
---|---  
[ScheduleBatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapSphereCommand.ScheduleBatch.html) | Schedule a batch of overlap sphere commands to perform in a job.  
* * *

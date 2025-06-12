* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapBoxCommand.html

# OverlapBoxCommand
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
Struct used to set up an overlap box command to be performed asynchronously during a job.
When you use this struct to schedule a batch of overlap box commands, the commands are performed asynchronously. The results of the overlap box are written to the results buffer. Because the results are written asynchronously, the results buffer can't be accessed until the job is complete.  
  
The results for a command at index N in the command buffer are stored at index N * maxHits in the results buffer.  
  
If maxHits is larger than the actual number of results for the command the result buffer will contain some invalid results which did not hit anything. The first invalid result is identified by the collider instance ID being 0. The second and later invalid results are not written to the overlap box command so their collider instance IDs are not guaranteed to be 0. When iterating over the results the loop should stop when the first invalid result is found.  
  
Overlap box command also controls whether or not Trigger colliders generate a hit. You should adjust maxHits and result array size accordingly to store all hits. Use [QueryParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters.html) to control hit flags. [QueryParameters.hitBackfaces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters-hitBackfaces.html) and [QueryParameters.hitMultipleFaces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters-hitMultipleFaces.html) flags are not supported and won’t have any impact on overlap results.  
  
Note: Only BatchQuery.ExecuteOverlapBoxJob is logged into the profiler. Query count information is not logged.  
  
Additional resources: [Physics.OverlapBox](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.OverlapBox.html), [ColliderHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderHit.html).
```
using Unity.Collections;
using UnityEngine;  
  
public class BoxOverlap : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //Print names of GameObjects inside the box
    void BatchOverlapBox()
    {
        var commands = new NativeArray<OverlapBoxCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapBoxCommand.html)>(1, Allocator.TempJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.TempJob.html));
        var results = new NativeArray<ColliderHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderHit.html)>(3, Allocator.TempJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.TempJob.html));  
  
        commands[0] = new OverlapBoxCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapBoxCommand.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), Vector3.one[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-one.html), Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html), QueryParameters.Default[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryParameters.Default.html));  
  
        OverlapBoxCommand.ScheduleBatch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapBoxCommand.ScheduleBatch.html)(commands, results, 1, 3).Complete();  
  
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
[center](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapBoxCommand-center.html) | The center of the box.  
[halfExtents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapBoxCommand-halfExtents.html) | Half of the size of the box in each dimension.  
[orientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapBoxCommand-orientation.html) | The orientation of the box.  
[physicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapBoxCommand-physicsScene.html) | The physics scene this command is run in.  
[queryParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapBoxCommand-queryParameters.html) | Structure for specifying additional parameters for a batch query such as layer mask or hit triggers.  
### Constructors
Constructor | Description  
---|---  
[OverlapBoxCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapBoxCommand-ctor.html) | Create an OverlapBoxCommand.  
### Static Methods
Method | Description  
---|---  
[ScheduleBatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OverlapBoxCommand.ScheduleBatch.html) | Schedule a batch of overlap box commands to perform in a job.  
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerFlowEventType.ParallelNext.html

#  [ProfilerFlowEventType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerFlowEventType.html).ParallelNext
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
Use for the parallel flow continuation point.
All parallel flow instances are equivalent and connected to the same [Begin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerFlowEventType.Begin.html) or [Next](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerFlowEventType.Next.html) events that happened previously. An example of a flow start point is job scheduling. For instance, [IJobParallelForExtensions.Schedule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobParallelForExtensions.Schedule.html) generates an implicit [Begin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerFlowEventType.Begin.html) Profiler flow event and [IJobParallelFor.Execute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobParallelFor.Execute.html) generates an implicit [ParallelNext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerFlowEventType.ParallelNext.html) event.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Threading;
using Unity.Profiling;
using Unity.Profiling.LowLevel;
using Unity.Profiling.LowLevel.Unsafe;  
  
public class Example
{
    static readonly ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html) k_ScheduleParallelTasksMarker = new ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html)("Schedule Parallel Tasks");
    static readonly ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html) k_ParallelTaskMarker = new ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html)("Parallel Task[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html)");  
  
    static void EmitFlowEventAndChainThread(uint flowId)
    {
        // Mark the next k_ParallelTaskMarker as a beginning of the flow
        ProfilerUnsafeUtility.FlowEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.FlowEvent.html)(flowId, ProfilerFlowEventType.ParallelNext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerFlowEventType.ParallelNext.html));
        using (k_ParallelTaskMarker.Auto())
        {
            // Do work
        }
    }  
  
    static void ScheduleParallelTask()
    {
        using (k_ScheduleParallelTasksMarker.Auto())
        {
            var flowId = ProfilerUnsafeUtility.CreateFlow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CreateFlow.html)(ProfilerUnsafeUtility.CategoryScripts[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryScripts.html));
            // Mark the parent k_ScheduleParallelTasksMarker as a beginning of the flow
            ProfilerUnsafeUtility.FlowEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.FlowEvent.html)(flowId, ProfilerFlowEventType.Begin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerFlowEventType.Begin.html));
            var thread = new Thread(() => EmitFlowEventAndChainThread(flowId));
            thread.Start();
        }
    }
}

```

Additional resources: [ProfilerUnsafeUtility.FlowEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.FlowEvent.html).
* * *

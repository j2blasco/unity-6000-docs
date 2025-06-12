* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetTotalReservedMemoryLong.html

#  [Profiler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html).GetTotalReservedMemoryLong
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
## Declaration
public static long GetTotalReservedMemoryLong(); 
### Returns
**long** Memory reserved by Unity in bytes. This returns 0 if the Profiler is not available. 
### Description
The total memory Unity has reserved.
This function returns the total memory Unity has reserved for current and future allocations. If the reserved memory is fully used, Unity will allocate more memory from the system as required.
```
using UnityEngine;
using UnityEngine.Profiling;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Total Reserved memory by Unity: " + Profiler.GetTotalReservedMemoryLong[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetTotalReservedMemoryLong.html)() + "Bytes");
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("- Allocated memory by Unity: " + Profiler.GetTotalAllocatedMemoryLong[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetTotalAllocatedMemoryLong.html)() + "Bytes");
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("- Reserved but not allocated: " + Profiler.GetTotalUnusedReservedMemoryLong[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetTotalUnusedReservedMemoryLong.html)() + "Bytes");
    }
}

```

* * *

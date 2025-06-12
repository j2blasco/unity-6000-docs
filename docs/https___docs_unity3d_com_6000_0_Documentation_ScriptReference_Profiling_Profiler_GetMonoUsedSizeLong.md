* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetMonoUsedSizeLong.html

#  [Profiler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html).GetMonoUsedSizeLong
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
public static long GetMonoUsedSizeLong(); 
### Returns
**long** Returns a long integer value of the memory in use. 
### Description
Gets the allocated managed memory for live objects and non-collected objects.
This function returns the amount of allocated managed-memory for all objects, both live and non-collected. Always call GC.Collect before calling this function, because non-referenced objects still take up space until the garbage collector (GC) collects them. This returns an ever-increasing value until GC.Collect is called.  
  
The size of [Profiler.GetMonoHeapSizeLong](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetMonoHeapSizeLong.html) might decrease after a subsequent GC.Collect is called, if the first GC.Collect call collected all remaining objects in a heap section. Allocating new memory might also implicitly re-trigger GC.Collect and if it finds more objects that are ready to be collected since the first call, it might lower the value that Profiler.GetMonoUsedSizeLong returns even further. Also, Unity might allocate managed memory on threads, or threaded code might get rid of pointers to managed allocations, so while it might look like no code should have changed the amount of managed allocations between two points of measurements, that is not necessarily the case.
```
using UnityEngine;
using System.Collections;
using UnityEngine.Profiling;  
  
class GetMonoExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        System.GC.Collect();
        System.GC.WaitForPendingFinalizers();
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Mono used size" + Profiler.GetMonoUsedSizeLong[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetMonoUsedSizeLong.html)() + "Bytes");
    }
}

```

* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.GCMode.html

#  [GarbageCollector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.html).GCMode
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
[Scripting.GarbageCollector.Mode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html) GCMode; 
### Description
Set and get global garbage collector operation mode.
Setting the global operation mode changes the garbage collector behaviour for the entire application.  
  
Not supported on the WebGL platform and in the Editor.  
  
It is recommended that you only change the garbage collector operation mode on the application level and do not change it in third party libraries.  
  
Subscribe to the [GarbageCollector.GCModeChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.GCModeChanged.html) event to get notified when the garbage collector mode is changed.  
  
**Disabling the Garbage Collector** Disabling the garbage collector by assigning [GarbageCollector.Mode.Disabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.Disabled.html) completely disables the garbage collector. This means that the garbage collector thread will never stop your application to perform a collection. Also, calling System.GC.Collect() will have no effect and will not start a collection. Disabling the garbage collector has to be done with great care, as continuous allocations after disabling the garbage collector will result in a continuous increase in memory usage.  
  
It is recommended that you only disable the garbage collector for long lived allocations. For example, in a game you should allocate all required memory for a level and then disable the garbage collector to avoid overhead during the level. After the level is completed and all memory is released, the garbage collector can then be enabled again and System.GC.Collect() can be called to reclaim memory before loading the next level.  
  
**Controlling the Garbage Collector manually** You can set GCMode to [GarbageCollector.Mode.Manual](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.Manual.html). This disables automatic invocations of the garbage collector, but still allows you to manually perform garbage collection. Manual collection gives you control over when collections happen, so you can fine-tune the smoothness of your content or your memory usage. Call either System.GC.Collect() for a full, blocking collection, or [GarbageCollector.CollectIncremental](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.CollectIncremental.html) to perform incremental garbage collection.  
  
Additional resources: [GarbageCollector.Mode.Enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.Enabled.html), [GarbageCollector.Mode.Disabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.Disabled.html), [GarbageCollector.Mode.Manual](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.Manual.html).
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;
using UnityEngine.Scripting;  
  
public class GarbageCollectorExample
{
    static void ListenForGCModeChange()
    {
        // Listen on garbage collector mode changes.
        GarbageCollector.GCModeChanged[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.GCModeChanged.html) += (GarbageCollector.Mode mode) =>
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("GCModeChanged: " + mode);
        };
    }  
  
    static void LogMode()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("GCMode: " + GarbageCollector.GCMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.GCMode.html));
    }  
  
    static void EnableGC()
    {
        GarbageCollector.GCMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.GCMode.html) = GarbageCollector.Mode.Enabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.Enabled.html);
        // Trigger a collection to free memory.
        GC.Collect();
    }  
  
    static void DisableGC()
    {
        GarbageCollector.GCMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.GCMode.html) = GarbageCollector.Mode.Disabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.Disabled.html);
    }
}

```

Using the GCMode API.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;
using UnityEngine.Profiling;
using UnityEngine.Scripting;  
  
public class GCManualControl : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Perform an incremental collection every time we allocate more than 8 MB
    const long kCollectAfterAllocating = 8 * 1024 * 1024;  
  
    // Perform an instant, full GC if we have more than 128 MB of managed heap.
    const long kHighWater = 128 * 1024 * 1024;  
  
    long lastFrameMemory = 0;
    long nextCollectAt = 0;  
  
    void Start()
    {
        // Set GC to manual collections only.
        GarbageCollector.GCMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.GCMode.html) = GarbageCollector.Mode.Manual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.Manual.html);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        long mem = Profiler.GetMonoUsedSizeLong[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetMonoUsedSizeLong.html)();
        if (mem < lastFrameMemory)
        {
            // GC happened.
            nextCollectAt = mem + kCollectAfterAllocating;
        }
        if (mem > kHighWater)
        {
            // Trigger immediate GC
            System.GC.Collect(0);
        }
        else if (mem >= nextCollectAt)
        {
            // Trigger incremental GC
            UnityEngine.Scripting.GarbageCollector.CollectIncremental();
            lastFrameMemory = mem + kCollectAfterAllocating;
        }
        lastFrameMemory = mem;
    }
}

```

Manual GC control using GarbageCollector.Mode.Manual.
* * *

* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.CurrentValue.html

#  [ProfilerRecorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html).CurrentValue
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
CurrentValue; 
### Description
Gets current value of the Profiler metric.
Use to obtain immediate profiler counter value or marker timing. If the current value is the only data you are interested in, there is no need to start ProfilerRecorder or allocate sample storage. In this case use 0 as a capacity parameter when creating ProfilerRecorder.
```
using UnityEngine;
using Unity.Profiling;  
  
public class Example
{
    public static void LogCurrentSystemMemoryUsage()
    {
        var systemMemoryRecorder = new ProfilerRecorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html)(ProfilerCategory.Memory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Memory.html), "System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html) Used Memory", 0);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html) Used Memory (bytes): " + systemMemoryRecorder.CurrentValue);
    }
}

```

Use _CurrentValue_ to retrieve timings of a code tagged with [ProfilerMarker.Auto](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.Auto.html).
```
using UnityEngine;
using Unity.Profiling;  
  
public class Example
{
    static readonly ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html) k_MyMarker = new ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html)(ProfilerCategory.Scripts[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Scripts.html), "MyMarker");  
  
    public static void TimeSynchronousMethodWithMarkers()
    {
        using (var recorder = ProfilerRecorder.StartNew[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.StartNew.html)(ProfilerCategory.Scripts[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Scripts.html), "MyMarker"))
        {
            using (k_MyMarker.Auto())
            {
                // ...
            }  
  
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("MyMarker total time, ns:  " + recorder.CurrentValue);
        }
    }
}

```

**Note:**   
[Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.Stop.html) resets _CurrentValue_ to zero.
* * *

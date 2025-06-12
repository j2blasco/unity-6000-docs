* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html

# ProfilerRecorder
struct in Unity.Profiling
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Records the Profiler metric data that a Profiler marker or counter produces.
Use ProfilerRecorder to access performance metrics that the Profiler exposes. You can use it to read Profiler counter data such as memory or render statistics, and Profiler marker timing data in a uniform way.  
  
You can use this API in Editor and Player builds, including Release Players. Use [ProfilerRecorderHandle.GetAvailable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerRecorderHandle.GetAvailable.html) to get the full list of supported metrics. For a list of built-in Profiler markers available, see the User Manual documentation on [Common Profiler markers](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html).  
  
The following example demonstrates how you can use ProfilerRecorder to get memory and timing statistics.
```
using System.Collections.Generic;
using System.Text;
using Unity.Profiling;
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    string statsText;
    ProfilerRecorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html) systemMemoryRecorder;
    ProfilerRecorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html) gcMemoryRecorder;
    ProfilerRecorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html) mainThreadTimeRecorder;  
  
    static double GetRecorderFrameAverage(ProfilerRecorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html) recorder)
    {
        var samplesCount = recorder.Capacity;
        if (samplesCount == 0)
            return 0;  
  
        double r = 0;
        unsafe
        {
            var samples = stackalloc ProfilerRecorderSample[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorderSample.html)[samplesCount];
            recorder.CopyTo(samples, samplesCount);
            for (var i = 0; i < samplesCount; ++i)
                r += samples[i].Value;
            r /= samplesCount;
        }  
  
        return r;
    }  
  
    void OnEnable()
    {
        systemMemoryRecorder = ProfilerRecorder.StartNew[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.StartNew.html)(ProfilerCategory.Memory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Memory.html), "System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html) Used Memory");
        gcMemoryRecorder = ProfilerRecorder.StartNew[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.StartNew.html)(ProfilerCategory.Memory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Memory.html), "GC Reserved Memory");
        mainThreadTimeRecorder = ProfilerRecorder.StartNew[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.StartNew.html)(ProfilerCategory.Internal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Internal.html), "Main Thread", 15);
    }  
  
    void OnDisable()
    {
        systemMemoryRecorder.Dispose();
        gcMemoryRecorder.Dispose();
        mainThreadTimeRecorder.Dispose();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        var sb = new StringBuilder(500);
        sb.AppendLine($"Frame Time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html): {GetRecorderFrameAverage(mainThreadTimeRecorder) * (1e-6f):F1} ms");
        sb.AppendLine($"GC Memory: {gcMemoryRecorder.LastValue / (1024 * 1024)} MB");
        sb.AppendLine($"System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html) Memory: {systemMemoryRecorder.LastValue / (1024 * 1024)} MB");
        statsText = sb.ToString();
    }  
  
    void OnGUI()
    {
        GUI.TextArea[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.TextArea.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 30, 250, 50), statsText);
    }
}

```

**Note:**   
ProfilerRecorder allocates unmanaged resources and implements IDisposable interface. Use [Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.Dispose.html) to free resources when you no longer need to record statistics.  
  
ProfilerRecorder gives you access to Unity metrics in two modes: immediate access to a value of a counter, and the counter value when the frame ends. Additional resources: [CurrentValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.CurrentValue.html), [LastValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.LastValue.html), [GetSample](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.GetSample.html), [ProfilerRecorderHandle.GetAvailable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerRecorderHandle.GetAvailable.html).
### Properties
Property | Description  
---|---  
[Capacity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.Capacity.html) | Maximum amount of samples ProfilerRecorder can capture.  
[Count](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.Count.html) | Collected samples count.  
[CurrentValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.CurrentValue.html) | Gets current value of the Profiler metric.  
[CurrentValueAsDouble](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.CurrentValueAsDouble.html) | Gets current value of the Profiler metric as double value.  
[DataType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.DataType.html) | Value data type of the Profiler metric.  
[IsRunning](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.IsRunning.html) | Indicates if ProfilerRecorder is attached to the Profiler metric.  
[LastValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.LastValue.html) | Gets the last value collected by the ProfilerRecorder.  
[LastValueAsDouble](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.LastValueAsDouble.html) | Gets the last value collected by the ProfilerRecorder as double.  
[UnitType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.UnitType.html) | Unit type.  
[Valid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.Valid.html) | Indicates whether ProfilerRecorder is associated with a valid Profiler marker or counter.  
[WrappedAround](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.WrappedAround.html) | Indicates if ProfilerRecorder capacity has been exceeded.  
### Constructors
Constructor | Description  
---|---  
[ProfilerRecorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder-ctor.html) | Constructs ProfilerRecorder instance with a Profiler metric name and category.  
### Public Methods
Method | Description  
---|---  
[CopyTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.CopyTo.html) | Copies collected samples to the destination array.  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.Dispose.html) | Releases unmanaged instance of the ProfilerRecorder.  
[GetSample](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.GetSample.html) | Gets sample data.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.Reset.html) | Stops data collection and clears collected samples.  
[Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.Start.html) | Start data collection.  
[Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.Stop.html) | Stops data collection.  
[ToArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.ToArray.html) | Use to convert collected samples to an array.  
### Static Methods
Method | Description  
---|---  
[StartNew](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.StartNew.html) | Initialize a new instance of ProfilerRecorder and start data collection.  
* * *

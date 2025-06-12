* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-record-timing-data.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Profile rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/profile-rendering.html)
  * [Frame Timing Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-landing.html)
  * Record frame timing data


[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-get-timing-data.html)
Get frame timing data
[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-troubleshoot.html)
Troubleshooting the Frame Time Manager
# Record frame timing data
You can read FrameTimingManager values using the ProfilerRecorder API instead of the FrameTimingManager C# API. The benefit of this is that when you use the ProfilerRecorder API, the FrameTimingManager only records values when you attach a recorder to a specific counter. This behavior enables you to control which counters collect data and so, reduce the impact that the FrameTimingManager has on performance. 
The following example shows how to track only the CPU Main Thread Frame Time variable with the ProfilerRecordAPI:
```

using Unity.Profiling;

using UnityEngine;

public class ExampleScript : MonoBehaviour

{

    string statsText;

    ProfilerRecorder mainThreadTimeRecorder;

    void OnEnable()

    {
        mainThreadTimeRecorder = ProfilerRecorder.StartNew(ProfilerCategory.Internal, "CPU Main Thread Frame Time");
    }

    void OnDisable()

    {
        mainThreadTimeRecorder.Dispose();
    }

    void Update()

    {

        var frameTime = mainThreadTimeRecorder.LastValue;

        // Your code logic here

    }
}


```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-get-timing-data.html)
Get frame timing data
[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-troubleshoot.html)
Troubleshooting the Frame Time Manager

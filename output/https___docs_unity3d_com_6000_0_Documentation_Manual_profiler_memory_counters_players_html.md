* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-memory-counters-players.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * [Unity Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)
  * [Collect performance data](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-collect-data.html)
  * [Memory performance data](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-memory.html)
  * Accessing memory counters in players


[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-memory-introduction.html)
Memory Profiler module introduction
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerMemory.html)
Memory Profiler module reference
# Accessing memory counters in players
You can use the [ProfilerRecorder API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html) to access the Memory **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) module’s counters in a player. 
The following example contains a simple script that collects **Total Reserved Memory** , **GC Reserved Memory** and **System Used Memory** metrics, and displays those as a [`GUI.TextArea`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.TextArea.html). The Memory Profiler module information belongs to the [`ProfilerCategory.Memory`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Memory.html) **Profiler category** Identifies the workload data for a Unity subsystem (for example, Rendering, Scripting and Animation categories). Unity applies color-coding to categories to visually distinguish between the types of data in the **Profiler** window.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profilercategory).
```
using System.Text;
using Unity.Profiling;
using UnityEngine;

public class MemoryStatsScript : MonoBehaviour
{
    string statsText;
    ProfilerRecorder totalReservedMemoryRecorder;
    ProfilerRecorder gcReservedMemoryRecorder;
    ProfilerRecorder systemUsedMemoryRecorder;

    void OnEnable()
    {
        totalReservedMemoryRecorder = ProfilerRecorder.StartNew(ProfilerCategory.Memory, "Total Reserved Memory");
        gcReservedMemoryRecorder = ProfilerRecorder.StartNew(ProfilerCategory.Memory, "GC Reserved Memory");
        systemUsedMemoryRecorder = ProfilerRecorder.StartNew(ProfilerCategory.Memory, "System Used Memory");
    }

    void OnDisable()
    {
        totalReservedMemoryRecorder.Dispose();
        gcReservedMemoryRecorder.Dispose();
        systemUsedMemoryRecorder.Dispose();
    }

    void Update()
    {
        var sb = new StringBuilder(500);
        if (totalReservedMemoryRecorder.Valid)
            sb.AppendLine($"Total Reserved Memory: {totalReservedMemoryRecorder.LastValue}");
        if (gcReservedMemoryRecorder.Valid)
            sb.AppendLine($"GC Reserved Memory: {gcReservedMemoryRecorder.LastValue}");
        if (systemUsedMemoryRecorder.Valid)
            sb.AppendLine($"System Used Memory: {systemUsedMemoryRecorder.LastValue}");
        statsText = sb.ToString();
    }

    void OnGUI()
    {
        GUI.TextArea(new Rect(10, 30, 250, 50), statsText);
    }
}

```

The following screenshot shows the result of adding the script to the [Tanks! tutorial project](https://assetstore.unity.com/packages/essentials/tutorial-projects/tanks-tutorial-46209).
![Tanks! tutorial with the overlaid memory information](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/profiler-tanks-memory-overlay.png) Tanks! tutorial with the overlaid memory information
This information is available in release players, as are the other [high level counters available in the Memory Profiler module](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerMemory.html). If you want to view the selected memory counters in a custom module in the Profiler window, use the [Profiler module editor](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-module-editor.html) to configure the chart.
For more information on adding profiler information to your code, refer to [Adding profiling information to your code](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-adding-information-code.html).
## Additional resources
  * [Adding profiling information to your code](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-adding-information-code.html)
  * [Visualizing profiler counters](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-creating-custom-counters.html)
  * [Memory Profiler module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerMemory.html)
  * [Memory Profiler module introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-memory-introduction.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-memory-introduction.html)
Memory Profiler module introduction
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerMemory.html)
Memory Profiler module reference

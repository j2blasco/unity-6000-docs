* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-play-edit-samples.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * [Unity Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)
  * [Collect performance data](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-collect-data.html)
  * Play mode and Editor profile samples


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerHighlights.html)
Highlights Profiler module reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-deep-profiling.html)
Instrument all function calls
# Play mode and Editor profile samples
When you profile the Unity Editor or Play mode, Unity groups their relevant timings into two sample groups that have the [following markers](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html):
  * `PlayerLoop`: Timings related to Play mode
  * `EditorLoop`: Timings related to the Editor


## Play mode samples
When you profile Play mode, the **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) only collects timing samples that happened inside the `PlayerLoop`. This group helps to reduce the amount of misleading measurements in the [CPU](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html) and [GPU Profiler modules](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerGPU.html).
Unity categorizes any `EditorLoop` samples as **Others** in the [CPU Profiler module charts](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html), meaning that `EditorLoop` samples are the biggest contributors to the **Others** category. If you want to find out what the Editor does in this time and get a detailed breakdown of what contributes to the **Others** category, [profile the Editor process](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-edit-mode.html).
**Important:** If you use [Deep Profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-deep-profiling.html), and target Play mode, it has a performance impact on every call that happens in both `PlayerLoop` and `EditorLoop`. This is because Deep Profiling hooks into the beginning and end of any scripting method call on domain reload and it doesn’t detect which parts are never called from the `PlayerLoop`. The method calls that happen in the `EditorLoop` don’t have the full overhead of creating a sample, but they still check if they emit one, which causes a smaller overhead.
## Editor samples
When you [profile the Editor process](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-edit-mode.html), all the samples that were previously hidden under the `EditorLoop` marker contribute to their respective categories. This means that the information in the [CPU Profiler module’s detail pane](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html) and its charts changes significantly.
There are certain [profiler markers](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html)Placed in code to describe a CPU or GPU event that is then displayed in the Unity Profiler window. Added to Unity code by default, or you can use [ProfilerMarker API](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilermarker-guide.html) to add your own custom markers. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profilermarker) that only appear when you [profile in the Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-edit-mode.html). These markers don’t appear in Player-related activity, and only relate to Editor activity. Editor-only markers include:
  * Security checks like the GetComponentNullErrorWrapper, which helps to identify a null component usage.
  * CheckConsistency, which validates object setup.
  * CheckAllowDestructionRecursive, which is a destruction check.
  * Prefab-related activities.


By default, in the [CPU Profiler module’s **Hierarchy** view](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html), sample stacks with Editor-only markers are collapsed and are named `EditorOnly [SampleName]`. While these sample stacks or their child samples might cause managed allocations that can trigger garbage collection, they don’t contribute to the `GC.Alloc` value of their parent sample if they’re collapsed.
To change the default behavior, in the top right of the module details pane, select the context menu and disable the [Collapse EditorOnly Samples](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html) setting. When you do this, you can expand the sample and contribute its `GC.Alloc` value to the enclosing marker.
This option doesn’t affect the **Timeline** view, and the samples and their children appear expanded. You can usually ignore the samples with these markers, because they relate to Editor-only activity and don’t have any impact on reducing managed allocations. However, they can be useful to investigate if they have a significant performance impact on Play mode.
## Additional resources
  * [Collect performance data in Play mode](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-play-mode.html)
  * [Collect performance data about the Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-edit-mode.html)
  * [CPU Usage Profiler module](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html)
  * [Profiler markers reference](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerHighlights.html)
Highlights Profiler module reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-deep-profiling.html)
Instrument all function calls

* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-cpu-introduction.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * [Unity Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)
  * [Collect performance data](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-collect-data.html)
  * [CPU performance data](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-cpu.html)
  * CPU Usage Profiler module introduction


[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-cpu.html)
CPU performance data
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-cpu-navigating.html)
Navigating the CPU Usage Profiler module
# CPU Usage Profiler module introduction
Get an overview of where your application spends time with the CPU **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) module.
The CPU Usage Profiler module provides an overview of areas where your application spends time, such as on rendering, its **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts), and animation. It displays this information in a chart at the top of the window. You can select individual frames to inspect data in a timeline, or a variety of hierarchical views in the details pane in the lower half of the [Profiler window](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow.html).
## Views
The CPU Usage Profiler module displays profiling data in a timeline view, or in different hierarchical views. The following views are available:
  * **Timeline** : Displays samples in a timeline graph, which displays the relationship between markers on different threads.
  * **Hierarchy** : Displays samples grouped by their call stack and marker.
  * **Inverted Hierarchy** : Displays samples grouped by their marker in inverted sample stacks.
  * **Raw Hierarchy** : Displays samples ungrouped.


To change views, use the [dropdown view selector](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html) in the bottom half of the Profiler window.
![Profiler window with a frame in the CPU Usage Profiler module selected. The Timeline view is selected in the details pane.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/profiler-cpu-module.png) Profiler window with a frame in the CPU Usage Profiler module selected. The Timeline view is selected in the details pane.
### Timeline view
The Timeline view is the default view for the CPU Usage Profiler module. It contains an overview of your application spent time and how the timings relate to each other. It displays performance data from all threads in their own subsections and along the same time axis.
Use the Timeline view to understand how activities on the different threads correlate to each other in their parallel execution. The Timeline view also displays how much your application uses the different threads, such as the [job system’s](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system.html) worker threads. It also indicates how work on the threads are queued up, and if any thread is idling (Idle sample) or waiting for another thread or a job to finish (Wait for x sample).
### Hierarchy views
The Hierarchy views display profiling data one thread at a time, defaulting to the main thread. These views only display a sample’s duration, whereas the Timeline view shows at which times each sample occurred. 
The Hierarchy view lists all samples you have profiled and groups them together by their shared call stack and the hierarchy of [profiler markers](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html)Placed in code to describe a CPU or GPU event that is then displayed in the Unity Profiler window. Added to Unity code by default, or you can use [ProfilerMarker API](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilermarker-guide.html) to add your own custom markers. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profilermarker). The Raw Hierarchy view doesn’t group samples together, which makes it ideal for looking into samples on a granular level.
The Inverted Hierarchy view groups samples by profiler marker and displays them with inverted sample stacks. The first level of the hierarchy shows an item for each profiler marker. Each child item in the tree represents part of an inverted sample stack and its data shows how much time or heap memory contributed via this sample stack to the aggregated parent item. 
The Inverted Hierarchy view is useful to reveal larger performance issues caused by lots of instances of small performance impacts. These kinds of issues can be harder to spot in the Timeline or non-inverted hierarchy views 
## Investigate managed code call stacks and allocations
[Profiler markers](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html) emit a set of samples which the Profiler uses to display and organize profiling information into different chronological and hierarchical views. All samples that the Profiler window displays are part of a sample stack.
A sample stack is different from a method’s call stack because Unity doesn’t tie every sample to a specific method, and it doesn’t record every call as a sample. [Deep Profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-deep-profiling.html) adds a profiler marker to every function call, but it doesn’t add any for native code, and recording these samples comes with a high overhead.
You can use the CPU Usage Profiler module to inspect the full call stacks for samples that `GC.Alloc`, `UnsafeUtility.Malloc`, and `JobHandle.Complete` emit. This is useful if you want to track down where these samples happened, without enabling Deep Profiling and encountering its high overhead. For information on how to enable call stacks, refer to [Enable full call stacks](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-cpu-navigating.html).
### Investigating managed allocations
You can also use the CPU Usage Profiler to investigate where Unity performed memory cleanup.
Whenever your code creates a new managed object there’s a chance that it will not fit in the current memory heap and Unity performs [garbage collection](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-garbage-collector.html). Garbage collection pauses all threads and scans the managed heap for unused memory. This process might take a long time and disrupts frame rate. Managed garbage collection appears as `GC.Collect` samples in the Profiler, while managed allocations appear as `GC.Alloc`.
To prevent the garbage collector from affecting your application’s frame rate, try to keep the `GC.Alloc` value at zero while your application runs, and to keep the heap size small. In the [Timeline view](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html), `GC.Alloc` samples appear colored in red-magenta, and represent the size of the allocation.
To learn where in the code managed allocations happen, you can enable the [full call stacks for GC.Alloc](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-cpu-navigating.html). For more information about the managed heap, refer to the documentation on [Managed memory](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-managed-memory.html).
## Additional resources
  * [Profiler modules introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-modules-introduction.html)
  * [Garbage collector overview](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-garbage-collector.html)
  * [Profiler markers overview](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html)
  * [Profiler window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-cpu.html)
CPU performance data
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-cpu-navigating.html)
Navigating the CPU Usage Profiler module

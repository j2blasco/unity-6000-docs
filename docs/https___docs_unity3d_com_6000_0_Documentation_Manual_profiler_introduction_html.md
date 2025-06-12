* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-introduction.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * [Unity Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)
  * Profiler introduction


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)
Unity Profiler
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-collect-data.html)
Collect performance data
# Profiler introduction
Analyze the performance of your application with the **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler).
The Profiler records multiple areas of your application’s performance, and displays that information to you. You can use this information to decide what you might need to optimize in your application, and to test the performance of changes you make.
To open the Profiler window go to **Window** > **Analysis** > **Profiler**.
![Profiler window with a frame in the CPU Usage Profiler module selected. The Timeline view is selected in the details pane.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/profiler-cpu-module.png) Profiler window with a frame in the CPU Usage Profiler module selected. The Timeline view is selected in the details pane.
You can inspect script code and view how your application uses certain assets and resources that might be slowing it down. You can also compare how your application performs on different devices. The Profiler has several different [Profiler modules](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-modules-introduction.html) which display performance data in areas such as rendering, memory, and audio.
The Profiler is an instrumentation-based profiler, which means that the Profiler uses markers in your application’s code to record detailed timing information about how long the code in each marker takes to execute. The Unity API has profiler markers built in so you can explore the performance of your code, locate performance issues, and identify areas to optimize.
You can also use custom [Profiler markers](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html)Placed in code to describe a CPU or GPU event that is then displayed in the Unity Profiler window. Added to Unity code by default, or you can use [ProfilerMarker API](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilermarker-guide.html) to add your own custom markers. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profilermarker) to monitor specific data, or use [Deep Profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-deep-profiling.html) to further customize the data you gather. 
## Additional resources
  * [Collect performance data](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-collect-data.html)
  * [Visualizing performance data](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-visualizing-data.html)
  * [Using the Profiler window](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)
Unity Profiler
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-collect-data.html)
Collect performance data

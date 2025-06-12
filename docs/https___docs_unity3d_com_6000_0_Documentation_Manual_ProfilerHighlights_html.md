* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerHighlights.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * [Unity Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)
  * [Collect performance data](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-collect-data.html)
  * Highlights Profiler module reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-file-access-module.html)
File Access Profiler module reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-play-edit-samples.html)
Play mode and Editor profile samples
# Highlights Profiler module reference
The Highlights **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) module displays information on whether your application is meeting its target frame rate and if its performance is bound by the CPU or the GPU. It can help you to determine if your application is CPU bound or GPU bound and where to begin investigating potential performance problems.
This module isn’t enabled by default. To enable the Highlights Profiler module, refer to [Activating Profiler modules](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-modules-activate.html)
## Chart
The Highlights chart flags any frames that have exceeded the application’s target frame rate. It displays this information in two lanes of markers:
**Value** | **Description**  
---|---  
**CPU** | Displays red markers in any frames where the CPU has exceeded the target frame time  
**GPU** | Displays yellow markers in any frames where the GPU has exceeded the target frame time  
Hover over any frame in the chart to view a short summary of the frame, including the times of the CPU and the GPU.
## Target Frame Time
Use the dropdown to set a target **frames per second** The frequency at which consecutive frames are displayed in a running game. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingStatistics.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#framespersecond) (FPS) for your application. Select from a preset value, or select **Custom** to set your own. When you select **Custom** , the [Profiler Preferences window](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-preferences-reference.html) opens.
## Details pane
When you select a frame in the Highlights chart, the module’s Details view displays more detailed information about the frame.
The **CPU Active Time** and **GPU Time** are displayed as bar charts relative to the target frame time. To achieve your target frame rate, you must keep the CPU Active Time and the GPU Time below the target frame time. The reason that both the CPU and the GPU each individually have the full frame time to complete their work is because the Unity engine does CPU and GPU work in parallel to achieve optimal performance. 
Select a chart to open the CPU timeline or Frame Debugger respectively to begin your performance investigation.
### CPU Active Time
The CPU Active Time is the duration within the frame that the CPU was doing work for. Unity computes this value by taking the longest thread duration between the main thread and the render thread after subtracting the time that thread spent waiting.
On the main thread, this means that Unity subtracts any **VSync** Vertical synchronization (VSync) is a display setting that caps a game’s frame rate to match the refresh rate of a monitor, to prevent image tearing.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VSync) related markers which don’t represent actual work on the thread, such as `WaitForTargetFPS` or `Gfx.WaitForPresentOnGfxThread` to calculate the thread’s active time. On the render thread, Unity subtracts the time spent waiting for commands as indicated by the marker `Gfx.WaitForGfxCommandsFromMainThread`, to calculate the thread’s active time.
It’s possible for the CPU Active Time to be longer than the CPU Time value displayed in the [CPU Usage module’s](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html) Timeline view when the render thread took longer than the main thread. This is because the Timeline view displays the beginning and end of the frame on the main thread.
### GPU Time
GPU Time is the duration between when the GPU was sent its first command for the frame and when the GPU completed its work for that frame.
You can find guidance on the next steps to take and where to begin your performance investigation in the panel on the right. 
## Additional resources
  * [Profiler window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow.html)
  * [Collect performance data introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-collect-data-introduction.html)
  * [Profiler modules introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-modules-introduction.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-file-access-module.html)
File Access Profiler module reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-play-edit-samples.html)
Play mode and Editor profile samples

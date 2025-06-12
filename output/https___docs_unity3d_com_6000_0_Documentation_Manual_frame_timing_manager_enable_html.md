* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-enable.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Profile rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/profile-rendering.html)
  * [Frame Timing Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-landing.html)
  * Enable the FrameTimingManager


[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager.html)
Introduction to the Frame Timing Manager
[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-get-timing-data.html)
Get frame timing data
# Enable the FrameTimingManager
**Tip** : FrameTimingManager is always active for Development Player builds.
To enable the FrameTimingManage for Release builds and in the Unity Editor:
  1. Go to **Edit** > **Project Settings** > **Player**.
  2. In **Other Settings** , navigate to the **Rendering** heading.
  3. Enable the **Frame Timing Stats** property.


If you use the OpenGL platform, you also need to enable the **OpenGL:**Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) GPU Recorders** property to measure GPU usage. To do this:
  1. Go to **Edit** > **Project** > **Settings** > **Player**.
  2. In **Other Settings** , navigate to the **Rendering** heading.
  3. Enable the **OpenGL: Profiler GPU** property.


Note: In Unity versions 2021.2 and earlier, the **OpenGL Profiler GPU Recorder** disables the **Frame Timing Stats** property, so you can’t use them together.
To access data that the FrameTimingManager records, use one of the following methods:
  * [Retrieve timestamp data from the FrameTimingManager C# API](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-get-timing-data.html).
  * [View frame time data in a Custom Profiler module](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-get-timing-data.html#ViewFrameTimeDataCustomProfilerModule).
  * [Record data through specific profiler counters.](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-record-timing-data.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager.html)
Introduction to the Frame Timing Manager
[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-get-timing-data.html)
Get frame timing data

* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-video-profiler-module.html

  * [Video and cutscenes](https://docs.unity3d.com/6000.0/Documentation/Manual/Video.html)
  * Video Profiler module


[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPanoramic-3D.html)
Set up your 3D panoramic video
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
Scripting
# Video Profiler module
The Video **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) module displays information about what resources the video in your application is using, such as memory, buffering, and number of [video clips](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoClip.html). You can use this to determine how efficiently your application plays back and buffers videos on your selected platforms. You can also use the CPU Usage Profiler module to assess where Unity spends time on video. For more information, see the [CPU Usage Profiler module](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html) documentation.
To open the Profiler window, go to menu: **Window > Analysis > Profiler**.
![The Video Profiler module](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/video-profiler-module.png) The Video Profiler module
## Chart categories
The Video Profiler module’s chart is divided into four categories. To change the order of the categories in the chart, you can drag and drop them in the chart’s legend. You can also click a category’s colored legend to toggle its display. For more information on how to use the Profiler window, see the documentation on [Getting started with the Profiler window](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow.html).
**Chart** | **Description**  
---|---  
**Total Video Sources** | The total number of video sources in your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).  
**Playing Video Sources** | The number of video sources playing in your Scene.  
**Pre-buffered frames** | The total number of pre-buffered frames.  
**Total Video Memory** | The amount of system memory the video in your application is using.  
## Module details pane
When you select a frame in the Video Profiler module, the module details pane at the bottom of the Profiler window displays further detailed information on the video playback in your Scene. The following information is available:
**Detail** | **Description**  
---|---  
**Total Video Sources** | The number of video sources in your Scene.  
**Playing Video Sources** | The number of video sources playing in your Scene.  
**Paused Video Sources** | The number of video sources that are paused.  
**Software Video Playback** | The number of videos playing that the platform doesn’t natively support.  
**Pre-buffered frames** | The total number of pre-buffered frames.  
**Pre-buffered frame limit** | The pre-buffered frame limit. Unity buffers up to 16 frames per clip.  
**Total frames dropped** | Number of frames that Unity had to skip in order to maintain real time. This might happen when your application runs slowly and cannot produce frames fast enough to play in real time.  
**Video Clip Count** | The number of video clips in your Scene.  
**Total Video Memory** | The amount of system memory the video in your application is using.  
## Additional resources
  * [Profiler window introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow.html)
  * [Profiling your application](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-profiling-applications.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPanoramic-3D.html)
Set up your 3D panoramic video
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
Scripting

* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-deep-profiling.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * [Unity Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)
  * [Collect performance data](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-collect-data.html)
  * Instrument all function calls


[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-play-edit-samples.html)
Play mode and Editor profile samples
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-window-navigating.html)
Navigating the Profiler window
# Instrument all function calls
The **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) only profiles code timings that are explicitly wrapped in [Profiler markers](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html)Placed in code to describe a CPU or GPU event that is then displayed in the Unity Profiler window. Added to Unity code by default, or you can use [ProfilerMarker API](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilermarker-guide.html) to add your own custom markers. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profilermarker). This includes the first call stack depth of invocations from Unity’s native code into your scripting code, such as `MonoBehaviour.Start`, `MonoBehaviour.Update`, or similar methods.
The only samples you can visualize as child samples of your scripting code are those that call back into Unity’s API, if that API is instrumented, or any of your own code which has explicit Profiler marker instrumentation. Most API calls that carry a performance overhead are instrumented. For example, accessing the main **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) through the `Camera.main` API registers as a `FindMainCamera` sample.
## Deep profiling
If you want to get data about all function calls to find out where your code impacts on your application’s performance, you can use the **Deep Profile** setting. When you enable the Deep Profile setting, the Profiler injects profiler instrumentation into all your script methods to record all function calls, including at least the first call stack depth into any Unity API.
Deep Profiling is resource-intensive and uses a lot of memory. As a result, your application runs significantly slower while it’s profiling. Deep Profiling works best for small games with simple scripting. If you use complex script code, your application might not be able to use Deep Profiling, and for many larger applications, Deep Profiling might make Unity run out of memory.
### Enabling Deep Profiling
You can enable Deep Profiling if you’re collecting performance data from a connected application, or if you’re collecting data in the Unity Editor.
To enable Deep Profiling for a built application:
  1. Open the **Build Profiles** window (**File** > **Build Profiles**)
  2. Select your application’s target platform
  3. Enable the ****Development Build** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DevelopmentBuild)** setting
  4. Enable **Deep Profiling**


To enable Deep Profiling when you collect data in the Editor:
  1. Open the Profiler window (**Window** > **Analysis** > **Profiler**)
  2. Select **Deep Profile** from the [Profiler toolbar](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow.html).


The Profiler then instruments all function calls when you start a profiling session.
## Additional resources
  * [Build Profiles Profile settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-build-settings-reference.html)
  * [Profiler markers introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html)
  * [Collect performance data introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-collect-data-introduction.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-play-edit-samples.html)
Play mode and Editor profile samples
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-window-navigating.html)
Navigating the Profiler window

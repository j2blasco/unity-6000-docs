* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-edit-mode.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * [Unity Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)
  * [Collect performance data](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-collect-data.html)
  * [Connecting the Profiler to a data source](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-profiling-applications.html)
  * Collect performance data about the Unity Editor


[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-play-mode.html)
Collect performance data in Play mode
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-build-settings-reference.html)
Build Profiles Profiler settings
# Collect performance data about the Unity Editor
Profile the Unity Editor process to understand how the Editor process affects your application in Play mode.
To profile the Editor:
  1. Open the Profiler (**Window > Analysis > Profiler**)
  2. Select the Target Selection dropdown, next to Record
  3. Select Edit

![Profiler windows Target Selection dropdown](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/profiler-target-player.png) Profiler window’s Target Selection dropdown
**Tip:** To reduce the impact that the **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) window has on Editor performance, open the Profiler window in its own process with the [Standalone Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-standalone-process.html). The Standalone Profiler is useful because the Profiler window itself uses resources that might skew the performance data.
## Profile the Editor’s startup times
To profile the Editor’s startup times, start the Editor with the command line option `-profiler-enable`. Refer to [Profiler command line arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-command-line-arguments.html) for more information.
## Additional resources
  * [Collect performance data introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-collect-data-introduction.html)
  * [Collect performance data on a target platform](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-target-device.html)
  * [Collect performance data in Play mode](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-play-mode.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-play-mode.html)
Collect performance data in Play mode
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-build-settings-reference.html)
Build Profiles Profiler settings

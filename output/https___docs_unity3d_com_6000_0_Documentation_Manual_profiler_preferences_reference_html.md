* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-preferences-reference.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * [Unity Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)
  * Profiler Preferences reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow.html)
Profiler window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-command-line-arguments.html)
Profiler command line arguments
# Profiler Preferences reference
The Preferences window contains additional Profiler window settings. To open the Preferences window go to menu: **Unity > Settings > Analysis > Profiler**.
## Profiler settings
Adjust the settings to customize how the **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) collects and displays data.
**Setting** | **Description**  
---|---  
**Frame count** | Set the maximum number of frames for the Profiler to capture. You can set this number between 300 and 2,000.  
**Show stats for ‘current frame’** | Set whether to display annotations on the frame line when you select the Current Frame button (⏭) on the Profiler controls.   
  
This setting is disabled by default, because the annotations might make it difficult to view data in real-time. To display the annotations, enable this setting.  
**Default recording state** | Select which recording state the Profiler opens in:  

  * **Enabled** : Keeps the Record button enabled between profiling sessions.
  * **Disabled** : Disables the Record button, regardless of whether you turn it on or off during your profiling session.
  * **Remember** : Remembers whether you enabled or disabled the Record button during your session and keeps it at its last state the next time you open the Profiler window.

  
**Default editor target mode on start** | Select what mode the Target Selection dropdown targets by default:  

  * **Play mode** (default): Targets [Play mode profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-play-mode.html) by default.
  * **Edit mode** : Targets [Edit mode profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-edit-mode.html) by default.

  
**Custom connection ID** | Change the name of your application as it appears in the Target Selection dropdown.  
**Target**Frames Per Second** The frequency at which consecutive frames are displayed in a running game. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingStatistics.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#framespersecond) (Highlights Module)** | Set the target frames per second that the [Highlights Profiler module](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerHighlights.html) uses. The Highlights Profiler module flags any frames which exceed this target frame rate.  
## Additional resources
  * [Profiler window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow.html)
  * [Profiler modules introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-modules-introduction.html)
  * [Connecting the Profiler to a data source](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-profiling-applications.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow.html)
Profiler window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-command-line-arguments.html)
Profiler command line arguments

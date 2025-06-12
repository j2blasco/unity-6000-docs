* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-command-line-arguments.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * [Unity Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)
  * Profiler command line arguments


[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-preferences-reference.html)
Profiler Preferences reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html)
Profiler markers reference
# Profiler command line arguments
Set how the **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) starts from the command line.
If you start your built player or the Unity Editor from the command line (such as the Command Prompt on Windows, Terminal on macOS, Linux shell, or adb for Android), you can pass command line arguments to configure some Profiler settings. For more information about starting Unity from the command line, refer to [Command line arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/CommandLineArguments.html).
**Command line argument** | **Description**  
---|---  
`-profiler-enable` | Profile the start-up of a player or the Editor.  
  
When you use this argument with a player, it has the same effect as building the player with the [Autoconnect Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-build-settings-reference.html) setting enabled.  
  
When you use this argument with the Editor, it starts collecting and displaying Profiler information in the Profiler window on start-up of the Editor.  
`-profiler-log-file <Path/To/Log/File.raw>` | Stream profile data to a .raw file on startup. This argument works for both players and the Editor.  
`-profiler-capture-frame-count <NumberOfFrames>` | Set how many frames to capture in a profile when streaming to a .raw file on start-up. This argument only works on players.  
`-profiler-maxusedmemory` | Set a maximum amount of memory in bytes for the Profiler to use at start up (for example, `-profiler-maxusedmemory 16777216`). By default, `maxUsedMemory` is 16MB for players and 256MB for the Editor.  
`-connection-id` | Set a custom player name set when you launch a player from the command line. You can also set this name in the [Profiler Preferences window](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-preferences-reference.html).  
## Additional resources
  * [Profiling your application](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-profiling-applications.html)
  * [Profiler Preferences reference](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-preferences-reference.html)
  * [Profiler Build Profiles settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-build-settings-reference.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-preferences-reference.html)
Profiler Preferences reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html)
Profiler markers reference

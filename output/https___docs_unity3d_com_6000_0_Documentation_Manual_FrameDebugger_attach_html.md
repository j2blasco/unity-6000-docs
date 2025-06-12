* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger-attach.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Profile rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/profile-rendering.html)
  * [Frame Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger-landing.html)
  * Attach the Frame Debugger to a built project


[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-hierarchy.html)
Check or find a rendering event
[](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger-share-event-information.html)
Share information about a rendering event
# Attach the Frame Debugger to a built project
You can change the Frame Debugger’s target process to attach the Frame Debugger to a built Unity Player. To be compatible with the Frame Debugger, the Unity Player must:
  * Use the ****Development Build** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DevelopmentBuild)** [Build Setting](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html).
  * Support multithreaded rendering. Every Unity platform except Web supports this.
  * For desktop platforms, use the **Run In Background** [Player Setting](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html). Otherwise, when you focus the Frame Debugger window in the Unity Editor, the Unity Player loses focus and doesn’t reflect any rendering changes.


If the Unity Player fulfills the above requirements, when you next [debug a frame](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger-debug.html), you can attach the Frame Debugger to the Unity Player.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-hierarchy.html)
Check or find a rendering event
[](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger-share-event-information.html)
Share information about a rendering event

* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-optimize-application-startup.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Optimization for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-optimization.html)
  * Optimize application startup times


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-thread-configuration.html)
Android thread configuration
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-game-state-hinting.html)
Game state hinting
# Optimize application startup times
Android devices can optimize the startup process for an application to reduce the time it takes the application to become interactive. For Android to do this, the application must indicate when it finishes initialization and becomes interactive for end users. Android then prioritizes work that must complete before the application is initialized.
Android applications use the [Activity.reportFullyDrawn](https://developer.android.com/reference/android/app/Activity#reportFullyDrawn\(\)) API to indicate that they have finished start-up. By default, Unity calls this method as the first **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) loads, before [Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Awake.html). However, if your application must do some extra work before users can interact with it, for example if the application needs to load some resources before it can show anything on the screen, you should call this API yourself on the frame that your application becomes interactive. To do this, call [DiagnosticsReporting.CallReportFullyDrawn](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.DiagnosticsReporting.CallReportFullyDrawn.html). If you call this method somewhere in your code, Unity no longer calls the method automatically when the first scene loads.
**Note** : Android only counts the first time you call `CallReportFullyDrawn`, so there is no reason to call it multiple times.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-thread-configuration.html)
Android thread configuration
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-game-state-hinting.html)
Game state hinting

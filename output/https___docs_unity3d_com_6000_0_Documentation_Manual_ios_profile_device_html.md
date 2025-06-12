* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ios-profile-device.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone.html)
  * [Developing for iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-developing.html)
  * [Test and debug an iOS application](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-testing-and-debugging.html)
  * Collecting performance data on an iOS device


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-device-simulator.html)
Device Simulator for iOS
[](https://docs.unity3d.com/6000.0/Documentation/Manual/iOSManagedStackTraces.html)
Managed stack traces on iOS
# Collecting performance data on an iOS device
Use the [Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-introduction.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) to collect performance data about your application. You can [collect performance data while in Play mode](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-play-mode.html) in the Unity Editor. However, to get the most accurate data about your application, you can connect the Profiler directly to an iOS device that’s on your network.
## Prerequisites
If you’re using a firewall, open ports `54998` to `55511` in your firewall’s outbound rules. These are the ports Unity uses for remote profiling.
## Enabling remote profiling
To enable remote profiling, follow these steps:
  1. Connect the device to your WiFi network. The Profiler uses a local WiFi network to send profiling data from your device to the Unity Editor.
  2. Attach your device to your computer via cable.
  3. Open the **Build Profiles** window (menu: **File > Build Profiles**).
  4. Enable the ****Development Build** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DevelopmentBuild)** setting.
  5. Enable the **Autoconnect Profiler** setting.
  6. Select **Build & Run**.
  7. When the application launches on the device, open the Profiler window in the Unity Editor (menu: **Window > Analysis > Profiler**).


After you open the Profiler window, it populates with data from your application. If the Editor doesn’t connect to the device automatically, select the Target Selection dropdown menu in the Profiler window and choose the appropriate device to start the Profiler connection manually.
You can also plug the target device directly into your computer to avoid network or connection issues.
## Additional resources
  * [Profiler introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-introduction.html)
  * [Using the Profiler window](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow.html)
  * [Optimize performance for iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-performance.html)
  * [Collect performance data in Play mode](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-play-mode.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-device-simulator.html)
Device Simulator for iOS
[](https://docs.unity3d.com/6000.0/Documentation/Manual/iOSManagedStackTraces.html)
Managed stack traces on iOS

* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/windowsstore-profiler.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Universal Windows Platform](https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsStore.html)
  * [Develop for Universal Windows Platform](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-developing.html)
  * Connect the profiler to UWP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/deep-linking-universal-windows-platform.html)
Use deep linking on UWP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-defines.html)
UWP scripting symbols
# Connect the profiler to UWP
You can use the Unity **profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) to get performance information about your application. For more information, refer to [Profiling your application](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-profiling-applications.html).
Due to restrictions with UWP, you won’t be able to connect the profiler if the Unity Editor is running on the same machine as UWP. Therefore, make sure to run the Unity Editor and UWP on separate machines. For example, if you’re running the Unity Editor and UWP on the same PC, you won’t be able to connect the profiler. The only exception to this rule is the **Autoconnect Profiler** build option, which makes the application connect to the Editor instead. 
You must also ensure that the machine where the Unity Editor is running and the machine where the Universal Windows App is running are on the same subnet.
**Note:** The profiler doesn’t work on Master configuration.
## Connect the Unity profiler
To connect the Unity profiler to a running Universal Windows application, perform the following steps:
  1. Go to **Edit** > **Project Settings** > **Player**.
  2. Select the **Publishing Settings** > **Capabilities** section.
  3. Enable **Private Networks Capability**.
  4. Enable **Internet (Client & Server) Capability**.
  5. If you’ve already enabled the **Autoconnect Profiler** in [Build Profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/windowsstore-buildsettings.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile), the profiler should connect automatically to the Universal Windows App. If not, you have to explicitly select it in Unity in **Window** > **Analysis** > **Profiler** > **Active Profiler**.
  6. Build the Universal Windows App Visual Studio solution from Unity.
  7. Select **Build and Run**.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/deep-linking-universal-windows-platform.html)
Use deep linking on UWP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-defines.html)
UWP scripting symbols

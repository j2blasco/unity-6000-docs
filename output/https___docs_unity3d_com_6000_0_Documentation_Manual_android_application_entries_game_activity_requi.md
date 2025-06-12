* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity-requirements.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Android application entry points](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries.html)
  * [The GameActivity application entry point](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity.html)
  * GameActivity requirements and compatibility


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity.html)
The GameActivity application entry point
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity-modify-bridge.html)
Modify GameActivity bridge code
# GameActivity requirements and compatibility
GameActivity has the following dependencies:
  * CMake build system.
  * AndroidX


## CMake
GameActivity uses CMake to produce the bridge code (`libgame.so`) during the build process.
**Note** : If you provide a custom Android SDK, be sure the SDK has CMake 3.22.1 included.
### AndroidX
GameActivity requires the following AndroidX **Gradle** An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gradle) dependencies:
  * `androidx.appcompat:appcompat`
  * `androidx.games:games-activity`
  * `androidx.core:core`
  * `Androidx.constraintlayout`


Gradle installs AndroidX and these dependencies automatically.
## Plug-in compatibility
If you use GameActivity, your application player loop runs on a native thread rather than a Java thread. This means that calling Java APIs like [myLooper](https://developer.android.com/reference/android/os/Looper#myLooper\(\)) from [plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/PluginsForAndroid.html)A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) will fail. In the case of `myLooper` it’s because there’s no Java looper present on the native thread. This also means that any API that uses APIs such as `myLooper` will also fail. For example, [registerInputDeviceListener](https://developer.android.com/reference/android/hardware/input/InputManager#registerInputDeviceListener\(android.hardware.input.InputManager.InputDeviceListener,%20android.os.Handler\)) will fail if the handler is null. It’s important to understand this limitation when you create [Android plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/PluginsForAndroid.html).
## Choreographer
If you use GameActivity, Unity tries to use the [NDK choreographer](https://developer.android.com/ndk/reference/group/choreographer) to synchronize frame times. If the [Device API Level](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidSdkVersions.html) is lower than 24, or your application uses a 32-bit Player and the Device API Level is lower than 29, Unity uses the [Java choreographer](https://developer.android.com/reference/android/view/Choreographer).
## Additional resources
  * [The Activity application entry point](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-activity.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity.html)
The GameActivity application entry point
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity-modify-bridge.html)
Modify GameActivity bridge code

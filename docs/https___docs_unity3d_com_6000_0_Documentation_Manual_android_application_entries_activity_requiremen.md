* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-activity-requirements.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Android application entry points](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries.html)
  * [The Activity application entry point](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-activity.html)
  * Activity requirements and compatibility


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-activity.html)
The Activity application entry point
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidUnityPlayerActivity.html)
Extend the default Unity activity
# Activity requirements and compatibility
Activity was originally the only application entry point that Unity supported and because of this it’s very stable in the majority of scenarios and is compatible with the majority of Unity features.
## Plug-in compatibility
If you use Activity, your application player loop runs on a Java thread. This means that you can call Java APIs like [myLooper](https://developer.android.com/reference/android/os/Looper#myLooper\(\)) from **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in).
## Choreographer
If you use Activity, Unity uses the [Java choreographer](https://developer.android.com/reference/android/view/Choreographer). This helps you to understand how frame synchronization occurs in your application.
## Additional resources
  * [The GameActivity application entry point](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-activity.html)
The Activity application entry point
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidUnityPlayerActivity.html)
Extend the default Unity activity

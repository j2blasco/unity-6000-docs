* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-activity.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Android application entry points](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries.html)
  * The Activity application entry point


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries.html)
Android application entry points
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-activity-requirements.html)
Activity requirements and compatibility
# The Activity application entry point
[Activity](https://developer.android.com/reference/android/app/Activity) was originally the only application entry point that Unity supported and because of this it’s very stable in the majority of scenarios.
This application entry point is appropriate to use in the following scenarios:
  * Your project uses [plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/PluginsForAndroid.html)A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) that must run on a Java thread. For more information, refer to [Plug-in compatibility](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-activity-requirements.html#plug-in-compatibility).
  * You are upgrading an old project that already uses the Activity application entry point.


If the above scenarios don’t apply to your project, the GameActivity application entry point is a more appropriate application entry point. Among other benefits, Unity’s implementation of GameActivity gives you more control over the interaction between Android and your application. For more information, refer to [GameActivity application entry point](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity.html).
**Topic** | **Description**  
---|---  
[Activity requirements and compatibility](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-activity-requirements.html) | Understand the system requirements and feature compatibility of the Activity application entry point.  
[Extend the default Unity activity](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidUnityPlayerActivity.html) | Override basic interactions between the Android operating system and the Unity Android application.  
## Additional resources
  * [Set the application entry point for your Android application](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-set.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries.html)
Android application entry points
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-activity-requirements.html)
Activity requirements and compatibility

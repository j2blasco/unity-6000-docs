* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Android application entry points](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries.html)
  * The GameActivity application entry point


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-custom-activity-command-line.html)
Specify Android Player command-line arguments
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity-requirements.html)
GameActivity requirements and compatibility
# The GameActivity application entry point
The [GameActivity](https://developer.android.com/games/agdk/game-activity) application entry point is an extension of the [Activity](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-activity.html) application entry point and is the default application entry point for new Unity projects. It provides more control over the interaction between Android and your application than the Activity application entry point. To provide this control, the GameActivity library does the following:
  * It doesn’t directly map to a specific Unity version which means you can update the GameActivity library separately to Unity.
  * It uses a customizable [glue library](https://developer.android.com/reference/games/game-activity/group/android-native-app-glue) as a bridge between itself and Unity. This means you can modify the bridge code to make changes and extend functionality.

**Topic** | **Description**  
---|---  
[GameActivity requirements and compatibility](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity-requirements.html) | Understand the system requirements and feature compatibility of the GameActivity application entry point.  
[Modify GameActivity bridge code](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity-modify-bridge.html) | Make changes to the code that connects the Unity runtime to the GameActivity library.  
[Update the GameActivity library](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity-update-library.html) | Change which version of the GameActivity library your application uses.  
## Additional resources
  * [Set the application entry point for your Android application](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-set.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-custom-activity-command-line.html)
Specify Android Player command-line arguments
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity-requirements.html)
GameActivity requirements and compatibility

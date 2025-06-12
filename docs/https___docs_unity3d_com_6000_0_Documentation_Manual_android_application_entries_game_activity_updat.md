* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity-update-library.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Android application entry points](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries.html)
  * [The GameActivity application entry point](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity.html)
  * Update the GameActivity library


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity-modify-bridge.html)
Modify GameActivity bridge code
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-set.html)
Set the application entry point for your Android application
## Update the GameActivity library
The GameActivity application entry point is implemented as a library separate from the Unity Editor which means that you can update the library independently. This is useful if Google provides bug fixes that your project requires because you can acquire the fixes via a GameActivity library version update.
**Note** : Unity doesn’t test all combinations of Unity version and GameActivity library version. If you update to a newer GameActivity library version, test your application thoroughly.
To update the GameActivity library version, change the value of the `androidx.games:games-activity` dependency in `build.gradle`. For information on the possible methods to do this, refer to [Modify Gradle project files](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files.html).
**Note** : Make sure that the other AndroidX dependencies support the GameActivity version that you want to use. If they don’t you must update them too. For more information, refer to [Declaring dependencies](https://developer.android.com/jetpack/androidx/releases/games#declaring-dependencies).
## Additional resources
  * [Modify GameActivity bridge code](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity-modify-bridge.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity-modify-bridge.html)
Modify GameActivity bridge code
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-set.html)
Set the application entry point for your Android application

* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-set.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Android application entry points](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries.html)
  * Set the application entry point for your Android application


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity-update-library.html)
Update the GameActivity library
[](https://docs.unity3d.com/6000.0/Documentation/Manual/deep-linking-android.html)
Deep linking on Android
# Set the application entry point for your Android application
You control the application entry points through [Android Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html). You can set multiple application entry points for **development builds** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DevelopmentBuild) of your application which helps you to quickly compare functionality and performance between different application entry points. However, you must only select one application entry point for release builds that you intend to publish. If you select more than one, Unity displays a warning message.
To set which application entry point/s to use for your application:
  1. Open [Android Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html).
  2. Go to **Other Settings** > **Configuration** > **Application Entry Point**.
  3. In the **Application Entry Point** section, select which application entry points you want to use.


If you select more than one application entry point and build or export your application, Unity generates multiple `activity` entries in the [Android App Manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/android-manifest.html); one for each application entry point. If you open the project in Android Studio, you can specify which application entry point you want to run/debug in the [Run/Debug Configurations dialog](https://developer.android.com/studio/run/rundebugconfig#opening). If you install the built application on a device, there will be as many application icons as there are application entry points.
## Additional resources
  * [The Activity application entry point](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-activity.html)
  * [The GameActivity application entry point](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity-update-library.html)
Update the GameActivity library
[](https://docs.unity3d.com/6000.0/Documentation/Manual/deep-linking-android.html)
Deep linking on Android

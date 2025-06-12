* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-export-process.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Building and delivering for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-building-and-delivering.html)
  * Export an Android project


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html)
Build your application for Android
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-optimize-distribution-size.html)
Optimize distribution size
# Export an Android project
If you need more control over the build pipeline, you can export a Unity project as a **Gradle** An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gradle) project and import that into Android Studio. This is useful if you want more control over the build pipeline, want to see or modify the [Android App Manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/android-manifest.html) that Unity generates for your application, or [integrate Unity-powered features into another Android application](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityasaLibrary-Android.html).
## Exporting
To export a Unity project for Android Studio:
  1. Open the **Build Profiles** window. (menu: **File** > **Build Profiles**).
  2. From the list of platforms in the **Platforms** panel, select **Android** or [create a build profile](https://docs.unity3d.com/6000.0/Documentation/Manual/create-build-profile.html) for the **Android** platform.  
**Note** : If Android is grayed out, [set up your project for Android development](https://docs.unity3d.com/6000.0/Documentation/Manual/android-sdksetup.html).
  3. Enable **Export Project**.
  4. Click **Export**.
  5. Select the destination folder and click **Select Folder** to start the export process.


After Unity exports the Gradle project, you can import the Gradle project into Android Studio. For information on how to do this, refer to [Migrate to Android Studio](https://developer.android.com/studio/intro/migrate.html). For information on the file structure of the exported Gradle project, refer to [Gradle project structure](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html#gradle-project-structure).
## Additional resources
  * [Gradle for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)
  * [Build your application for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html)
Build your application for Android
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-optimize-distribution-size.html)
Optimize distribution size

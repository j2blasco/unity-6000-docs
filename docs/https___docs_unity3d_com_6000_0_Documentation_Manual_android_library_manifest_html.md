* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-library-manifest.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Introducing Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-introducing.html)
  * Unity Library Manifest


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-launcher-manifest.html)
Unity Launcher Manifest
[](https://docs.unity3d.com/6000.0/Documentation/Manual/how-unity-builds-android-applications.html)
How Unity builds Android applications
# Unity Library Manifest
A Unity Library Manifest is the main Unity manifest and contains information about the Unity Player and its [activity](https://developer.android.com/guide/components/activities/intro-activities). Unity uses a default Unity Library Manifest during the build process to generate the final [Android App Manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/android-manifest.html) for the application. For more information on how to modify this file, refer to [Modify Gradle project files](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files.html).
## Settings
A Unity Library Manifest declares:
  * The Unity [activity](https://developer.android.com/guide/components/activities/intro-activities).
  * The theme that the Unity activity uses.
  * Permissions.
  * **VR** Virtual Reality [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VR) modes.
  * VR performance.
  * Whether to allow the user to resize the application window. This is useful for VR.
  * The maximum **aspect ratio** The relationship of an image’s proportional dimensions, such as its width and height.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AspectRatio).
  * How to react to configuration changes.
  * Supported orientations.
  * Supported launch modes.   
**Note** : Unity only supports the [singleTask launch mode](https://developer.android.com/guide/topics/manifest/activity-element.html#lmode).
  * Android UI.
  * Whether to use hardware acceleration.
  * Which features the application uses such as a gamepad or touchscreen.
  * Which graphics APIs the application supports.
  * Whether the application supports notches on the device.
  * The initial window size.
  * Splash screen configuration.
  * Whether to extract native libraries when installing the application.
  * Which devices the application can run on.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-launcher-manifest.html)
Unity Launcher Manifest
[](https://docs.unity3d.com/6000.0/Documentation/Manual/how-unity-builds-android-applications.html)
How Unity builds Android applications

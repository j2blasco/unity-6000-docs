* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-launcher-manifest.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Introducing Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-introducing.html)
  * Unity Launcher Manifest


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-manifest.html)
Android App Manifest
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-library-manifest.html)
Unity Library Manifest
# Unity Launcher Manifest
A Unity Launcher Manifest configures how the application looks and behaves before the application launches. For example, it contains the application’s icon, name, and install location. The Unity Launcher Manifest is a Unity-specific concept for Android development and you can overwrite it to integrate Unity as a component into an existing project. For more information, see [Integrating Unity into Android applications](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityasaLibrary-Android.html).
## Settings
You can configure all the settings in the Unity Launcher Manifest from [Unity’s Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html). This means, unless you want to integrate Unity as a component into an existing project, you don’t need to overwrite the Unity Launcher Manifest or manually edit any settings directly in the file.
A Unity Launcher Manifest file declares the following:
  * The package’s name.
  * The application’s icons.
  * The application’s name.
  * The application’s [starting activity](https://developer.android.com/guide/components/activities/intro-activities) and its intents.
  * The application’s install location.
  * The application’s supported screen sizes.
  * The application’s `isGame` flag.  
**Note** : This setting is exclusively used by AndroidTV. If you don’t enable AndroidTV support in [Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings), Unity doesn’t declare this setting.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-manifest.html)
Android App Manifest
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-library-manifest.html)
Unity Library Manifest

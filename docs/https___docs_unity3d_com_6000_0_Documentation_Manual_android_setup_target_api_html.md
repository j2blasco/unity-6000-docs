* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-setup-target-api.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Getting started with Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-getting-started.html)
  * [Android environment setup](https://docs.unity3d.com/6000.0/Documentation/Manual/android-sdksetup.html)
  * Set up the Android SDK Target API


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-external-tools-reference.html)
Android External Tools reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html)
Android Player settings
# Set up the Android SDK Target API
Configure the Android SDK Target API level for your application.
The Unity Hub installs the latest version of the Android SDK Target API that Google Play requires. If you need to use a more recent version, you can change it in the [Android Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html).
## Configure Target API version
To configure the Android SDK Target API version in **Android**Player settings** Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings)**, follow these steps: 
  1. Open **Android Player Settings** (menu: **Edit** > **Project Settings** > **Player**).
  2. In the **Other Settings** section, change the **Target API Level**.

![Android Player Settings with the Target API Level dropdown selected.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/android-sdk-target-api.png) Android Player Settings with the Target API Level dropdown selected.
### Newer Target API version
If you select a Target API version newer than the latest installed version, the Unity Android SDK Updater can automatically download and install the new version. Unity displays a prompt and you can choose to either:
  * Automatically download and install the new version of the Android SDK.
  * Continue to use the highest installed version of the Android SDK.


### Older Target API version
If you select a Target API version that’s not installed and is older than the latest installed version, the Unity Android SDK Updater can’t perform the update and Unity displays an error message.
In this case, to update the Android SDK Target API, you must use the Android [sdkmanager](https://developer.android.com/studio/command-line/sdkmanager) from either [Android Studio](https://developer.android.com/studio) or the [command-line tool](https://developer.android.com/studio/command-line/sdkmanager). Regardless of the method you choose, make sure to select the correct Android SDK folder for Unity in the **Android External Tools** section.
**Important** : On Windows, if you installed the Unity Editor in the default folder (`/Program Files/`), you must run the `sdkmanager` with elevated privileges (**Run as Administrator**) to perform the update.
## Additional resources
  * [Install dependencies](https://docs.unity3d.com/6000.0/Documentation/Manual/android-install-dependencies.html)
  * [Android External Tools reference](https://docs.unity3d.com/6000.0/Documentation/Manual/android-external-tools-reference.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-external-tools-reference.html)
Android External Tools reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html)
Android Player settings

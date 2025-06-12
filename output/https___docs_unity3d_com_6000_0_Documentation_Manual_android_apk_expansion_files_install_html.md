* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-apk-expansion-files-install.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Android application size restrictions](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-size-restrictions.html)
  * [APK expansion files](https://docs.unity3d.com/6000.0/Documentation/Manual/android-OBBsupport.html)
  * Manually install an APK expansion file


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-apk-expansion-files-in-unity.html)
APK expansion files in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-apk-expansion-files-host.html)
Host APK expansion files
# Manually install an APK expansion file
Main and patch expansion files must be in a particular location on the device for the application to read from them. If you [Build and Run](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html) your application, Unity installs both the **APK** The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#APK) and the main APK expansion file on the device.
If you instead want to install the application manually, or want to install a patch expansion file, you must use the ****ADB** An Android Debug Bridge (ADB). You can use an ADB to deploy an Android package (APK) manually after building. [More info](https://developer.android.com/studio/command-line/adb.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ADB)** utility to copy APK expansion files into the correct location on your device. For information on how to do this, refer to [Testing file reads](https://developer.android.com/google/play/expansion-files.html#TestingReading). 
**Note** : The APK expansion file name must correspond to the format that Google requires. For more information, refer to [expansion files](https://developer.android.com/google/play/expansion-files.html).
## Additional resources
  * [Host APK expansion files](https://docs.unity3d.com/6000.0/Documentation/Manual/android-apk-expansion-files-host.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-apk-expansion-files-in-unity.html)
APK expansion files in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-apk-expansion-files-host.html)
Host APK expansion files

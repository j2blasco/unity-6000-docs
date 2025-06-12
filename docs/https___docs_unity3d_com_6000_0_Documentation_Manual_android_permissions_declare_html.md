* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-permissions-declare.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Device features and permissions](https://docs.unity3d.com/6000.0/Documentation/Manual/android-device-features-and-permissions.html)
  * Declare permissions for an application


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-permissions-in-unity.html)
Android permissions in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-RequestingPermissions.html)
Request runtime permissions
# Declare permissions for an application
Android applications declare what permissions they require in their [Android App Manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/android-manifest.html). This page explains how to manage permissions for an Android application. For a list of the possible permissions, see [Manifest.permission](https://developer.android.com/reference/android/Manifest.permission).
You can use one of the following methods to modify the Android App Manifest file and manage permissions:
  * Create a custom [Unity Library Manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/android-library-manifest.html) template for Unity to generate the application’s Android App Manifest file from.
  * Export the project and modify the Android App Manifest file in Android Studio.
  * Use the Android Project Configuration manager to modify Android App Manifest file set up in the custom modules of your **gradle** An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gradle) project.


**Note** : Depending on the [Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings) and Unity APIs that the application uses, Unity automatically adds some required permissions to the Unity Library Manifest. For more information, see [Unity-handled permissions](https://docs.unity3d.com/6000.0/Documentation/Manual/android-permissions-in-unity.html#unity-handled-permissions).
## Create a template Unity Library Manifest
Unity uses templates to produce the final Gradle project files. You can override the template that Unity uses and new permissions for an application via the template.
For more information, refer to [Modify Gradle project files with Gradle template files](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-templates.html).
## Use Android Studio
To have complete control over which permissions are in the final Android App Manifest file, export the project and edit the Android App Manifest in Android Studio.
For more information, refer to [Modify Gradle project files with Android Studio](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-android-studio.html).
## Use the Android Project Configuration Manager
Use Android Project Configuration Manager to set up and modify custom Gradle project files in C#. You cannot modify the manifest stored in the default `unityLibrary` and `launcher` modules of your gradle project. You can use the API to set up a custom manifest file in a custom module and add new permissions for your application.
For more information, refer to [Modify Gradle project files with Android Project Configuration Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-agp.html).
## Additional resources
  * [Android permissions in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/android-permissions-in-unity.html)
  * [Request runtime permissions](https://docs.unity3d.com/6000.0/Documentation/Manual/android-RequestingPermissions.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-permissions-in-unity.html)
Android permissions in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-RequestingPermissions.html)
Request runtime permissions

* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-manifest.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Introducing Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-introducing.html)
  * Android App Manifest


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)
Gradle for Android
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-launcher-manifest.html)
Unity Launcher Manifest
# Android App Manifest
The Android App Manifest contains information about an Android application. Each application has a single Android App Manifest [XML](https://en.wikipedia.org/wiki/XML) file at the root of the [source set](https://developer.android.com/studio/build#sourcesets) called `AndroidManifest.xml`. The Android operating system and digital distribution services (for example, Google Play) use Android App Manifests to find information, such as the application’s name, the application’s [entry point](https://developer.android.com/guide/components/activities/intro-activities), Android version support, hardware features support, and application permissions. For more information about the Android App Manifest file, and for a list of settings that it configures, see the Android Developer documentation on [Android App Manifests](https://developer.android.com/guide/topics/manifest/manifest-intro.html).
To generate an Android App Manifest to represent an application, Gradle merges manifest files from a variety of sources. This includes:
  * **Unity Library Manifest** : A manifest file that Unity produces which configures Unity Player activities. For more information, see [Unity Library Manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/android-library-manifest.html).
  * **Unity Launcher Manifest** : A manifest file that Unity produces which configures the application that wraps the Unity library. For more information, see [Unity Launcher Manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/android-launcher-manifest.html).
  * ****Plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) manifests**: Manifest files that represent plug-ins such as Android Archives (AAR) or Android Library plug-ins.


For information on how Unity uses these manifest files to generate an Android App Manifest, see [Generating an Android App Manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/android-manifest.html#generating-an-android-manifest).
## Generating an Android App Manifest
The [Android application build process](https://docs.unity3d.com/6000.0/Documentation/Manual/how-unity-builds-android-applications.html) generate an Android App Manifest file for the application. To do this:
  1. Unity uses the Unity Library Manifest as a template for the Android App Manifest. If you [override the Unity Library Manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-templates.html), Unity uses the file you specify as the template.
  2. Unity updates the Unity Library Manifest and Unity Launcher Manifest files with information such as [permissions](https://docs.unity3d.com/6000.0/Documentation/Manual/android-manifest.html#permissions), configuration options, and the features that the application uses.
  3. [Gradle](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gradle) merges the Unity Library Manifest, Unity Launcher Manifest, and plug-in manifests into one Android App Manifest file.


You can view the Android App Manifest file inside the output Android App Bundle (AAB) or Android Package (APK) using the [Android Studio APK Analyzer](https://developer.android.com/studio/build/apk-analyzer.html), or another third-party tool such as [Apktool](https://ibotpeaches.github.io/Apktool/).
**Important** : You cannot edit the Android App Manifest file in the **APK** The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#APK) or AAB. For information on how to override the contents of an Android App Manifest, refer to [Modify Gradle project files](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files.html).
## Permissions
Unity automatically adds the necessary permissions to the manifest based on the [Android Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html) and Unity APIs that your application calls from C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts). For example:
  * The following classes, packages, and Player setting add the `INTERNET` permission. 
    * Setting **Internet Access** to **Require** in [Android Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html#Configuration) for **development builds** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DevelopmentBuild).
    * [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) and [Ping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ping.html) classes
    * [System.Net.Sockets ](https://learn.microsoft.com/en-us/dotnet/api/system.net.sockets.socket?view=net-8.0) API
    * [Unity Analytics](https://docs.unity.com/ugs/manual/analytics/manual/overview)A data platform that provides analytics for your Unity game. [More info](https://docs.unity.com/ugs/en-us/manual/analytics/manual/overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#UnityAnalytics) package and **Crash and Exception Reporting** in the [Cloud Diagnostics package](https://docs.unity.com/ugs/manual/cloud-diagnostics/manual/CloudDiagnostics/WelcometoCloudDiagnostics).
  * Using vibration (such as [Handheld.Vibrate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handheld.Vibrate.html)) adds `VIBRATE`.
  * The [InternetReachability](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-internetReachability.html) property adds `ACCESS_NETWORK_STATE`.
  * Location APIs (such as [LocationService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LocationService.html)) adds `ACCESS_FINE_LOCATION`
  * [WebCamTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html) APIs add `CAMERA`.
  * The [Microphone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.html) class adds `RECORD_AUDIO`.


If a plug-in requires a permission that is declared in its manifest, Unity automatically adds the permission to the final Android App Manifest during the Gradle merge stage. Note that Unity includes all Unity APIs that the plug-ins use in the permissions list.
You can use the Android [Runtime Permission System](https://developer.android.com/training/permissions/requesting.html) to [request permission at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/android-RequestingPermissions.html), instead of specifying permissions in the Android App Manifest.
For more information about permissions, see Android developer documentation on [Android App Manifest Permissions](https://developer.android.com/guide/topics/manifest/manifest-intro.html#perms).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)
Gradle for Android
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-launcher-manifest.html)
Unity Launcher Manifest

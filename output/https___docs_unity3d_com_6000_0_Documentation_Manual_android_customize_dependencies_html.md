* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-customize-dependencies.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Getting started with Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-getting-started.html)
  * [Android environment setup](https://docs.unity3d.com/6000.0/Documentation/Manual/android-sdksetup.html)
  * Customize dependencies


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-supported-dependency-versions.html)
Supported dependency versions
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-external-tools-reference.html)
Android External Tools reference
# Customize dependencies
Use custom version of a dependency based on the requirement of your project.
It’s recommended to use the Unity Hub to install Android SDK & NDK tools and OpenJDK to ensure that you receive the correct versions and configurations. However, there are situations where you might want to change the SDK, NDK, or JDK version that Unity uses to build applications for Android. For example, if you have multiple versions of Unity with the same dependencies and you don’t want to duplicate the installation of the SDK, NDK, and JDK, you can specify a shared location.
## Use a custom dependency version
To use a custom version of a dependency for your project, follow these steps:
  1. Download the custom version of the dependency.  
**Warning** : Unity only supports versions of the OpenJDK, SDK, or NDK provided through the Unity Hub. For more information, refer to [Supported dependency versions](https://docs.unity3d.com/6000.0/Documentation/Manual/android-supported-dependency-versions.html).
  2. In Unity’s main menu, go to **Edit** > **Preferences** (macOS: **Unity** > **Settings**)
  3. In the left navigation panel, select **External Tools**. The Android section of the **External Tools** panel contains entries for JDK, SDK, NDK, and **Gradle** An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gradle). Each entry contains: 
     * A checkbox that indicates whether to use the version that Unity provides or a custom version.
     * The path to the dependency’s installation folder.
  4. Disable the respective **Installed with Unity (recommended)** option to customize the installation for any of these dependencies . For example, to customize JDK dependency version, disable the **JDK Installed with Unity (recommended)** option.
  5. Select **Browse** to set the custom dependency installation folder path.


Your Unity project now uses the custom dependency version that you set in the **Android External Tools** section.
## Additional resources
  * [Supported dependency versions](https://docs.unity3d.com/6000.0/Documentation/Manual/android-supported-dependency-versions.html)
  * [Android External Tools reference](https://docs.unity3d.com/6000.0/Documentation/Manual/android-external-tools-reference.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-supported-dependency-versions.html)
Supported dependency versions
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-external-tools-reference.html)
Android External Tools reference

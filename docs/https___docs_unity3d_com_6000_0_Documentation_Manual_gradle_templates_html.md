* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/gradle-templates.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Building and delivering for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-building-and-delivering.html)
  * Gradle templates


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-building-and-delivering.html)
Building and delivering for Android
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-template-variables.html)
Gradle template variables
# Gradle templates
Gradle templates configure how to build an Android application using [Gradle](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gradle). Each Gradle template represents a single Gradle project. Gradle projects can include, and depend on, other Gradle projects.
## Gradle template files
A Gradle template consists of the following files:
File | Location | Contains  
---|---|---  
`baseProjectTemplate.gradle` | In the exported project, `root/build.gradle` folder | Configuration information that affects all modules in the final Gradle project. It specifies which Android Gradle Plugin version to use and locations of java plugins. The locations are a combination of online repositories and java plugins inside of this project.  
`launcherTemplate.gradle` | In the exported project, `root/launcher/build.gradle` folder | Instructions on how to build the Android application. This includes bundling, signing, and whether to split the **apk** The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#APK). It depends on the unityLibrary project and outputs either an .apk file or an app bundle.  
`mainTemplate.gradle` | In the exported project, `root/unityLibrary/build.gradle` folder | Instructions on how to build Unity as a Library. This outputs an .aar file. You can override the Unity template with a custom template in the Unity Editor. Refer to the Providing a custom Gradle build template section on this page for more details.  
`libTemplate.gradle` | Varies | If an [Android Library](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidAARPlugins.html) **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) doesn’t include a `build.gradle` file, Unity uses the `libTemplate.gradle` file as a template to generate one. After Unity generates the `build.gradle` file, or if one already exists in the plug-in’s directory, Unity copies the plug-in into the Gradle project.  
`settingsTemplate.gradle` | In the exported project, `root/settings.gradle` file | Specifies the names of modules that the Gradle build system should include when it builds the project. You can override the Unity template with a custom template in the Unity Editor. Refer to the Providing a custom Gradle build template section on this page for more details.  
`gradleTemplate.properties` | In the exported project, `root/gradle.properties` file | Configures the Gradle build system and specifies properties such as the size of the [Java virtual machine (JVM) heap](https://www.ibm.com/docs/en/integration-bus/10.0?topic=development-jvm-heap-sizing)  
To have more control over the Gradle project files that Unity produces, you can override Unity’s default Gradle template files. For information on how to do this, refer to [Modify Gradle project files with Gradle template files](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-templates.html).
## Modifying the exported Gradle project using C#
To modify the Gradle project after Unity assembles it, create a class that inherits from [IPostGenerateGradleAndroidProject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.IPostGenerateGradleAndroidProject.html) and override the [OnPostGenerateGradleAndroidProject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.IPostGenerateGradleAndroidProject.OnPostGenerateGradleAndroidProject.html) function. This function receives the path to the unityLibrary module as a parameter and you can use it to reach the application’s manifest and resources through C# scripting.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-building-and-delivering.html)
Building and delivering for Android
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-template-variables.html)
Gradle template variables

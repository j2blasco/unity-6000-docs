* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Introducing Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-introducing.html)
  * Gradle for Android


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-requirements-and-compatibility.html)
Android requirements and compatibility
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-manifest.html)
Android App Manifest
# Gradle for Android
Gradle is a build system that automates a number of build processes and prevents many common build errors. Unity uses **Gradle** for all Android builds. You can either build the output package (.apk, .aab) in Unity, or export a Gradle project from Unity, and then build it with an external tool such as Android Studio.
For more information about:
  * Gradle: Refer to the [Gradle user manual](https://docs.gradle.org/current/userguide/userguide.html#getting-started) and [Android Gradle plugin documentation](https://developer.android.com/reference/tools/gradle-api).
  * Exporting a Unity project as a Gradle project: Refer to [Exporting an Android Project](https://docs.unity3d.com/6000.0/Documentation/Manual/android-export-process.html).
  * Building an output package (.apk): Refer to Unity documentation on [Building apps for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html) and Android developer documentation on [configuring your build](https://developer.android.com/studio/build/index.html).
  * Building an output package (.aab): Refer to Unity documentation on [Play Asset Delivery](https://docs.unity3d.com/6000.0/Documentation/Manual/play-asset-delivery.html) and Android developer documentation on [Android app bundles](https://developer.android.com/guide/app-bundle/).


## Version compatibility
The following table shows compatibility between Gradle version and Unity version.
Unity version | Gradle version | Android Gradle plug-in version  
---|---|---  
6000.0.45f1+ | 8.11 | 8.7.2  
6000.0.1f1 - 6000.0.44f1 | 8.4 | 8.3.0  
Refer to the Gradle and Android Gradle plug-in versions for other Unity releases: [2022.3](https://docs.unity3d.com/2022.3/Documentation/Manual/android-gradle-overview.html) and [2021.3](https://docs.unity3d.com/2021.3/Documentation/Manual/android-gradle-overview.html)
If you want to use a custom Gradle or Android Gradle plug-in version, it’s important to know the version compatibility between Gradle and the Android Gradle plug-in. For information on this, refer to [Update Gradle](https://developer.android.com/studio/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle).
## Gradle project files
Gradle project files configure different aspects of your application, such as which modules to include and how to build them.
The following table lists the Gradle project files that exist for Unity projects and describes the purpose of each one.
**Gradle project file** | **Purpose**  
---|---  
**Main Manifest** | This file contains important metadata about your Android application. For more information about the responsibilities of the Main/Unity Library Manifest, refer to [Unity Library Manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/android-library-manifest.html).  
**Unity Launcher Manifest** | This file contains important metadata about your Android application’s launcher. For more information about the responsibilities of the Unity Launcher Manifest, refer to [Unity Launcher Manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/android-launcher-manifest.html).  
**Main Gradle** | This file contains information on how to build your Android application as a library.  
**Launcher Gradle** | This file contains instructions on how to build your Android application.  
**Base Gradle** | This file contains configuration that’s shared between all other templates and Gradle projects.  
**Gradle Properties** | This file contains configuration settings for the Gradle build environment. This includes:- The JVM (Java Virtual Machine) memory configuration.- A property to allow Gradle to build using multiple JVMs.- A property for choosing the tool to do the minification.- A property to not compress native libs when building an app bundle.  
**Gradle Settings** | This file contains declaration of artifact repositories to resolve external dependencies required for your application.  
**Proguard** | This file contains configuration settings for the minification process. If minification removes some Java code which should be kept, you should add a rule to keep that code in this file.  
## Gradle project structure
If you export your Unity project as a Gradle project, Unity creates a Gradle project with two modules:
  * UnityLibrary module: Contains the Unity runtime and project data. This module is a library that you can integrate into any other Gradle project. You can use it to embed Unity into existing Android applications.
  * Launcher module: Contains the application’s name and all of its icons. This is a simple Android application module that launches Unity. You can replace it with your own application.

**File** | **Description**  
---|---  
`launcher` | A directory that contains the [launcher module](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html#launcher-module) and everything related to it.  
`src` | A standard Android Gradle project directory that contains the launcher module’s source code and resources. Unity places the source code and resources in the `main` subdirectory.  
`main` | A standard Android Gradle project directory that contains the launcher module’s source code and resources. Unity only supports the main source set. For more information about source sets, refer to [Create source sets](https://developer.android.com/studio/build/build-variants#sourcesets).  
`res` | A standard Android Gradle project directory that contains resources to include in the final application. The resources are application icons, text that the application accesses at runtime, and application style descriptions.   
  
To specify the resources in this directory, set application icons and the project name in the [Android Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html).  
`AndroidManifest.xml` | A standard Android Gradle project file that Unity merges into the final [Android App Manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/android-manifest.html). It contains settings specific to the launcher module.   
  
**Important** : If multiple manifest files specify different values for the same setting, the manifest merging process fails and you must fix it manually. You can specify rules for the manifest merger to automatically decide how to solve merge conflicts. For information on how to do this, refer to [Manage manifest files](https://developer.android.com/studio/build/manage-manifests).   
  
For information on how to influence the contents of this file, refer to [Modify Gradle project files](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files.html).  
`build.gradle` | A standard Gradle project build.gradle file that describes how to build the launcher module and includes a list of dependencies to include in the build. In Unity, the launcher module depends on the [unityLibrary](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html#unity-library) module which means unityLibrary is built and included in the final result when building the launcher module.   
  
To influence the contents of this file, provide a custom [Launcher Gradle Template](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html#Publishing).  
`setupSymbols.gradle` | A Unity-specific file that includes build script to embed debug symbol files into the App Bundle and create symbol files with the legacy `.so` extension.  
`shared` | A directory that contains common configuration information that applies to multiple modules in a project.  
`keepUnitySymbols.gradle` | A Unity-specific file that includes a script to store debug metadata in runtime binaries for resolving stack traces.  
`unityLibrary` | A directory that contains the [unityLibrary module](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html#unity-library) and everything related to it.  
`libs` | A common Android Gradle project directory that stores [Android Archive](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidAARPlugins.html) (.aar) and [Java Archive](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidJARPlugins.html) (.jar) plug-ins for the unityLibrary module.   
  
For exported Unity projects, this contains the `unity-classes.jar` and all .jar and .aar plug-ins in the Unity project.   
  
**Note** : This directory doesn’t contain [Android Library plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidAARPlugins.html). Instead, Unity copies these into the Gradle project as separate modules.  
`unity-classes.jar` | A Unity-specific java plug-in that contains java code that the Unity engine uses.  
`src` | A standard Android Gradle project directory that contains the unityLibrary module’s source code and resources. Unity places the source code and resources in the `main` subdirectory.  
`main` | A standard Android Gradle project directory that contains the unityLibrary module’s source code and resources. Unity only supports the main source set. For more information about source sets, refer to [Create source sets](https://developer.android.com/studio/build/build-variants#sourcesets).  
`assets` | A standard Android Gradle directory that contains project assets. Unity places the Unity project’s resources in the `bin` subdirectory.  
`bin` | A standard Android Gradle project directory that Unity adds all the Unity project’s resources to.  
`java` | A standard Android Gradle project directory that contains uncompiled java source files for the unityLibrary module. Unity only uses this directory to store the UnityPlayerActivity source file. For information on how to extend UnityPlayerActivity, refer to [Extending the UnityPlayerActivity Java Code](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidUnityPlayerActivity.html).  
`jniLibs` | A standard Android Gradle project directory that contains native code libraries that the unityLibrary module uses. Unity places the `libil2cpp`, `libmain`, and `libunity` Unity engine libraries in this directory. Unity also places any [Native (C++) plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidNativePlugins.html) in this directory.  
`jniStaticLibs` | A standard Android project directory that contains `baselib.a` library that the unityLibrary module uses to create `libil2cpp.so`.  
`res` | A standard Android Gradle project directory that contains resources to include in the final application. For exported Unity projects, the `res` directory for the unityLibrary module only contains style descriptions that the unityLibrary module uses.  
`AndroidManifest.xml` | A standard Android Gradle project file that Unity merges into the final [Android App Manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/android-manifest.html). It contains settings specific to the unityLibrary module.   
  
To influence the contents of this file, provide a custom [Custom Main Manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html#Publishing).  
`symbols` | A directory that Unity adds if you choose to generate symbol files for your application through the [Debug Symbols](https://docs.unity3d.com/6000.0/Documentation/Manual/android-build-settings.html#debug-symbols) build setting. This directory includes files containing debug metadata and the symbol table section for Unity libraries. You can set the directory path in Android Studio to resolve function names during debugging.  
`build.gradle` | A standard Gradle project build.gradle file that describes how to build the unityLibrary module and includes a list of dependencies to include in the build. In Unity, the unityLibrary module depends on all of the [plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/PluginsForAndroid.html)A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) in the Unity project.   
  
To influence the contents of this file, provide a custom [Main Gradle Template](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html#Publishing).  
`proguard-unity.txt` | A Unity-specific file that contains ProGuard configurations for Unity java code (code in unity-classes.jar plug-in). Configurations are effective when Minification is enabled in **Player settings** Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings) (or if it’s enabled by manually modifying gradle build files).  
`build.gradle` | The base Gradle file that affects all modules in the Gradle project. It specifies which plug-in versions to use in this Gradle project. One of these plug-ins is Android Gradle Plug-in.   
  
To influence the contents of this file, provide a custom [Base Gradle Template](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html#Publishing).  
`proguard-user.txt` | This is a Unity project specific file which contains ProGuard configurations for the project’s java code and third-party java plug-ins. Just like `ProGuard-unity.txt` Gradle uses it if you enable minification.   
  
To create this file, enable **Custom Proguard File** in the [Android Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html#Publishing).  
`gradle.properties` | A standard Gradle project file that configures how to build the application. For information on the Unity specific properties in this file, refer to [Properties in gradle.properties file](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html#unity-gradle-properties). For information on the Gradle properties this file can contain, refer to [Gradle property files](https://developer.android.com/studio/build#properties-files).  
  
To influence the contents of this file, provide a custom [Gradle Properties Template](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html#Publishing).  
`local.properties` | A standard Android Gradle project file that configures the environment of the build system. Unity specifies the path to SDK here so that by default, the exported Gradle project uses the same SDK that the Unity Editor used. NDK path used to be specified here with previous Gradle versions as well, but now Unity specifies it in the build.gradle files of **launcher** and **unityLibrary** modules.   
  
For information on the properties this file can contain, refer to [Gradle property files](https://developer.android.com/studio/build#properties-files).  
`settings.gradle` | A standard Android Gradle project file that specifies all of the modules that make up this Android Gradle project. In projects that Unity exports, this usually only specifies the **launcher** and **unityLibrary** modules. However, if the Unity project uses [Play Asset Delivery](https://docs.unity3d.com/6000.0/Documentation/Manual/play-asset-delivery.html), each asset pack is a separate module, so this file lists them too. The file also specifies locations which contain Gradle project plug-ins. The locations are a combination of online repositories and java plug-ins inside of this project.   
  
To influence the contents of this file, provide a custom [Gradle Settings Template](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html#Publishing).  
### Properties in gradle.properties file
`gradle.properties` file includes the following properties that are specific to Unity:
**Property** | **Description**  
---|---  
**unityStreamingAssets** | Indicates the names of assets inside the [Streaming Assets](https://docs.unity3d.com/6000.0/Documentation/Manual/StreamingAssets.html) directory. Unity specifies that these assets should be in the final application and Gradle shouldn’t compress them.  
**unityTemplateVersion** | The version of the Gradle template file that Unity uses. If your project’s Gradle template version differs from the specified one, Unity throws an error to inform you to update your Gradle files and build your project in an empty folder.  
**unity.projectPath** | The path to your Unity project.  
**unity.debugSymbolLevel** | The debug symbol level used by Unity.  
**unity.buildToolsVersion** | The build tools version used by Unity.  
**unity.minSdkVersion** | The minimum API level used by Unity.  
**unity.targetSdkVersion** | The target API level used by Unity.  
**unity.compileSdkVersion** | The compile SDK version of the Android SDK that’s used to compile your application during the build process.  
**unity.applicationId** | The application ID used by Unity. For example, `com.MyCompany.MyApp`.  
**unity.abiFilters** | The Application Binary Interface (ABI) configurations included in the application used by Unity and are separated by commas. For example, armeabi-v7a, arm64-v8a.  
**unity.versionCode** | The internal version number for the application. It’s used to indicate how recent the application version is, where higher number denotes a more recent version.  
**unity.versionName** | The application version number expressed as a string. This version number is visible to the users.  
**unity.namespace** | The application namespace used by Unity. For example, `com.MyCompany.MyApp`.  
**unity.androidSdkPath** | The Android Software Development Kit (SDK) installation folder path set in the **Android** section of **External Tools** , menu: **Edit** > **Preferences** > **External Tools** (macOS: **Unity** > **Settings** > **External Tools**).  
**unity.androidNdkPath** | The Android Native Development Kit (NDK) installation folder path set in the **Android** section of **External Tools** , menu: **Edit** > **Preferences** > **External Tools** (macOS: **Unity** > **Settings** > **External Tools**).  
**unity.androidNdkVersion** | The Android Native Development Kit (NDK) version set in the **Android** section of **External Tools** , menu: **Edit** > **Preferences** > **External Tools** (macOS: **Unity** > **Settings** > **External Tools**).  
**unity.jdkPath** | The Java Development Kit (JDK) installation folder path set in the **Android** section of **External Tools** , menu: **Edit** > **Preferences** > **External Tools** (macOS: **Unity** > **Settings** > **External Tools**).  
**unity.javaCompatabilityVersion** | The Java compatibility version used by Unity.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-requirements-and-compatibility.html)
Android requirements and compatibility
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-manifest.html)
Android App Manifest

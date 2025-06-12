* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-symbols.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Testing and debugging](https://docs.unity3d.com/6000.0/Documentation/Manual/android-testing-and-debugging.html)
  * Android symbols


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-debugging-on-an-android-device.html)
Debug on Android devices
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-device-simulator.html)
Simulate an Android device
# Android symbols
To help you debug your application, Unity can generate a package that contains symbol files with debug metadata for native Unity libraries. Symbol files contain an executable file section called symbol table (`.symtab`) that translates active memory addresses into information you can use, like a method name. The translation process is called symbolication. You can upload a symbols package to the Google Play Console to see a human-readable stack trace on the [Android Vitals](https://developer.android.com/topic/performance/vitals) dashboard.
For more information about executable file (ELF) section, refer to [Wikipedia](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format).
Unity generates symbol files for the following libraries:
  * `libmain`: Responsible for the initial Unity engine loading logic. The symbol file is precompiled.
  * `libunity`: Unity’s engine code:
    * If **Strip Engine Code** property is disabled, the symbol file is precompiled.
    * If **Strip Engine Code** property is enabled, Unity compiles the symbol file during build process.
  * `libil2cpp`: Contains C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts):
    * If you don’t export your project, Unity compiles the symbol file during build process.
    * If you export your project, **Gradle** An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gradle) compiles the symbol file.


Gradle generates the remaining symbol files.
Depending upon your application build format, Unity generates symbol files in two ways :
  * As a zip file that can be generated for both `apk` or `aab`.
  * Directly embeds symbol files in the `aab`. Unity doesn’t embed symbol files into an `apk`.


Use [UserBuildSettings.DebugSymbols.format](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.UserBuildSettings.DebugSymbols-format.html) API to set the format of the symbol package.
## Types of symbol files
Unity uses [debugSymbolLevel](https://developer.android.com/reference/tools/gradle-api/7.3/com/android/build/api/dsl/Ndk#debugSymbolLevel\(\)) property of Gradle to generate symbol files. There are two types of symbol files:
  * Public: A small file that contains a symbol table section. For more information, refer to [Public symbols](https://docs.unity3d.com/6000.0/Documentation/Manual/android-symbols.html#public-symbols).
  * Debugging: Contains everything that a public symbol file contains along with full debugging information that you can use for more in-depth debugging. For more information, refer to [Debugging symbols](https://docs.unity3d.com/6000.0/Documentation/Manual/android-symbols.html#debugging-symbols).


Use [UserBuildSettings.DebugSymbols.level](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.UserBuildSettings.DebugSymbols-level.html) to generate the required type of symbol file.
**Note:** By default, Gradle generates symbol files with `.so.sym` or `.so.dbg` extensions. Some digital distribution services don’t recognize these extensions and require files with `.so` extension. In such cases, use [Unity.Android.Types.DebugSymbolFormat.LegacyExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Types.DebugSymbolFormat.LegacyExtensions.html) API to create symbol files with `.so` extension.
```
UserBuildSettings.DebugSymbols.format = DebugSymbolFormat.IncludeInBundle | DebugSymbolFormat.Zip | DebugSymbolFormat.LegacyExtensions;

```

### Public symbols
A public symbols file contains information that resolves function addresses to human-readable strings. These files don’t contain debugging information. This makes public symbol files smaller than [debugging symbols](https://docs.unity3d.com/6000.0/Documentation/Manual/android-symbols.html#debugging-symbols) files.
### Debugging symbols
A debugging symbols file contains full debugging information and a symbol table section. Use it to:
  * Resolve stack traces and to debug applications that you have source code available for.
  * Attach a native debugger to the application and debug the code.


**Note:** If debugging symbols aren’t available, Unity places a [public symbols](https://docs.unity3d.com/6000.0/Documentation/Manual/android-symbols.html#public-symbols) file in your project at build time. For the `libmain` and `libunity` libraries, debugging symbols aren’t available and Unity always generates public files.
### Custom symbols
You can instruct Unity to include additional symbol files. This is useful if you use shared libraries and want your local debugger, and Google Play, to resolve the shared library stack traces if the application crashes.
To make Unity include a custom symbols file:
  1. In the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), select a **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) that has a `.so` file extension.
  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), find the **Platform settings** section.
  3. Set **CPU** to the CPU architecture that the symbols file is compatible with.
  4. Set **Shared Library Type** to **Symbol**.


Whenever Unity generates a symbols package, it adds the additional symbol files to the symbols package.
If you want to make Unity include a custom symbols file from a C# script, the **UnityEditor.Android** namespace includes the following APIs to set the **CPU** and **Shared Library Type** respectively:
  * [PluginImporter.SetAndroidCPU](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidPluginImporterUtilities.SetAndroidCPU.html)
  * [PluginImporter.SetAndroidSharedLibraryType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidPluginImporterUtilities.SetAndroidSharedLibraryType.html)


**Note:** The symbols file name must match the name of the shared library that the symbols file is for. For example, if a shared library is called **mylibrary.so** , the symbols file must also be named **mylibrary.so**. To avoid file name **collisions** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision), the symbols file and the shared library must be in separate directories.
**Important:** Ensure the symbols file is up to date and compatible with the shared library that contains the executable code. If you don’t, your local debugger and Google Play will fail to resolve stack traces for code in the shared library.
![Custom plug-in in the Inspector.](https://docs.unity3d.com/6000.0/Documentation/uploads/Android/android_custom_symbol.png) Custom plug-in in the Inspector.
## Generating a symbols package
There are two ways to enable symbols package generation for your application:
  * Through the ****Build Profiles** A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile)** window.
  * Using the [UserBuildSettings.DebugSymbols.level](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.UserBuildSettings.DebugSymbols-level.html) and [UserBuildSettings.DebugSymbols.format](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.UserBuildSettings.DebugSymbols-format.html) APIs.


To enable symbols package generation through the **Build Profiles** window:
  1. Open the **Build Profiles** window (menu: **File** > **Build Profiles**).
  2. From the list of platforms in the **Platforms** panel, select **Android** or [create a build profile](https://docs.unity3d.com/6000.0/Documentation/Manual/create-build-profile.html) for the **Android** platform.
  3. Set **Debug Symbols** to one of the following:
     * [Public](https://docs.unity3d.com/6000.0/Documentation/Manual/android-symbols.html#public-symbols)
     * [Debugging](https://docs.unity3d.com/6000.0/Documentation/Manual/android-symbols.html#debugging-symbols)
  4. Set **Symbols output options** to **.zip**.


After you enable symbols package generation, building your project generates a `.zip` file that contains symbol files for the `libmain` and `libunity` library. If you set your [scripting backend](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ScriptingBackend) to ****IL2CPP** A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP)**, the `.zip` also contains a symbol file for the `libil2cpp` library. Unity places this symbols package within the output directory.
If you enable **Export Project** in the Android build settings, Unity doesn’t build the project. Instead, it exports the project for Android Studio, generates symbols for `libmain` and `libunity`, and places them within `unityLibrary/symbols/<architecture>/` in the output directory. When you build your exported project from Android Studio, Gradle generates the `libil2cpp` symbol file and places it within the `unityLibrary/symbols/<architecture>/` directory alongside the `libmain` and `libunity` symbol file.
## Using symbols in the Google Play console
### Embedded symbols
If you’re producing an Android App bundle (aab), you can embed symbols directly into an `aab` and upload it to Google Play.
**Note:** Unity doesn’t embed symbols into an `apk`. In this case, you must upload a zip file with symbols separately.
```
UserBuildSettings.DebugSymbols.level = DebugSymbolLevel.SymbolTable;
UserBuildSettings.DebugSymbols.format = DebugSymbolFormat.IncludeInBundle;

```

### Zipped symbols
To produce a zipped symbols package, use the following code:
```
UserBuildSettings.DebugSymbols.level = DebugSymbolLevel.SymbolTable;
UserBuildSettings.DebugSymbols.format = DebugSymbolFormat.Zip | DebugSymbolFormat.LegacyExtensions;

```

After you upload your application to Google Play, you can upload a [public symbols](https://docs.unity3d.com/6000.0/Documentation/Manual/android-symbols.html#public-symbols) zip package. For information on how to do this, refer to Google’s documentation: [Deobfuscate or symbolicate crash stack traces](https://support.google.com/googleplay/android-developer/answer/9848633).
**Note:** Google Play doesn’t symbolicate crashes that your application received before you uploaded the symbols package.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-debugging-on-an-android-device.html)
Debug on Android devices
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-device-simulator.html)
Simulate an Android device

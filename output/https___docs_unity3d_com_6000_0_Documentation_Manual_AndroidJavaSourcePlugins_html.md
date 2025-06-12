* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidJavaSourcePlugins.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Create and use plug-ins in Android](https://docs.unity3d.com/6000.0/Documentation/Manual/PluginsForAndroid.html)
  * [Android plug-in types](https://docs.unity3d.com/6000.0/Documentation/Manual/android-plugin-types.html)
  * Java and Kotlin source plug-ins


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-native-plugins-call.html)
Call native plug-in for Android code
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-plugins-java-code-from-c-sharp.html)
Call Java and Kotlin plug-in code from C# scripts
# Java and Kotlin source plug-ins
Unity can interpret individual Java and Kotlin source files as individual **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in).
Unity supports Java and Kotlin code written in source files with `.java` and `.kt` extensions. To do this, Unity interprets each source file as an individual plug-in and compiles them when it builds the Player. This type of plug-in is useful if you need to write a small amount of code for a single project. If you plan to reuse the code in multiple projects or distribute it to other people, then an [Android Library or Android Archive plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidAARPlugins.html) might be more appropriate.
## Create a Java or Kotlin source plug-in
To indicate to Unity to create a plug-in from a Java (`.java`) or Kotlin (`.kt`) source file:
  1. In the **Assets** folder, place your Java (`.java`) or Kotlin (`.kt`) source file.  
**Tip** : It’s best practice to create a sub-folder to contain your Java and Kotlin source files.
  2. Select the source file and view it in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window.
  3. In the Inspector, under the **Select Platforms for plugin** section, enable **Android**.
  4. Select **Apply**.


**Note** : You can place the source files in any folder in your Project, except in special use locations such as StreamingAssets. If you place files in these locations, the Unity Editor doesn’t display the plug-in inspector.
## Edit Java or Kotlin files in an exported Android Studio project
By default when you [export a Unity project for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-export-process.html), Unity copies any Java/Kotlin files over to the Android Studio project. If you edit these files in Android Studio, the changes aren’t reflected in the original files in the Unity project. If you export the Unity project again, the export process will overwrite your changes in Android Studio.
To resolve this, Unity provides the **Symlink Sources** [Build Setting](https://docs.unity3d.com/6000.0/Documentation/Manual/android-build-settings.html). If you select this Build Setting, Unity creates a [symbolic link](https://en.wikipedia.org/wiki/Symbolic_link) in the Android Studio project to Java/Kotlin files in the Unity project, instead of copying files over. This means that if you edit the files from Android Studio, the edit affects the files in the original Unity project.
## Additional resources
  * [Android plug-in types](https://docs.unity3d.com/6000.0/Documentation/Manual/android-plugin-types.html)
  * [Call Java and Kotlin plug-in code from C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/android-plugins-java-code-from-c-sharp.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-native-plugins-call.html)
Call native plug-in for Android code
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-plugins-java-code-from-c-sharp.html)
Call Java and Kotlin plug-in code from C# scripts

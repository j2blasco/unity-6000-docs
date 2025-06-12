* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidJARPlugins.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Create and use plug-ins in Android](https://docs.unity3d.com/6000.0/Documentation/Manual/PluginsForAndroid.html)
  * [Android plug-in types](https://docs.unity3d.com/6000.0/Documentation/Manual/android-plugin-types.html)
  * JAR plug-ins


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-aar-import.html)
Import an Android Archive plug-in
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidNativePlugins.html)
Native plug-ins for Android
# JAR plug-ins
You can use Java Archive (JAR) **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) to interact with the Android OS or to call methods written in Java from C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts).
Java Archive (JAR) plug-ins contain Java code that you can call from C# scripts. They’re useful if you want to interact with the Android operating system, or just call Java code from C#.
This type of plug-in is useful if you plan to reuse Java code in multiple projects, or distribute it to other people. If instead you only want to write a small amount of Java code for a single project, then a [Java or Kotlin source code plug-in](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidJavaSourcePlugins.html) might be more appropriate.
## Import a JAR plug-in
To import a [JAR plug-in](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidJARPlugins.html) (AAR) plug-in into your Unity Project:
  1. Copy the `.jar` file to your Unity Project’s **Assets** folder.
  2. Select the `.jar` file in Unity and view it in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
  3. In the **Select platforms for plugin** section, select **Android**.
  4. Select **Apply**.


## Additional resources
  * [Android plug-in types](https://docs.unity3d.com/6000.0/Documentation/Manual/android-plugin-types.html)
  * [Call Java and Kotlin plug-in code from C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/android-plugins-java-code-from-c-sharp.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-aar-import.html)
Import an Android Archive plug-in
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidNativePlugins.html)
Native plug-ins for Android

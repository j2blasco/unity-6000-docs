* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-agp.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Building and delivering for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-building-and-delivering.html)
  * [Modify Gradle project files](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files.html)
  * Modify Gradle project files with the Android Project Configuration Manager


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-templates.html)
Modify Gradle project files with Gradle template files
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-android-studio.html)
Modify Gradle project files with Android Studio
# Modify Gradle project files with the Android Project Configuration Manager
You can use Android Project Configuration Manager to modify the contents of custom **gradle** An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gradle) project files in your Android project. You cannot modify the contents of the default gradle project files `unityLibrary` and `launcher` modules with Android Project Configuration Manager. However, you can create custom modules to set up custom Gradle project files and modify them as required.
The entry point for the Android Project Configuration Manager is the [OnModifyAndroidProjectFiles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifier.OnModifyAndroidProjectFiles.html) method in the [AndroidProjectFilesModifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifier.html) interface. This means to use the Android Project Configuration Manager, first create a class that implements `AndroidProjectFilesModifier` and declares a body for `OnModifyAndroidProjectFiles`. The following code example shows how to do this.
```
using UnityEditor.Android;

public class ModifyProjectScript : AndroidProjectFilesModifier
{
    public override void OnModifyAndroidProjectFiles(AndroidProjectFiles projectFiles)
    {
    }
}

```

## Additional resources
  * [Export an Android project](https://docs.unity3d.com/6000.0/Documentation/Manual/android-export-process.html)
  * [Modify Gradle project files with Gradle template files](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-templates.html)
  * [Modify Gradle project files with Android Studio](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-android-studio.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-templates.html)
Modify Gradle project files with Gradle template files
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-android-studio.html)
Modify Gradle project files with Android Studio

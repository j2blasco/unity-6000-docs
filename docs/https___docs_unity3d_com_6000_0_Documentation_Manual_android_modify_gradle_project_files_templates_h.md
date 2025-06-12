* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-templates.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Building and delivering for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-building-and-delivering.html)
  * [Modify Gradle project files](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files.html)
  * Modify Gradle project files with Gradle template files


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-methods.html)
Modify the Gradle project files for a Unity application
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-agp.html)
Modify Gradle project files with the Android Project Configuration Manager
# Modify Gradle project files with Gradle template files
To have some control over the format and contents of **Gradle** An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gradle) project files, you can override Unity’s default templates with your own custom template. To do this:
  1. Go to **Edit** > **Project Settings** to open the Project Settings window.
  2. Select the **Player** tab, then open [Android Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html)
  3. In the **Publishing Settings** section, enable the checkbox that corresponds to the Gradle project file type you want to create a custom template for. This creates a Gradle project template file and displays the path to the file.
  4. Modify the template file to control the final format and contents of the final Gradle project file.


**Note** : If there is a discrepancy between the values set in the Android **Player settings** Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings) and the template file, Unity displays a warning message, and Player settings take precedence.
To verify that your template modifications give the result that you expect, [export your project](https://docs.unity3d.com/6000.0/Documentation/Manual/android-export-process.html) and view the final Gradle project files in the resulting project.
## Additional resources
  * [Gradle template variables](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-template-variables.html)
  * [Export an Android project](https://docs.unity3d.com/6000.0/Documentation/Manual/android-export-process.html)
  * [Modify Gradle project files with the Android Project Configuration Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-agp.html)
  * [Modify Gradle project files with Android Studio](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-android-studio.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-methods.html)
Modify the Gradle project files for a Unity application
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-agp.html)
Modify Gradle project files with the Android Project Configuration Manager

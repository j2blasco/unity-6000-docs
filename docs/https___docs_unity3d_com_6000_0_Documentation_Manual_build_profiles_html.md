* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Editor Features](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorFeatures.html)
  * [Build profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html)
  * Introduction to build profiles


[](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html)
Build profiles
[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-build-profile.html)
Create and manage build profiles
# Introduction to build profiles
A **build profile** is a set of configuration settings you can use to build your application on a particular platform. Use the **Build Profiles** window to create multiple build profiles for each platform you work on, saving different configurations for release and **development builds** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DevelopmentBuild). For more information on release and development builds, refer to [Understanding build types](https://docs.unity3d.com/6000.0/Documentation/Manual/build-types.html).
Navigate to **File** > **Build Profiles** to access the **Build Profiles** window.
## Profile types
There are two types of profiles available in the **Build Profiles** window.
### Platforms
The Platforms pane displays a list of currently installed platforms that Unity supports. A platform profile includes some [shared settings](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles-reference.html#shared-build-settings) that apply to all platforms. For example, if you enable the **Development Build** setting for one platform profile, Unity will enable the setting across all the available platform profiles. Platforms also share the same **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) data across each platform profile.
You can duplicate a platform, and create a new build profile. To do that, right click your selected platform and select **Copy to new profile**. 
### Build Profiles
Unlike platforms, settings saved under build profiles aren’t shared across all the platforms. You can assign specific scenes to each build profile. Build profiles allow you to save multiple independent build configurations. You can save as many build profiles as you require using a custom name for each profile. Unity saves the build profile as an asset file that is ready for use with **version control** A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and PlasticSCM. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VersionControl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VersionControl).
![Build profiles stored as Assets in the Project window.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/build-profiles-assets.png) Build profiles stored as Assets in the Project window.
## Additional resources
  * [Create a build profile](https://docs.unity3d.com/6000.0/Documentation/Manual/create-build-profile.html)
  * [Build Profiles window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles-reference.html)
  * [Build Profiles scripting API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Profile.BuildProfile.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html)
Build profiles
[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-build-profile.html)
Create and manage build profiles

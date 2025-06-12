* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/override-player-settings.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Editor Features](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorFeatures.html)
  * [Build profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html)
  * Override Player settings with build profiles


[](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profile-scene-list.html)
Manage scenes in your build
[](https://docs.unity3d.com/6000.0/Documentation/Manual/build-types.html)
Introduction to build types
# Override Player settings with build profiles
You can override Player settings when using a build profile for your target platform. This allows you to have custom Player settings for each build profile you want to use.
## Override Player settings
To override Player settings, use the following steps:
  1. Navigate to **File** > **Build Profiles**.
  2. Select or create a build profile for your target platform. For information on how to create a build profile, refer to [Create a build profile](https://docs.unity3d.com/6000.0/Documentation/Manual/create-build-profile.html).
  3. In the **Player Settings Overrides** section, select **Customize player settings**.


The [Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings) for the build profile’s target platform will appear, allowing you to customize them as required. The Player settings inherit their initial values from your build targets global Player settings. To update these global settings, navigate to **Edit** > **Project Settings** > **Player**.
**Note** : You can only override Player settings for build profiles. If you want to override Player settings for a platform profile, you must create a build profile for that target.
## Remove and reset Player settings overrides
You can remove and reset any overridden Player settings for your build profile using the available options from the **More** (**⋮**) menu. The available options are as follows:
**Property** | **Description**  
---|---  
**Remove Overrides** | Remove and reset all overridden Player settings. To add new overrides, you must select **Customize player settings**.  
**Reset To Globals** | Reset overridden Player setting values to the global values for the target platform. Set the global values from **Edit** > **Project Settings** > **Player**.  
## Additional resources
  * [Build profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile)
  * [Create a build profile](https://docs.unity3d.com/6000.0/Documentation/Manual/create-build-profile.html)
  * [Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profile-scene-list.html)
Manage scenes in your build
[](https://docs.unity3d.com/6000.0/Documentation/Manual/build-types.html)
Introduction to build types

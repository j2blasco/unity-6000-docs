* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide2022LTS.html

  * [Install and upgrade](https://docs.unity3d.com/6000.0/Documentation/Manual/install-and-upgrade.html)
  * [Upgrade Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuides.html)
  * Upgrade to Unity 2022 LTS


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide20231.html)
Upgrade to Unity 2023.1
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide2021LTS.html)
Upgrade to Unity 2021 LTS
# Upgrade to Unity 2022 LTS
This page lists changes in Unity 2022 LTS version which might affect existing projects when you upgrade them from a 2021 version to 2022 LTS.
**Note** : 2022 LTS is also known as 2022.3.0.
### Page Outline
  * [Articulation Drive `forceLimit` property now accepts force input instead of impulse](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide2022LTS.html#artdrive)
  * [Change to generated lightmap UVs](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide2022LTS.html#lightmap)
  * [Change to `GradientField` in the UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide2022LTS.html#gradient)
  * [UI Toolkit Numeric and Compound fields are available at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide2022LTS.html#fields)
  * [The Physical Keys option in Input Manager is enabled by default](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide2022LTS.html#keys)
  * [Added support for `BatchRendererGroup`](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide2022LTS.html#batch)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide2022LTS.html#ren-pipe)A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline)
  * [Enlighten Baked Global Illumination is deprecated](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide2022LTS.html#baked-gi)
  * [Minimum Bounces isn’t available in the Lighting window](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide2022LTS.html#minbounce)
  * [Unity’s default Gradle templates have changed](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide2022LTS.html#default-gradle)
  * [Navigation and Pathfinding is moving from the Unity core to the AI Navigation package](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide2022LTS.html#nav+pathfinding)


## Articulation Drive `forceLimit` property now accepts force input instead of impulse
The Articulation Drive `forceLimit` feature was used previously as an impulse limit instead of a force limit. This made the force limit dependent on the `fixedDeltaTime` value.
If you have already adapted to the use of this value as an impulse, when you upgrade, your values for `forceLimit` in your Articulation Drive in the Articulation Body component will be incorrect by a large scale.
There are checks for when you open an older project. When you upgrade a project, Unity automatically divides the relevant values by the `Time.fixedDeltaTime` set in the **ProjectSettings** > **Time** page to avoid the incorrect configuration. This catches most cases where robots are simulated based on the project set Time value.
If you use custom time values from script to simulate your robots, then you need to manually correct these values.
## Change to generated lightmap UVs
Unity’s UV generation procedure has changed. **Lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) might appear corrupted in projects that use the [Generate Lightmap UVs option](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUvs-GeneratingLightmappingUVs.html) in Model Import Settings. To resolve this problem, rebake all of the lightmaps in your project.
This change only affects projects that use Generate Lightmap UVs.
## Change to `GradientField` in the UI Toolkit
From Unity 2022.1, the color picker in `GradientField` doesn’t have **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) enabled by default. Existing projects that use `GradientField` now use a regular color picker instead of the HDR color picker.
To continue the use of a HDR color picker, you can enable it using the HDR property in `GradientField`.
## UI Toolkit Numeric and Compound fields are available at runtime
The following fields are now available that work automatically at runtime:
  * `DoubleField`
  * `FloatField`
  * `IntegerField`
  * `LongField`
  * `Hash128Field`
  * `RectField`
  * `RectIntField`
  * `Vector2Field`
  * `Vector3Field`
  * `Vector4Field`
  * `Vector2IntField`
  * `Vector3IntField`
  * `BoundsField`
  * `BoundsIntField`


The UXML files in your projects don’t update and work upon upgrading. However, when you add new promoted types through the UI Builder, it breaks the backwards compatibility of UXML assets with older Unity versions. To keep the UXML assets backwards compatible, you need to use the old types (`UnityEditor.UIElements` namespace) in UXML files.
## The Physical Keys option in Input Managed is enabled by default
The Physical keys option allows you to map key codes to the physical keyboard layout, rather than to the language-specific layout that may vary between users in different regions. For example, on some keyboards the first row of letters reads “QWERTY”, and on others it reads “AZERTY”. This means if you scripted specific controls to use the well known “WASD” keys for movement, they would not be in the correct physical arrangement (like the arrow-key arrangement) on an AZERTY-layout keyboard. With Physical Keys enabled, Unity uses a generic ANSI/ISO “Qwerty” layout to represent the physical location of the keys regardless of the user’s actual layout. This means if you specify the “Q” key, it will always be the left-most letter on the first row of letter keys, even if the user’s keyboard has a different letter in that position.
As of 2022.1 the option is enabled by default with intent of deprecating and removing old behavior in the future.
## Added support for `BatchRendererGroup`
The `BatchRendererGroup` API was originally written for the MegaCity demo but was never fully documented or usable without a lot of implementation details. This API has been rewritten from the ground up and is fully documented and supported.
For information on how to use the new interface, refer to the [BatchRendererGroup](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group.html) page.
## Render pipelines
This upgrade guide describes how to upgrade to version 2022.2 of Unity’s built-in render pipeline. 
To upgrade to other render pipelines to version 2022.2, refer to the documentation for the render pipeline you’re using:
  * [The URP upgrade guide](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-2022-2.html)
  * [The HDRP upgrade guide](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@14.0/manual/Upgrading-from-2022.1-to-2022.2.html)


To upgrade other packages, refer to the documentation for the packages you are using.
## Enlighten Baked Global Illumination is deprecated
The **Enlighten** A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Enlighten) Baked **Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination) lightmapping backend is no longer available by default. When you upgrade a project to this version, Unity removes the Enlighten baking backend from the **lightmapper** A tool in Unity that bakes lightmaps according to the arrangement of lights and geometry in your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmapper) selection dropdown and substitutes a Progressive Lightmapper in every **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) where you’ve selected the Enlighten baking backend. 
On Apple silicon devices, Unity substitutes the Progressive GPU Lightmapper for the Enlighten baking backend. On all other devices, Unity selects the CPU Progressive Lightmapper.
To continue using the Enlighten baking back end, open **Edit** > **Project Settings** > **Editor** and in the **Graphics** section of that menu, activate **Enable Enlighten for Baked GI (Legacy)**. However, this option isn’t available in 2023.1 and later.
## Minimum Bounces is not available in the Lighting window
The Minimum Bounces property of the [Progressive Lightmapper](https://docs.unity3d.com/6000.0/Documentation/Manual/progressive-lightmapper.html) is no longer available in the Lighting window.
When you upgrade a project to 2022.2, Unity resets the Minimum Bounces value to 2, the recommended number of minimum bounces for lightmapping. To change this value, edit the LightingSettings API property [minBounces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-minBounces.html).
## Unity’s default Gradle templates have changed
In 2022.2, Unity updated the default versions of all tools used by Android. The new versions are as follows:
**Tool** | **Version** |   
---|---|---  
SDK |  |   
| Cmdline-tools component | version 6.0  
| Build-tools component version | 32.0.0  
| Platform-tools component | 32.0.0  
| Platform (API level) | 31 and 32 added by default  
| Tools component | Removed  
NDK | r23b |   
JDK (OpenJDK) | 11.0.14.1+1 |   
**Gradle** An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gradle) | 7.2 |   
Android Gradle Plugin | 7.1.2 |   
The update to Gradle version 7.2 changed some [build.gradle](https://developer.android.com/studio/build#build-files) file configuration options. This required significant changes to Unity’s default [gradle templates](https://docs.unity3d.com/6000.0/Documentation/Manual/gradle-templates.html). Unity won’t attempt to upgrade custom Gradle templates to match the new format which means projects that contain custom template files might fail to build. To solve this, recreate any custom template files based on the new default template files.
For information about the `build.gradle` configuration option changes, refer to the [Android Gradle Plugin release notes](https://developer.android.com/studio/releases/gradle-plugin).
## Navigation and Pathfinding is moving from the Unity core to the AI Navigation package
The package documentation is located here: https://docs.unity3d.com/Packages/com.unity.ai.navigation@latest 
If you have projects that were created with the Navigation feature in previous versions of the Unity engine you can do one of the following:
  * Continue to use your projects as they are
  * Convert your projects to use the new package


In either case, the **AI Navigation** package is automatically installed and added to your project.
To start using the new package you need to convert your project as follows:
  1. Go to **Window > AI > NavMesh Updater**.
  2. In the **NavMesh** A mesh that Unity generates to approximate the walkable areas and obstacles in your environment for path finding and AI-controlled navigation. [More info](https://docs.unity3d.com/Packages/com.unity.ai.navigation@latest/index.html?subfolder=/manual/NavInnerWorkings.html%23walkable-areas)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#NavMesh) Updater window, select which kind of data to convert.
  3. Click **Initialize Converters** to detect and display the types of data you selected.
  4. Select the data to be converted.
  5. Click **Convert Assets** to complete the conversion.


As part of the conversion process, the **NavMesh Updater** makes the following changes: 
  * Any NavMesh that was previously baked and embedded in the scene is now referenced from a NavMeshSurface component created on a new **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) called **Navigation**.
  * Any object that was marked with Navigation Static will now have a NavMeshModifier component with the appropriate settings.


If the NavMeshes in different scenes are baked with different agent settings then you need to create new Agent types to match those settings. To create the Agent types do the following: 
  1. Go to **Window > AI > Navigation**.
  2. Select **Agents**.
  3. Create new entries and specify the relevant settings.


When you have created the new entries you then need to do the following:
  * Assign the newly created agent types to their respective NavMeshSurfaces in the **Navigation** created for that scene,
  * Assign the agent types to the NavMeshAgents intended to use that NavMesh.


To find the settings that were used for each existing NavMesh, select the NavMesh .asset file in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow). The NavMesh settings is displayed in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
If your project uses the `NavMeshSurface`, `NavMeshModifier`, `NavMeshModifierVolume` or `NavMeshLink` components defined by **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) downloaded from [Unity’s NavMeshComponents GitHub repository ](https://github.com/Unity-Technologies/NavMeshComponents), then remove those scripts and any associated files before you add the **AI Navigation** package to your project. If you don’t remove these scripts, you might get conflicts and errors related to these components in the Console. The new components mirror the same behavior as the old components do in your project except when using the following components:
  * The `NavMeshSurface` component now includes an option to use only the objects that have a `NavMeshModifier` in the baking process.
  * You can now specify whether or not to apply the `NavMeshModifier` component to child objects in the hierarchy.


## Additional resources
  * [Install Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/GettingStartedInstallingUnity.html)
  * [API updater](https://docs.unity3d.com/6000.0/Documentation/Manual/APIUpdater.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide20231.html)
Upgrade to Unity 2023.1
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide2021LTS.html)
Upgrade to Unity 2021 LTS

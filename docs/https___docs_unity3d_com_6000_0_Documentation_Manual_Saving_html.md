* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Saving.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * Save your work


[](https://docs.unity3d.com/6000.0/Documentation/Manual/CustomizingYourWorkspace.html)
Customizing your workspace
[](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorFeatures.html)
Editor Features
# Save your work
Unity categorizes most saved information into either [scene changes](https://docs.unity3d.com/6000.0/Documentation/Manual/Saving.html#SceneChanges) or [project-wide changes](https://docs.unity3d.com/6000.0/Documentation/Manual/Saving.html#ProjectWideChanges).
  * To save all current scene and project-wide changes, go to **File** > **Save** (or **Save as**).
  * To save Project-wide changes, but not Scene changes, go to **File** > **Save Project**.


**Note** : If you edit in [Prefab Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingInPrefabMode.html), saving through **File** > **Save** only saves changes to the open Prefab. Exit the Prefab Mode to save wider changes.
Unity saves some information automatically while you work in the Editor. See [Automatic saves](https://docs.unity3d.com/6000.0/Documentation/Manual/Saving.html#ImmediateSaving) for more details.
## Scene changes 
Scene changes include modifications to **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). For example:
  * If you add, move, or delete a GameObject.
  * If you change a GameObject’s parameters in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window.


## Project-wide changes 
Project-wide changes in Unity apply to your entire project rather than a specific scene. For example, if you create a temporary scene to test changes, you can save the project and not the scene.
Project-wide changes include:
  * ****Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings)**: When you save your project, Unity saves changes to the Project Settings in the `ProjectSettings` folder, in these files:
    * **Input** : `InputManager.asset`
    * **Tags And Layers** : `TagManager.asset`
    * **Audio** : `AudioManager.asset`
    * **Time** : `TimeManager.asset`
    * **Player** : `ProjectSettings.asset`
    * **Physics** : `DynamicsManager.asset`
    * **Physics 2D** : `Physics2DSettings.asset`
    * **Quality** : `QualitySettings.asset`
    * **Graphics** : `GraphicsSettings.asset`
    * **Network** : `NetworkManager.asset`
    * **Editor** : `EditorUserSettings.asset`
  * ****Build Profiles** A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile)**: Unity saves changes to platform profiles and build profiles in the `Library` folder as assets. For more information, refer to [Introduction to build profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html).
  * **Changed assets** : When you save project-wide settings, Unity saves any unsaved assets.
**Note:** Some asset types have an **Apply** button in the Inspector. Unity will not save these unless you select **Apply**.
  * **Dirty assets** : Unity saves **Dirty** assets, which are files on your disk that are modified in the software but not saved yet. You can use [custom Editors](https://docs.unity3d.com/6000.0/Documentation/Manual/editor-CustomEditors.html) and [scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) to mark an Asset as dirty in one of these ways:
    * Use the [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) class with [SerializedProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).
    * Use the [Undo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.html) class to record modifications.
    * Use [SetDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SetDirty.html).


## Automatic saves 
Unity automatically saves the following changes to your disk:
  * **New assets** : Unity automatically saves new assets when you create them but you need to save later changes.
  * **Asset Import Settings** : For the changes to take effect with most assets, you need to select **Apply** in the Inspector window. Unity saves the changes when you select **Apply**.
  * **Baked data** : When you have data that is set to Baked in your project, Unity saves this data after the bake finishes. This includes: 
    * Baked Lighting data
    * Baked navigation data
    * Baked **occlusion culling** A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Occlusionculling) data
  * **Script execution order changes** : After you select **Apply** , Unity saves this data into each script’s `.meta` file.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CustomizingYourWorkspace.html)
Customizing your workspace
[](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorFeatures.html)
Editor Features

* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/presets-creating-using.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Reusing settings with preset assets](https://docs.unity3d.com/6000.0/Documentation/Manual/Presets.html)
  * Create presets to save and reuse settings


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Presets.html)
Reusing settings with preset assets
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SupportingPresets.html)
Supporting presets for custom types
# Create presets to save and reuse settings
Presets are assets used to save and reuse settings configurations from Unity Editor windows. Presets help you avoid having to manually configure the same settings repeatedly. You can save the property configuration of a component, asset, or [Project Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings) window and then apply that configuration in other instances of the same context.
For example, you can edit the properties of a **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) component, save these settings to a preset asset, then apply that preset asset to Rigidbody components in other **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). The preset applies only to the Rigidbody component and doesn’t affect other components.
You can store presets in the `Assets` folder of your project. Use the [Project](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html) window to view and select presets to edit in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
![Example of Preset assets in the Project window, organized in a Presets subfolder](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/preset-assets.png) Example of Preset assets in the Project window, organized in a Presets subfolder
## Save settings to a new preset
To save configured settings, create a new preset asset for them as follows:
  1. Identify the asset or settings group you want to save as a preset: 
     * **For GameObjects** : Select a GameObject in the **Hierarchy** window to open its properties in the **Inspector** window.
     * **For assets** : Select an asset in the **Project** window to open its import settings in the **Inspector** window.
     * **For Project Settings** : From the main menu, go to **Edit > Project Settings** and select the settings group you want to save as a preset.
  2. Configure the properties in the **Inspector** or **Project Settings** window.
  3. Click the preset selector (the slider icon) at the top-right corner of the window.   
![The Preset slider icon on a Transform component in the Inspector window.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/preset-icon.png)
  4. In the **Select Preset** window, click **Create New**. A File Save dialog appears.
  5. Choose a location for your new preset, enter its name, and click **Save**.


**Note** : Preset support and the preset selector are only available for certain **Project Settings** windows.
## Edit saved settings in an existing preset
To edit the saved settings in an existing preset, select the preset asset from the **Project** window and edit its properties in the **Inspector** window.
**Note:** When you change the properties in a preset, your changes don’t affect items you’ve already applied the preset to. For example, if you apply a preset for a Rigidbody component to a GameObject, and then edit the preset, the settings in the Rigidbody component don’t change.
![Editing a preset in the Inspector window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/preset-edit-preset.png) Editing a preset in the Inspector window
## Apply settings from a preset
There are two ways to apply a preset:
  * Via the **Select Preset** window.
  * For component presets, you can drag a preset from the **Project** window onto a GameObject that contains the component type.


**Note:** Applying a preset copies properties from the preset to the item. It doesn’t link the preset to the item. Changes you make to the preset don’t affect the items you have previously applied the preset to.
To apply a preset via the **Select Preset** window:
  1. Select the GameObject, Asset import settings, or **Project Settings** window to which you want to apply the preset.
For GameObjects, select a GameObject in the **Project** window to open its properties for editing in the **Inspector** window.
For assets, select an asset in the **Project** window to open its import settings for editing in the **Inspector** window.
For project settings, from the main menu go to **Edit > Project Settings** and select the settings group you want to save as a preset.
  2. In the **Inspector** or **Project Settings** window, click the preset selector (the slider icon) at the top-right of the window.
  3. In the **Select Preset** window, search for and select the preset to apply.
Unity applies this preset to the component, asset, or Project Settings window.
  4. Close the **Select Preset** window.


If you apply a component preset via drag-and-drop, Unity’s behavior depends on the state of your GameObject:
  * If you drop the preset on an existing GameObject in the Hierarchy window, Unity adds a new component and copies properties from the preset.
  * If you drop the preset on an empty area in the Hierarchy window, Unity creates a new, empty GameObject and adds a component with properties copied from the preset.
  * If you drop the preset on the **Inspector** window onto the title of an existing component, Unity copies properties from the preset.
  * If you drop the preset on an empty area in the **Inspector** window, Unity adds a new component and copies properties from the preset.


### Partially apply settings from a preset
You can choose to only apply some properties from a preset and exclude others. To do this:
  1. Select your preset in the **Project** In Unity, you use a project to design and develop a game. A project stores all of the files that are related to a game, such as the asset and Scene files. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/2Dor3D.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Project) window.
  2. In the **Inspector** , right-click a property and choose **Exclude Property**. The window displays a red horizontal line next to excluded properties.  
![The Inspector window for a Preset asset displays a red line next to a property excluded from the preset.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/preset-exclude-property.png)
  3. [Apply the preset](https://docs.unity3d.com/6000.0/Documentation/Manual/presets-creating-using.html#apply-preset) to the target component, asset, or Project Settings.


**Note:** To select all or clear all checkboxes in a preset, select the **More items** menu (**⋮**) or right-click the preset name, and select **Include all properties** or **Exclude all properties**. You can still adjust individual properties if you need to.
You can also use the Exclude option for presets that you then set as the default configuration for components and asset importers. For more information, refer to [Preset Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PresetManager.html).
### Applying presets based on asset location
You can write code to apply a preset to an asset based on the asset’s location in your project folder structure. For more information, refer to [Applying default presets to assets by folder](https://docs.unity3d.com/6000.0/Documentation/Manual/DefaultPresetsByFolder.html).
## Export preset assets
To share saved settings across projects and team members, you can export presets as an **asset package** A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Assetpackage) that other team members can [import](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackagesImport.html). For more information and instructions for how to export preset assets, refer to [Create and export asset packages](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackagesCreate.html).
## Using presets for transitions of Animation State nodes
You can save and apply presets for [Animation state](https://docs.unity3d.com/6000.0/Documentation/Manual/class-State.html) nodes. However, the [transitions](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transition.html)The blend from one state to another in a state machine, such as transitioning a character from a walk to a jog animation. Transitions define how long the blend between states should take, and the conditions that activate the blend. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transition.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Transition) in the preset are shared among presets and the nodes that you apply the preset to. For example, you apply a preset to two different nodes in the [Animator window](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorWindow.html)The window where the Animator Controller is visualized and edited. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorWindow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorWindow). In the **Inspector** window, you edit the settings for one of the transitions in the first node. Your change also appears in the other node and in the preset.
## Additional resources
  * [Supporting presets for custom types](https://docs.unity3d.com/6000.0/Documentation/Manual/SupportingPresets.html)
  * [Applying default presets to assets by folder](https://docs.unity3d.com/6000.0/Documentation/Manual/DefaultPresetsByFolder.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Presets.html)
Reusing settings with preset assets
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SupportingPresets.html)
Supporting presets for custom types

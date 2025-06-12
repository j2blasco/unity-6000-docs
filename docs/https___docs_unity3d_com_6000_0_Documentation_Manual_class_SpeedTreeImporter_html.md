* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-SpeedTreeImporter.html

  * [World building](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingEnvironments.html)
  * [Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/script-Terrain.html)
  * [Trees](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Trees-Landing.html)
  * [Import trees from SpeedTree](https://docs.unity3d.com/6000.0/Documentation/Manual/SpeedTree-landing.html)
  * SpeedTree Import Settings window


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SpeedTree.html)
SpeedTree model import
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SpeedTreeImporter-Model.html)
SpeedTree Model tab reference
# SpeedTree Import Settings window
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter.html "Go to SpeedTreeImporter page in the Scripting Reference")
When you put SpeedTree files in your Unity project’s Assets folder, Unity automatically imports and stores them as Unity assets. To view the import settings in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), select the file in the **Project** In Unity, you use a project to design and develop a game. A project stores all of the files that are related to a game, such as the asset and Scene files. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/2Dor3D.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Project) window. To customize how Unity imports the selected file, use the properties on the **Model** and **Materials** tabs on this window. SpeedTree 9 assets imported as .st9 files also have a **Wind** tab.
**Note:** These settings are for importing models created in [SpeedTree](https://docs.unity3d.com/6000.0/Documentation/Manual/SpeedTree.html). For information on models and animation created in other 3D modeling applications, see the [Model Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-FBXImporter.html) window.
![The SpeedTree Import Settings window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/class-SpeedTreeImporter.png) The SpeedTree Import Settings window
Unity recognizes and imports SpeedTree model assets in the same way it handles other assets. If you’re using SpeedTree Modeler 7, re-save your .spm files using the Unity version of the Modeler. If you’re using SpeedTree Modeler 8 or 9, save your .st or .st9 files directly into the Unity project folder. The SpeedTree Importer generates a **prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) with the [LOD Group](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html)A component to manage level of detail (LOD) for GameObjects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LODGroup) component configured. You can instantiate the prefab in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) as a common prefab instance or select the prefab as a tree prototype and paint it across the **terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain).
Materials come embedded in the imported SpeedTree model as sub-assets. If you want to make adjustments to the materials, you can extract them to a location of your choice or re-use existing materials with Material Remapping.
**Topic** | **Description**  
---|---  
**[Model tab](https://docs.unity3d.com/6000.0/Documentation/Manual/SpeedTreeImporter-Model.html)** | Understand the options in the Model tab of the SpeedTree Import Settings window.  
**[Materials tab](https://docs.unity3d.com/6000.0/Documentation/Manual/SpeedTreeImporter-Materials.html)** | Understand the options in the Materials tab of the SpeedTree Import Settings window.  
**[Wind tab](https://docs.unity3d.com/6000.0/Documentation/Manual/SpeedTreeImporter-Wind.html)** | Understand the wind options for SpeedTree 9 assets imported as .st9 files.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SpeedTree.html)
SpeedTree model import
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SpeedTreeImporter-Model.html)
SpeedTree Model tab reference

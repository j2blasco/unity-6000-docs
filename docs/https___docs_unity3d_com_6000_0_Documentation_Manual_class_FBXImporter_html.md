* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-FBXImporter.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Models](https://docs.unity3d.com/6000.0/Documentation/Manual/models.html)
  * [Importing models into Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/models-importing.html)
  * Model Import Settings reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/GenericAnimations.html)
Importing a model with non-humanoid (generic) animations
[](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Model.html)
Model tab Import Settings reference
# Model Import Settings reference
To open a model’s Import Settings, select the model from the [Project window](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow). The [Inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) then displays the Import Settings for the selected model.
![The Import Settings window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/model-import-settings.png) The Import Settings window
**Note:** These settings are for importing models and animations created in most 3D modeling applications. However, models created in SketchUp and SpeedTree use specialized settings. For more information, refer to [SketchUp Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SketchUpImporter.html), and [SpeedTree Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SpeedTreeImporter.html). 
You can customize how Unity imports the selected file by setting the properties in the following tabs:
## Model
Contains settings for 3D models, which can represent a character, a building, or a piece of furniture. In these cases, Unity creates multiple assets from a single **model file** A file containing a 3D data, which may include definitions for meshes, bones, animation, materials and textures. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/3D-formats.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Modelfile). In the Project window, the main imported object is a model [prefab](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab). Usually there are also several **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) objects that the model prefab references. 
For more information, refer to [Model Import Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Model.html).
## Rig
Contains settings for rigs (sometimes called skeletons). A rig includes a set of deformers arranged in a hierarchy that animate a mesh (sometimes called skin) on one or more models created in a 3D modeling application such as Autodesk 3ds Max or Autodesk Maya. For humanoid and generic (non-humanoid) models, Unity creates an **avatar** An interface for retargeting animation from one rig to another. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Avatar) to reconcile the imported rig with the Unity **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). 
For more information, refer to [Rig Import Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Rig.html).
## Animation
Contains settings for animation clips. You can define any series of different poses that happen over a set of frames, such as walking, running, or idling as an **animation clip** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip). You can reuse clips for any model that has an identical rig. Often a single file contains several different actions, each of which you can define as a specific animation clip. 
For more information, refer to [Animation Import Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html).
## Materials
Contains settings for the materials and textures in your model. You can extract materials and textures or leave them embedded within the model. You can also adjust how materials are mapped in the model. 
For more information, refer to [Materials Import Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Materials.html).
## Additional resources
  * [Model import workflows](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingModelFiles.html)
  * [Model file formats](https://docs.unity3d.com/6000.0/Documentation/Manual/3D-formats.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GenericAnimations.html)
Importing a model with non-humanoid (generic) animations
[](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Model.html)
Model tab Import Settings reference

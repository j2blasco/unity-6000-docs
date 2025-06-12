* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingModelFiles.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Models](https://docs.unity3d.com/6000.0/Documentation/Manual/models.html)
  * [Importing models into Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/models-importing.html)
  * Importing a model


[](https://docs.unity3d.com/6000.0/Documentation/Manual/models-importing.html)
Importing models into Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)
Importing a model with humanoid animations
# Importing a model
Model files can contain a variety of data, such as meshes, animation rigs and clips, materials, and textures. 
Unity’s primary support for **model files** A file containing a 3D data, which may include definitions for meshes, bones, animation, materials and textures. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/3D-formats.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Modelfile) is the FBX format. However, you can save your 3D files from most common 3D modeling software in [their native format](https://docs.unity3d.com/6000.0/Documentation/Manual/HOWTO-ImportObjectsFrom3DApps.html) (for example, .max, .blend, .mb, .ma). When Unity finds these file types in your `Assets` folder, it calls your 3D modeling software’s FBX export **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in), and imports the file. The 3D modeling software must be installed on the same computer as Unity, so in most cases it’s best practice to directly export as FBX from your application into your `Assets` folder.
## Adjusting model settings
To open a model’s Import Settings, select the model from the [Project window](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow). The [Inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) then displays the Import Settings for the selected model.
![The Import Settings window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/model-import-settings.png) The Import Settings window
**Note:** A SpeedTree model has different importing settings. For more information, refer to [SpeedTree Model tab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SpeedTreeImporter-Model.html).
## Rig and animation settings
If your file contains animation data, you can set up the rig with the [Rig tab](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Rig.html) and then extract or define **Animation Clips** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) with the [Animation tab](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html). The workflow differs between humanoid and generic animation types because Unity needs the humanoid’s bone structure to be specific, but only needs to know which bone is the **root node** A transform in an animation hierarchy that allows Unity to establish consistency between Animation clips for a generic model. It also enables Unity to properly blend between Animations that have not been authored “in place” (that is, where the whole Model moves its world position while animating). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationRootMotionNodeOnImportedClips.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rootnode) for the generic type. For more information, refer to [Importing a model with humanoid animations](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html) and [Importing a model with non-humanoid (generic) animations](https://docs.unity3d.com/6000.0/Documentation/Manual/GenericAnimations.html).
## Importing materials
If your file contains materials and textures, you can define how you want to deal with them:
  1. Select a model file from the Project window.
  2. In the Inspector, select [the Materials tab](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Materials.html).
  3. Use the [Material Creation Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Materials.html) drop-down menu to choose how you want to import the materials from the FBX file.


## Importing textures
Unity follows a specific search pattern to automatically look for textures on import. First, the importer looks for a subfolder called `Textures` within the same folder as the **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh), or in any parent folder. If this fails, Unity performs an exhaustive search of all textures in the project. Although slightly slower, the main disadvantage of the exhaustive search is that there might be two or more textures in the project with the same name. In this case, it’s not guaranteed that Unity can find the right one.
## Importing normal maps
If you have a character with a [normal map](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterNormalMap.html)A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap) that was generated from a high-polygon version of the model, import the game-quality version with the [Smoothing Angle](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Model.html#geometry) property set to 180°. This prevents odd-looking seams in lighting due to tangent splitting. If the seams are still present with these settings, choose the [Calculate Legacy With Split Tangents](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Model.html#geometry) setting from the **Tangents** drop-down menu. If you’re converting a grayscale image into a normal map, you don’t need to do this.
## Importing blend shapes
Unity supports blend shapes (morphing) and can import blend shapes from FBX and DAE files exported from 3D modeling applications. You can also import animation from FBX files. Unity supports vertex-level animation for blend shapes on vertices, normals and tangents.
Skin and blend shapes can affect meshes at the same time. When Unity imports meshes containing blend shapes, it uses the [`SkinnedMeshRenderer`](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SkinnedMeshRenderer.html) component instead of the [`MeshRendere`r](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html) component, regardless of whether it has skin or not.
Unity imports blend shape animation as part of regular animation and animates blend shape weights on skinned **mesh renderers** A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer).
To import blend shapes with normals perform one of the following:
  * Use the normals from the FBX file. In the **Model** tab, set the [Blend Shape Normals](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Model.html#geometry) property to **Import**.
  * Use the same logic to calculate normals on a mesh and blend shapes. In the **Model** tab, set the [Blend Shape Normals](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Model.html#geometry) property to **Calculate**.


**Note:** If you want tangents on your blend shapes then set the [Tangents](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Model.html#geometry) import setting to **Calculate**.
## Importing visibility properties
Unity can read visibility properties from FBX files with the [Import Visibility](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Model.html#scene) property. Values and **animation curves** Allows you to add data to an imported clip so you can animate the timings of other items based on the state of an animator. For example, for a game set in icy conditions, you could use an extra animation curve to control the emission rate of a particle system to show the player’s condensing breath in the cold air. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationCurvesOnImportedClips.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationCurves) can enable or disable MeshRenderer components by controlling the [`Renderer.enabled`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-enabled.html) property.
Visibility inheritance is true by default but can be overridden. For example, if the visibility on a parent mesh is set to 0, all the renderers on its children are also disabled. In this case, one animation curve is created for each child’s `Renderer.enabled` property.
Some 3D modeling applications either don’t support or have limitations with visibility properties. For more information refer to [Support for proprietary model file formats](https://docs.unity3d.com/6000.0/Documentation/Manual/HOWTO-ImportObjectsFrom3DApps.html).
## Camera support
The following properties are supported when importing **cameras** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) from an FBX file:
**Property** | **Description**  
---|---  
**Projection** mode | Orthographic or perspective. Doesn’t support animation.  
**Field of View** | Supports animation.  
All **Physical Camera** properties | If you import a Camera with Physical Properties (for example, from Maya), Unity creates a Camera with the **Physical Camera** property enabled and the **Focal Length** , **Sensor Type** , **Sensor Size** , **Lens Shift** , and **Gate Fit** values from the FBX file.  
  
**Note:** Not all 3D modeling applications have a concept of **Gate Fit**. When not supported by the 3D modeling application, the default value in Unity is **None**.  
**Near** and **Far** **Clipping Plane** A plane that limits how far or close a camera can see from its current position. A camera’s viewable range is between the far and near clipping planes. See far clipping plane and near clipping plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#clippingplane) distance | Unity doesn’t import any animation on these properties. When exporting from 3ds Max, enable the **Clip Manually** setting; otherwise the default values are applied on import.  
**Target Cameras** | If you import a Target Camera, Unity creates a camera with a [LookAt](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LookAtConstraint.html) constraint using the target object as the source.  
For more information, refer to [Camera Inspector window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html).
## Light support
The following light types are supported:
  * Omni
  * Spot
  * Directional
  * Area


The following light properties are supported:
**Property** | **Description**  
---|---  
**Range** | The **FarAttenuationEndValue** is used if **UseFarAttenuation** is enabled. **FarAttenuationEndValue** does not support animation.  
**Color** | Supports animation.  
**Intensity** | Supports animation.  
**Spot Angle** | Supports animation. Only available for Spot Lights.  
**Note** : In 3ds Max, the exported default value is the value of the property at the current selected frame. To avoid confusion, move the playhead to frame 0 when exporting.
### Limitations
Some 3D modeling applications apply scaling on light properties. For instance, you can scale a spotlight by its hierarchy and affect the light cone. Unity doesn’t do this, which can cause lights to look different in Unity.
The FBX format doesn’t define the width and height of area lights. Some 3D modeling applications don’t have this property and only allow you to use scaling to define the rectangle or disc area. Because of this, area lights always have a size of 1 when imported.
Targeted light animations aren’t supported unless their animation is baked.
## Using a model file
To add a model file to your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) perform one of the following actions:
  * If the model contains a mesh, drag the file into the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) to instantiate it as a [prefab](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) for a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject).
  * If it contains Animation Clips, drag the file into [the Animator window](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorWindow.html) to use in [the State Machine](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBasics.html). You can also drag the animation directly onto an instantiated Prefab in the Scene view. This automatically creates an Animation Controller and connects the animation to the model.


## Additional resources
  * [Preparing humanoid models for export](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingHumanoidChars.html).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/models-importing.html)
Importing models into Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)
Importing a model with humanoid animations

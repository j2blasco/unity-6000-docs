* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-changedensity.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes.html)
  * Configure the size and density of Adaptive Probe Volumes


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-showandadjust.html)
Display Adaptive Probe Volumes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-usebakingsets.html)
Bake multiple scenes together with Baking Sets
# Configure the size and density of Adaptive Probe Volumes
Refer to [Understanding Adaptive Probe Volumes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-concept.html) for more information about how Adaptive Probe Volumes work.
## Change the size
To ensure the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) considers static geometry from all loaded scenes when it places **Light Probes** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe), set **Mode** to **Global** in the Adaptive Probe Volume **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window so the Adaptive Probe Volume covers the entire **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
You can also do one of the following in the Inspector of an Adaptive Probe Volume, to set the size of an Adaptive Probe Volume:
  * Set **Mode** to **Local** and set the size manually.
  * Set **Mode** to **Local** and select **Fit to all Scenes** , **Fit to Scene** , or **Fit to Selection**. Refer to [Adaptive Probe Volume Inspector reference](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-inspector-reference.html) for more information.
  * To exclude certain **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) when URP calculates Light Probe positions, enable **Override Renderer Filters**. For more information about Layers, refer to [Layers and Layer Masks](https://docs.unity3d.com/Manual/layers-and-layermasks.html).


You can use multiple Adaptive Probe Volumes in a single scene, and they can overlap. However in a Baking Set, URP creates only a single Light Probe structure. trouble
### Resize
To resize the Adaptive Probe Volume, use one of the handles of the box **gizmo** A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#GizmosIcons)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gizmo) in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView). You can’t resize an Adaptive Probe Volume by changing the **Transform component** A Transform component determines the Position, Rotation, and Scale of each object in the scene. Every GameObject has a Transform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TransformComponent) of the GameObject, or using the scale gizmo.
In this screenshot, a red box indicates the box gizmo handles.
![The resize handles for Adaptive Probe Volumes.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/probe-volumes/ProbeVolume-Size-gizmo.png)  

## Adjust Light Probe density
You might need to do the following in your project:
  * Increase Light Probe density in highly detailed scenes or areas such as interiors, to get a good lighting result.
  * Decrease Light Probe density in empty areas, to avoid those areas using disk space and increasing bake time unnecessarily.


In the [Inspector for an Adaptive Probe Volume](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-inspector-reference.html), enable and adjust **Override Probe Spacing** to set a minimum and maximum density for the Light Probes in the Adaptive Probe Volume.
The values can’t exceed the **Min Probe Spacing** or **Max Probe Spacing** values in the **Probe Placement** section of the [Adaptive Probe Volumes panel](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-lighting-panel-reference.html), so you might need to adjust these values first.
You can also add local Adaptive Probe Volumes in different areas with different **Override Probe Spacing** values, to control Light Probe density more granularly. For example, in empty areas, add a local Adaptive Probe Volume with a higher **Override Probe Spacing** minimum value, to make sure Light Probes have a lower density in those areas.
If you increase Light Probe density, you might increase bake time and how much disk space your Adaptive Probe Volume uses.
### Decrease Light Probe density for terrain
Because **terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) is detailed but less important than your main scenery or characters, you can do the following:
  1. Put terrain on its own [Layer](https://docs.unity3d.com/Manual/layers-and-layermasks.html)Layers in Unity can be used to selectively opt groups of GameObjects in or out of certain processes or calculations. This includes camera rendering, lighting, physics collisions, or custom calculations in your own code. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Layer).
  2. Surround the terrain with an Adaptive Probe Volume.
  3. In the Inspector for the Adaptive Probe Volume, enable **Override Renderer Filters** , then in ****Layer Mask** A value defining which layers to include or exclude from an operation, such as rendering, collision or your own code. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LayerMask)** select only your terrain Layer.
  4. To adjust Light Probe density to capture more or less lighting detail, enable **Override Probe Spacing** and adjust the values.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-showandadjust.html)
Display Adaptive Probe Volumes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-usebakingsets.html)
Bake multiple scenes together with Baking Sets

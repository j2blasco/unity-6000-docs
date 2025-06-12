* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html

  * [World building](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingEnvironments.html)
  * [Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/script-Terrain.html)
  * Terrain Settings reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Heightmaps.html)
Working with Heightmaps
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Runtime.html)
Using Terrain at runtime
# Terrain Settings reference
Each **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) tile has its own settings. If you’re using the built-in Terrain system, you need to change settings for each individual tile. If you’re using the [Terrain Tools package](https://docs.unity3d.com/Packages/com.unity.terrain-tools@5.1/manual/terrain-toolbox.html), you can change all tiles at once. 
**Tip:** When you create a new tile from an existing one, the new tile inherits most of the settings from its parent tile. 
To change the settings for a single terrain tile, in both the built-in Terrain system and the Terran Tools package:
  1. In the **Hierarchy** window, select the tile.
  2. In the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window, select **Terrain Settings** (gear icon).


## Basic Settings
**Property** | **Description**  
---|---  
**Grouping ID** | The ID the tile uses for **Auto connect**. Only tiles with the same grouping ID can connect.  
**Auto Connect** | Automatically connect to neighboring tiles that have the same **Grouping ID**.  
**Reconnect** | If you change the **Grouping ID** of a tile, or disable **Auto Connect** for one or more tiles, you might lose connections between tiles. To reconnect tiles, click the **Reconnect** button. **Reconnect** only connects two adjacent tiles if they have the same **Grouping ID** and if both tiles have **Auto Connect** enabled. This option isn’t available in the **Terrain Toolbox** window, which handles multiple tiles at once.  
**Draw** | Enable rendering the terrain. Drawing is enabled by default; disable it when you want to focus on other tiles while painting or in Play mode. The only element that isn’t drawn is the terrain’s height; trees, grass, and other details are still drawn. Note that disabling drawing doesn’t prevent actions on the tile. For example, height sculpting over the tile’s area still changes its height.  
**Draw Instanced** | Enable instanced rendering. For more information, refer to [Optimizing draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/optimizing-draw-calls.html).  
**Enable**Ray Tracing** The process of generating an image by tracing out rays from the Camera through each pixel and recording the color contribution at the hit point. This is an alternative to rasterization. raytracing  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Raytracing) Support** | Use ray tracing to draw the terrain. Ray tracing renders a more realistic terrain, but has an impact on performance. This option isn’t available in the **Terrain Toolbox** window, which handles multiple tiles at once.  
****Pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) Error** | Simplifies the generated terrain to optimize rendering. The lower the value, the more faithful the rendering to the original maps, such as the **heightmaps** A greyscale Texture that stores height data for an object. Each pixel stores the height difference perpendicular to the face that pixel represents.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Heightmap) and textures, and the higher the performance needs.  
**Minimum Detail Limit** | Higher levels increase the heightmap’s complexity. `0` means no limit on how simple the heightmap can be. **Minimum Detail Limit** and **Maximum Complexity Limit** have a combined value that is limited by **Heightmap Resolution** (refer to Texture Resolution below). Because of the limit of their combined value, they limit each other. This option isn’t available in the **Terrain Toolbox** window, which handles multiple tiles at once.  
**Maximum Complexity Limit** | Higher levels simplify the heightmap. `0` means no limit on how complex the heightmap can be. **Maximum Complexity Limit** and **Minimum Detail Limit** have a combined value that is limited by **Heightmap Resolution** (refer to Texture Resolution below). Because of the limit of their combined value, they limit each other. This option isn’t available in the **Terrain Toolbox** window, which handles multiple tiles at once.  
**Base Map Dist.** | The maximum distance to **render textures** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) in full resolution. Beyond this distance, a lower resolution composite image is used.  
## Cast shadows
Defines how the terrain casts shadows onto other objects. Shadow interactions with other objects rely on [Rendering.ShadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastingMode.html).
**Property** | **Description**  
---|---  
**Off** | The terrain doesn’t cast shadows.  
**On** | The terrain casts one sided shadows.  
**Two Sided** | The terrain casts a shadow from either side of a surface, ignoring backface culling.  
**Shadows Only** | Render only the terrain’s shadows, not the terrain itself.  
## Reflection probes
To control how terrain reflects its environment, set the blend options for adjacent **reflection probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe) and the **skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox). Reflection probes create more realistic reflections, but decrease performance. Global environment reflections are controlled from the [Lighting window](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html). You can override these reflections for a specific Terrain tile with the **Reflection Probes** setting. This setting only has an effect when you use the default material or a custom material with a **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) that supports rendering with reflections. For more information, refer to [Reflection Surface Shader examples in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples-Reflection.html). 
Note that HDRP doesn’t support skyboxes for environment reflections.
**Property** | **Description**  
---|---  
**Off** | Disable reflection probe blending and use only the skybox for reflection.  
**Blend Probes** | Blends only adjacent probes and ignores the skybox. Use this for indoors or overhung areas, such as caves, to prevent sky reflections.  
**Blend Probes And Skybox** | Works like **Blend Probes** , but also blends the skybox. Use this for open air areas, where the sky is always visible.  
**Simple** | Use reflection probes, but don’t blend adjacent ones.  
## Material
Replace the terrain’s default material. You can select a material you’ve created earlier, or duplicate the default material. Changes done to any material, including the default material, impact all Terrain tiles using that material. 
**Property** | **Description**  
---|---  
**Create** | Creates a new copy of the default material and applies it to the current tile. The new material opens in the Inspector window. The **Create** button is only available once for each tile; it’s removed from the interface after use.  
**Select Material** | Use a material you’ve created earlier. In the **Material** field, select the texture picker (circle).  
## Tree and Detail Objects
**Property** | **Description**  
---|---  
**Draw** | Enable rendering tress, grass, and details. Drawing is enabled by default; disable it when you want to focus on the topography.  
**Bake Light Probes For Trees** | Create internal [light probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) at the position of each tree, and use their information to render light. These probes don’t affect other renderers in the scene.  
  
If you don’t check this box, trees are still affected by [Light Probe Groups](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeGroup.html)A component that enables you to add Light Probes to GameObjects in your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbeGroup). This option is only effective for trees whose prototype has the **Mesh Renderer** > **Receive Global Illumination** > **Light Probe** property enabled (refer to [Mesh Renderer component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)).  
**Remove Light Probe Ringing** | Ringing is an unwanted light probe behaviour that can happen when there are different light intensities in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). It causes light to render where it shouldn’t, such as the dark side of an object. **Remove Light Probe Ringing** removes the ringing, but it also makes the probe less exact, and reduces light contrast. For more information, refer to [Light Probe Groups: Ringing](https://docs.unity3d.com/6000.0/Documentation/Manual/light-probes-troubleshooting.html#Ringing). This option is only available when you use **Bake Light Probes For Trees**.  
**Preserve Tree Prototype Layers** | For [ray casting](https://docs.unity3d.com/6000.0/Documentation/Manual/use-layers.html), let tree instances use the layer value of their prototype, instead of the Terrain **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject)’s layer value.  
**Detail Distance** | How far, in meters, an object ([Detail Mesh or Grass Texture](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Grass.html)) needs to be from the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) to be culled. If the distance is too short, a user moving through the scene might see the change from culling to visible as objects popping in or out of the frame.  
**Detail Density Scale** | A factor applied to the density of all details with the **Affected by Density Scaling** property enabled. `0` means no details; `1` means the full density defined for each detail. For more information, refer to [Paint meshes and grass](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Grass.html). This option isn’t available in the **Terrain Toolbox** window, which handles multiple tiles at once.  
**Tree Distance** | How far, in meters, a tree needs to be from the camera to be culled. If the distance is too short, a user moving through the scene might see the change from culling to visible as objects popping in or out of the frame. For SpeedTree trees, this property has no impact; use the tree’s **LOD** The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LOD) group.  
****Billboard** A textured 2D object that rotates so that it always faces the Camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Billboard) Start** | How far, in meters, a tree needs to be from the camera to change from a **3D object** A 3D GameObject such as a cube, terrain or ragdoll. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GameObjects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#3DObject) to a billboard. If the distance is too short, a user moving through the scene might see the trees change shape. For SpeedTree trees, this property has no impact; use the tree’s **LOD group** A component to manage level of detail (LOD) for GameObjects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LODGroup).  
**Fade Length** | The distance over which trees transition between 3D objects and billboards. A longer distance creates a slower transition, and a user moving through the scene might see the branches move from facing the camera (billboard) to their final 3D positions. For SpeedTree trees, this property has no impact; use the tree’s LOD group.  
**Max**Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Trees** | The maximum number of visible trees that can render as 3D meshes. Beyond this limit, trees are all billboards, even if they’re close enough to the camera to be 3D. The Editor prioritises the trees nearest the camera to be 3D. For SpeedTree trees, this property has no impact; use the tree’s LOD group.  
## Tree Motion Vectors
For the animation of trees moving in the wind: Set whether to use motion vectors. Motion vectors track each renderer’s per-pixel, screen-space motion from one frame to the next. You can use this information to apply post-prcessing effects.   
  
**Note:** Not all platforms support motion vectors. Refer to [SystemInfo.supportsMotionVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsMotionVectors.html) for more information.  
  
This property corresponds to the [Terrain.treeMotionVectorModeOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-treeMotionVectorModeOverride.html) method. This option isn’t available in the **Terrain Toolbox** window, which handles multiple tiles at once.
**Property** | **Description**  
---|---  
**Camera Motion Only** | Use only camera movement to track motion.  
**Per Object Motion** | Track motion when the camera moves, the GameObject moves, or both move.  
**Force No Motion** | Don’t track motion.  
**Inherit From Prototype** | Use the **Motion Vector** property setting of the tree prototype.  
## Detail Scatter Mode
How to cover an area with details (mesh or grass). This option isn’t available in the **Terrain Toolbox** window, which handles multiple tiles at once. 
**Property** | **Description**  
---|---  
**Coverage** | Paints based on the detail’s **Detail Density** value (refer to [Paint meshes and grass](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Grass.html)).  
**Instance Count** | Paints based on the **Detail Resolution** and **Detail Resolution Per Patch** values in the **Mesh Resolution** properties below.  
## Wind Settings for Grass
**Property** | **Description**  
---|---  
**Speed** | How quickly the wind moves the grass from side to side.  
**Size** | The size of ripples on grassy areas. Lower values create a uniform movement; higher values create waves of motion in different directions.  
**Bending** | How much the grass bends in the wind. `0` stops all movement. `1` moves the grass halfway towards the ground, but doesn’t lay it flat.  
**Grass Tint** | The color tint applied to all grass objects. The final color for each grass is the **Grass Tint** multiplied by the grass’s **Healthy Color** and **Dry Color** values, which you can set for each grass type individually (refer to [Paint meshes and grass](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Grass.html)).  
**Wind Settings for Grass** don’t impact trees. To animate tree movement, refer to [Animate trees with wind](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WindZone.html).
## Mesh Resolution
With all resolutions, higher values provide more detail but require more memory and processing power.
**Property** | **Description**  
---|---  
**Terrain Width** | The terrain tile’s x-axis value, in world units. The value range is from 1 to 100,000. Changing this value changes the size of anything already on the tile, such as sculpted hills.  
**Terrain Length** | The terrain tile’s z-axis value, in world units. The value range is from 1 to 100,000. Changing this value changes the size of anything already on the tile, such as sculpted hills.  
**Terrain Height** | The possible difference between the lowest and highest points in the heightmap (y-axis), in world units. The value range is from 1 to 10,000. You can’t use negative values; if you need to sculpt below the surface level of your world, raise the terrain’s starting point (refer to [Raise or lower Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-RaiseLowerTerrain.html)). Changing this value changes the size of anything already on the tile, such as sculpted hills.  
**Detail Resolution Per Patch** | The size in pixels of each detail patch, which is a part of the **Detail Resolution** map. A high value reduces draw calls, but might increase triangle count because detail patches are culled per batch. The recommended value is 16. If your **Detail Distance** is high and your grass is sparse, use a higher value. The range is from `8` to `128`, and the value is squared to form a grid.  
**Detail Resolution** | The number of pixels in the detail resolution map. A higher value gives more exact detail painting. The range is `0` to `4048`, and the value is squared to form a grid.  
## Holes Settings
**Compress Holes Texture** : Compress the texture used to paint holes to the `DXT1` format in the Player during runtime. This format is widely supported on PC and console platforms. For more information, refer to [TextureFormat.DXT1](https://docs.unity3d.com/ScriptReference/TextureFormat.DXT1.html) and [Paint holes in the terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-PaintHoles.html).
This option isn’t available in the **Terrain Toolbox** window.
## Texture Resolutions
With all resolutions, higher values provide more detail but require more memory and processing power.
**Property** | **Description**  
---|---  
**Heightmap Resolution** | The pixel resolution of the terrain tile’s heightmap. The higher the resolution, the more detail the terrain contours can include. This value must be a power of two plus one, for example, 513, which is 512 + 1. Changing this value changes the possible values of **Minimum Detail Limit** and **Maximum Complexity Limit** : their combined value is the power of the resolution minus 4. If **Heightmap Resolution** is `33 x 33`, **Minimum Detail Limit** and **Maximum Complexity Limit** is locked at `0`.  
**Control Texture Resolution** | The resolution of the splatmap that controls the blending of the different Terrain Textures.  
**Base Texture Resolution** | The resolution of the composite texture the terrain uses when you view it from a distance greater than the [Basemap Distance](https://docs.unity3d.com/ScriptReference/Terrain-basemapDistance.html) (you can set a basemap distance for all terrain tiles in **Project Settings** > **Quality** > **Terrain Setting Overrides**).  
The **Require resampling on change** banner reminds you that when you change properties under **Texture Resolutions** , the Unity Editor resizes the tile’s content to the new size you specify. This can affect the quality of your content.
### Heightmap Import and Export
You can import heightmaps to use in your project, or export your existing heightmap. This option isn’t available in the **Terrain Toolbox** window, because you can’t export multiple tiles at once.
The heightmap is an image file in the RAW grayscale format. 
For more information, refer to [Import and export heightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Heightmaps.html).
## Lighting
These options aren’t available in the **Terrain Toolbox** window, which handles multiple tiles at once.
**Property** | **Description**  
---|---  
**Contribute**Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination)** | Use the Terrain in Global Illumination computations. When you enable this property, **Lightmapping** properties become available.  
**Receive Global Illumination** | Use **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) or light probes as illumination sources. If you disable **Contribute Global Illumination** , select **Light Probes** in this list. If you enable **Contribute Global Illumination** , you can select **Lightmaps**. The Lightmapping options are available only if you enable **Contribute Global Illumination** in the **Lighting** section, and select **Lightmaps** from the **Receive Global Illumination** dropdown.  
## Lightmapping
These options aren’t available in the **Terrain Toolbox** window, which handles multiple tiles at once.
These options are available only if you enable **Contribute Global Illumination** in the **Lighting** section, and select **Lightmaps** from the **Receive Global Illumination** dropdown.
**Property** | **Description**  
---|---  
**Scale in Lightmap** | Specify the relative size of an object’s [UV tile within a lightmap](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUvs.html). A value greater than `1.0` increases the number of pixels (the lightmap resolution) used, and creates more exact lighting for important or detailed areas. A value smalle than `1.0` decreases the number of pixels and is better for areas with fewer details. Set the value to `0` to let the object contribute lighting to other objects in the scene without being lightmapped itself.  
**Lightmap Parameters** | Choose or create a Lightmap Parameters asset for the tile. Refer to [Lightmap Parameters](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightmapParameters.html) for more information.  
**Rendering**Layer Mask** A value defining which layers to include or exclude from an operation, such as rendering, collision or your own code. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LayerMask)** | For the scriptable **render pipelines** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), set the rendering layer for this Terrain tile. For more information, refer to [Rendering Layers in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-layers.html) or [Renderings Layer in HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@16.0/manual/Rendering-Layers).  
## Quality Settings
**Ignore Quality Settings** : Set the tile to ignore the Terrain Override Settings set in the [Quality settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#Terrain).
This option isn’t available in the **Terrain Toolbox** window, which handles multiple tiles at once.
## Terrain Collider
The Terrain **Collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) component manages **collisions** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) on the terrain. For details about the **Terrain Collider** A terrain-shaped collider component that handles collisions for collision surface with the same shape as the Terrain object it is attached to. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TerrainCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TerrainCollider) component properties, refer to [Terrain Collider component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TerrainCollider.html).
You can’t set a collider in the **Terrain Toolbox** window. You have to set them for each tile.
## Additional resources
  * [Terrain Collider component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TerrainCollider.html)
  * [Import and export heightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Heightmaps.html)
  * [Mesh Renderer component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Heightmaps.html)
Working with Heightmaps
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Runtime.html)
Using Terrain at runtime

* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/2d-renderer-sorting.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * 2D renderer sorting


[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-game-art-syle-reference.html)
2D game art style reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)
Sprites
# 2D renderer sorting
## Overview
Unity sorts Renderers according to a priority order that depends on their types and usages. You can specify the render order of Renderers through their [Render Queue](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShaderTags.html). In general, there are two main queues: the [Opaque queue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderQueue.Geometry.html) and the [Transparent queue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderQueue.Transparent.html). 2D Renderers are mainly within the Transparent queue, and include the [Sprite Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/renderer/renderer-landing.html)A component that lets you display images as Sprites for use in both 2D and 3D scenes. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/renderer/renderer-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SpriteRenderer), [Tilemap Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-renderer-reference.html), and [Sprite Shape Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/shape-renderer/shape-renderer-landing.html) types.
## Transparent Queue Sorting Order by Priority
2D Renderers within the Transparent Queue generally follow the priority order below:
  1. [Sorting Layer and Order in Layer](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-renderer-sorting.html#sortlayer)
  2. [Specify Render Queue](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-renderer-sorting.html#renderqueue)
  3. [Distance to Camera](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-renderer-sorting.html#cameradistance)
     * [Perspective](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-renderer-sorting.html#persp)
     * [Orthographic](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-renderer-sorting.html#ortho)
     * [Custom Axis sort mode](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-renderer-sorting.html#customaxis)
     * [Sprite Sort Point](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-renderer-sorting.html#sortpoint)
  4. [Sorting Group](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-renderer-sorting.html#sortgroup)
  5. [Material/Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-renderer-sorting.html#material)
  6. [Tiebreaker](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-renderer-sorting.html#tiebreak)


There are other factors which can cause the sorting order to differ from the regular priority order. These factors vary from project to project.
## Sorting Layer and Order in Layer
The [Sorting Layer](https://docs.unity3d.com/Manual/class-TagManager.html#SortingLayers) and **Order in Layer** (in the Renderer’s **Property** settings) are available to all 2D Renderers through the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window or via the Unity Scripting API. Set the Renderer to an existing **Sorting Layer** or create a new one to determine its priority in the rendering queue. Change the value of the **Order in Layer** to set the Renderer’s priority among other Renderers within the same **Sorting Layer**.
## Specify Render Queue
You can specify the Render Queue type of the Renderer in its Material settings or in the **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) settings of its Material. This is useful for grouping and sorting Renderers which are using different Materials. Refer to documentation on [ShaderLab: SubShader Tags](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShaderTags.html) for more details.
## Distance to Camera
The [Camera component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html) sorts Renderers based on its **Projection** setting. The two options are **Perspective** and **Orthographic**. 
### Perspective
In this mode, the sorting distance of a Renderer is the direct distance of the Renderer from the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera)’s position.
### Orthographic
The sorting distance of a Renderer is the distance between the position of the Renderer and the Camera along the Camera’s view direction. For the default 2D setting, this is along the (0, 0, 1) axis.
When you set the Camera component to **Perspective** or **Orthographic,** Unity automatically sets the Camera’s [TransparencySortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TransparencySortMode.html) to match the selected mode. You can set the Transparency Sort Mode manually in two ways: 
  * Open the ****Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings)** and go to [Graphics](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html#Camera), then under **Camera Settings** use Transparent Sort Mode
  * Set the Camera’s [TransparencySortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TransparencySortMode.html) via the Scripting API.


The Camera **Transparency Sort Mode** settings are under the **Graphics** category in the **Project Settings** (main menu: **Edit** > **Project Settings** > **Graphics**). When this is set to **Default** , a Camera component’s Projection setting take priority. When this is set to an option other than **Default** , the Camera component’s Projection setting remains the same, but the Camera’s **Transparency Sort Mode** changes to that option. 
An additional option available through the Project settings and via the Scripting API is the [Custom Axis sort mode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TransparencySortMode.CustomAxis.html).
### Custom Axis sort mode
Select this mode to sort Renderers based on their distance along the custom axis you set in the Project settings (main menu: **Edit** > **Project Settings** > **Graphics** > **Transparency Sort Axis**). This is commonly used in projects with [Isometric Tilemaps](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-landing.html) to sort and render the Tile Sprites correctly on the Tilemap. Refer to [Creating an Isometric Tilemap](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/create-isometric-tilemap.html) for further information.
**Note:** If your project is a 2D Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) project, the **Transparency Sort Mode** isn’t available in the **Project Settings** , and is instead configured in the 2D Renderer asset properties. Refer to the [Configure the 2D Renderer Asset documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2DRendererData-overview.html) for more information.
### Sprite Sort Point
By default, a **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite)’s **[Sort Point](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/renderer/set-sort-point-sprite.html)** is set to its **Center** , and Unity measures the distance between the camera’s Transform position and the Center of the Sprite to determine their render order during sorting. An alternate option is to set a Sprite’s **Sort Point** to its **Pivot** position in World Space. Select the **Pivot** option in the Sprite’s [Sprite Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/renderer/renderer-landing.html) property settings and edit the Sprite’s Pivot position in the [Sprite Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/sprite-editor-landing.html).
## Sorting Group
The [Sorting Group](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sorting-group/sorting-group-landing.html) is a component that groups Renderers which share a common root together for sorting purposes. All Renderers within the same Sorting Group share the same **Sorting Layer, Order in Layer,** and **Distance to Camera**. Refer to documentation on the [Sorting Group](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sorting-group/sorting-group-landing.html) component and its settings for more details.
## Material/Shader
Unity sorts Renderers with the same [Material settings](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html) together for more efficient rendering performance, such as with [dynamic batching](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DynamicBatching).
## Tiebreaker
When multiple Renderers have identical sorting priority, the tiebreaker is the order that Unity places the Renderers in the Render Queue. Because this is an internal process that you have no control over, you should use the sorting options (such as **Sorting Layers** and **Sorting Groups**) to make sure all Renderers have distinct sorting priorities.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-game-art-syle-reference.html)
2D game art style reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)
Sprites

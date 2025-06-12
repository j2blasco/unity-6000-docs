* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/occlusion-culling-getting-started.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Excluding hidden objects with occlusion culling](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling-landing.html)
  * Set up a scene for occlusion culling


[](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)
Occlusion culling
[](https://docs.unity3d.com/6000.0/Documentation/Manual/occlusion-culling-scene-loading.html)
Set up multiple scenes for occlusion culling
# Set up a scene for occlusion culling
This page describes how to set up your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) for **occlusion culling** A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Occlusionculling), bake your occlusion culling data, and visualize the results.
## Setting up your Scene
Before you begin, identify all of the **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in your Scene that you would like to be Static Occluders (GameObjects that do not move, and that block the view of GameObjects that are behind them) and Static Occludees (GameObjects that do not move, and are occluded by Static Occluders). A GameObject can be both a Static Occluder and a Static Occludee.
Good candidates for Static Occluders are medium to large solid GameObjects, such as a wall or a building. To be a Static Occluder, a GameObject must:
  * Have a [Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) or [Mesh Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer) component
  * Be opaque
  * Not move at runtime


Note that if you are using **LOD** The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LOD) groups, Unity uses the base level GameObject (LOD0) of a Static Occluder to determine what it occludes. If the silhouette of a GameObject varies considerably between LOD0 and other LOD levels, it might not be a good candidate for a Static Occluder.
Any GameObject that is likely to be occluded at runtime is a good candidate to be a Static Occludee, including small or transparent GameObjects. To be a Static Occludee, a GameObject must:
  * Have any type of Renderer component
  * Not move at runtime


When you have identified the GameObjects that you would like to be Static Occluders and Static Occludees, you can set up your Scene.
  1. Select all of the GameObjects that you would like to be Static Occluders.
  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, open the **[Static Editor Flags](https://docs.unity3d.com/6000.0/Documentation/Manual/StaticObjects.html)** drop-down menu and select **Occluder Static**.
  3. Select all of the GameObjects that you would like to be Static Occludees.
  4. In the Inspector window, open the **Static Editor Flags** drop-down menu and select **Occludee Static**.
  5. Add a **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) to your Scene and select it, or select an existing Camera.
  6. In the Inspector window, ensure that the Camera’s **Occlusion Culling** property is enabled.


## Baking the data
  1. In the top menu, select **Window > Rendering > Occlusion Culling** to open the [Occlusion Culling window](https://docs.unity3d.com/6000.0/Documentation/Manual/occlusion-culling-window.html).
  2. Select the **Bake** tab.
  3. In the bottom right hand corner of the Inspector window, press the **Bake** button. Unity generates the occlusion culling data, saves the data as an asset in your Project, and links the asset with the current Scene(s).


## Visualizing the results
  1. Ensure that the Occlusion Culling window and the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) are both visible. When the Occlusion Culling window is visible, Unity displays occlusion culling data and the Occlusion Culling popup in the Scene view.
  2. Select a Camera in the Scene.
  3. Move the Camera around, and observe the Scene view. You should see GameObjects disappear from view when the Camera cannot see them, due to either frustum culling or occlusion culling.
  4. Use the [Occlusion Culling popup](https://docs.unity3d.com/6000.0/Documentation/Manual/occlusion-culling-window.html#occlusion-culling-popup) in the Scene view to configure the visualization.
  5. If required, tweak the [bake settings](https://docs.unity3d.com/6000.0/Documentation/Manual/occlusion-culling-window.html#bake-tab) in the **Bake** tab of the Occlusion Culling window, and repeat the baking process.


If you are using the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), you can use the **Overdraw** [Scene view mode](https://docs.unity3d.com/6000.0/Documentation/Manual/ViewModes.html) to see the amount of overdraw that is occurring, and the Stats panel in the Game view to see the number of triangles, verts, and batches that Unity is rendering.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)
Occlusion culling
[](https://docs.unity3d.com/6000.0/Documentation/Manual/occlusion-culling-scene-loading.html)
Set up multiple scenes for occlusion culling

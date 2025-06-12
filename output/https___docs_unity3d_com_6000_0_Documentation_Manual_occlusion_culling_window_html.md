* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/occlusion-culling-window.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Excluding hidden objects with occlusion culling](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling-landing.html)
  * Occlusion Culling window reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-OcclusionPortal.html)
Control occlusion in areas with Occlusion Portals
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CullingGroupAPI-landing.html)
Configure culling with the CullingGroup API
# Occlusion Culling window reference
Open the Occlusion Culling window by navigating to the top menu and selecting **Window** > **Rendering** > **Occlusion Culling** A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Occlusionculling).
The Occlusion Culling window has 3 tabs: **Object** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Object), **Bake** , and **Visualization**. In addition to this, when both the Occlusion Culling window and the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view are visible, the Occlusion Culling popup is visible in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView).
## Object tab
![Occlusion Culling Window for a Mesh Renderer](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/OcclusionCullingInspectorObject.png) Occlusion Culling Window for a Mesh Renderer
In the **Object** tab, you can click the **All** , **Renderers** , and **Occlusion Areas** buttons to filter the contents of the Hierarchy window.
When the **Renderers** filter is active, select a Renderer in the Hierarchy window or Scene view to view and change its occlusion culling settings in the Occlusion Culling window.
When the **Occlusion Areas** filter is active, you can select an Occlusion Area in the Hierarchy window or Scene view to view and change its **Is View Volume** setting in the Occlusion Culling window. You can also click Create New Occlusion Area to create a new Occlusion Area in the Scene.
## Bake tab
In the **Bake** tab, you can fine-tune the parameters of the Occlusion Culling bake process. Configure these settings to find a balance between bake times, data size at runtime, and visual results.
The **Set Default Parameters** button resets the parameters to the default values.
![Occlusion culling inspector bake tab.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/OcclusionCullingInspectorBake.png) Occlusion culling inspector bake tab. Setting | Description  
---|---  
**Smallest Occluder** | The size of the smallest GameObject that can occlude other GameObjects, in metres. In general, for the smallest file size and fastest bake times, you should choose the highest value that gives good results in your Scene.  
**Smallest Hole** | The diameter of the smallest gap through which a **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) can see, in metres. In general, for the smallest file size and fastest bake times, you should choose the highest value that gives good results in your Scene.  
**Backface Threshold** | If you need to reduce the size of the baked data, Unity can sample the Scene as it bakes, and exclude parts of the Scene where the visible occluder geometry consists of more than a given percentage of backfaces. An area with a high percentage of backfaces is likely to be underneath or inside geometry, and therefore not likely somewhere the Camera is at runtime. The default value of 100 never removes areas from the data. Lower values result in a smaller file size, but can lead to visual artifacts.  
At the bottom of the Bake tab are the **Bake** and **Clear** buttons. Click the **Bake** button to bake occlusion culling data. Click the **Clear** button to remove previously baked data.
## Visualization tab
When you select a Camera in the Scene view or Hierarchy window while the **Visualization** tab is visible, Unity updates the Scene view to show the effects of occlusion culling from the perspective of the selected Camera. You can use the Occlusion Culling popup in the Scene view to configure the visualization.
## Occlusion Culling popup in the Scene view
The Occlusion Culling popup has two modes: **Edit** , and **Visualization**. You can switch between them using the drop-down menu.
### Edit mode
Setting | Description  
---|---  
**View Volumes** | When this is enabled, the Scene view contains blue lines that show the cells in the occlusion culling data. The cell size is affected by the **Smallest Occluder** setting: a lower value results in more, smaller cells, which in turn results in increased precision, and a larger file size.  
## Visualize mode
**Visualize** mode allows you to preview the results of occlusion culling from the perspective of a given Camera. If you have a Camera selected, the preview relates to that Camera. Otherwise, the preview relates to the last Camera that you selected while in Visualize mode.
Setting | Description  
---|---  
**Camera Volumes** | When this is enabled, you can see yellow lines that indicate the area of the Scene for which Unity has generated occlusion culling data. This is determined based on Scene geometry, and on any View Volumes that you have defined in your Scene using Occlusion Areas. When the Camera is outside of the yellow lines, Unity does not perform occlusion culling.  
  
You can also see grey lines that indicate the cell in the occlusion culling data that the Camera’s current position corresponds to, and the subdivisions within the current cell. The **Smallest Hole** setting defines the minimum size of the subdivisions within cells: a lower value results in more, smaller subdivisions per cells, which in turn results in increased precision, and a larger file size.  
**Visibility Lines** | When this is enabled, you can see green lines that indicate what the currently selected Camera can see.  
**Portals** | When this is enabled, you can see lines that represent connections between cells in the occlusion data. The currently visible portals are the ones that the currently selected Camera can see.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-OcclusionPortal.html)
Control occlusion in areas with Occlusion Portals
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CullingGroupAPI-landing.html)
Configure culling with the CullingGroup API

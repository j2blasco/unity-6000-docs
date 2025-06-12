* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-OcclusionArea.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Excluding hidden objects with occlusion culling](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling-landing.html)
  * Create high-precision occlusion areas


[](https://docs.unity3d.com/6000.0/Documentation/Manual/occlusion-culling-dynamic-gameobjects.html)
Cull moving GameObjects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-OcclusionPortal.html)
Control occlusion in areas with Occlusion Portals
# Create high-precision occlusion areas
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OcclusionArea.html "Go to OcclusionArea page in the Scripting Reference")
Use the Occlusion Area component to define View Volumes in the **occlusion culling** A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Occlusionculling) system. View Volumes are areas of the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) where the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) is likely to be located at runtime. At bake time, Unity generates higher precision data within View Volumes. At runtime, Unity performs higher precision calculations when the Camera’s position is within a View Volume.
If you have not defined any View Volumes in your Scene, Unity creates a View Volume at bake time that contains all Scene geometry that is marked as Occluder Static or Occludee Static. This can lead to unnecessarily large data size, slow bake times and resource-intensive runtime calculations in large or complex Scenes. To avoid this, place Occlusion Areas in your Scene to define View Volumes for the areas where the Camera is likely to be.
## Using an Occlusion Area component to define a View Volume
  1. Add an **Occlusion Area** component to an empty **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in your Scene
  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, configure the **Size** property so that the **bounding volume** A closed shape representing the edges and faces of a collider or trigger.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Boundingvolume) covers the desired area
  3. In the Inspector window, enable **Is View Volume**


## Occlusion Area component reference
![Occlusion Area](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Inspector-OcclusionArea.png) Occlusion Area **_Property:_** | **_Function:_**  
---|---  
**Size** | Set the size of the Occlusion Area.  
**Center** | Set the center of the Occlusion Area. By default this is 0,0,0 and is located in the center of the box.  
**Is View Volume** | If enabled, the Occlusion Area defines a View Volume. If disabled, the Occlusion Area does not define a View Volume. This must be enabled for an Occlusion Area to work.  
OcclusionArea
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/occlusion-culling-dynamic-gameobjects.html)
Cull moving GameObjects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-OcclusionPortal.html)
Control occlusion in areas with Occlusion Portals

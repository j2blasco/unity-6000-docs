* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-OcclusionPortal.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Excluding hidden objects with occlusion culling](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling-landing.html)
  * Control occlusion in areas with Occlusion Portals


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-OcclusionArea.html)
Create high-precision occlusion areas
[](https://docs.unity3d.com/6000.0/Documentation/Manual/occlusion-culling-window.html)
Occlusion Culling window reference
# Control occlusion in areas with Occlusion Portals
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OcclusionPortal.html "Go to OcclusionPortal page in the Scripting Reference")
An Occlusion Portal can either be open or closed. When an Occlusion Portal is closed, it occludes other **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). When an Occlusion Portal is open, it does not occlude other GameObjects. 
If you have a GameObject in your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) that has an open and a closed state (such as a door), you can create an Occlusion Portal that represents it in the **occlusion culling** A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Occlusionculling) system. You can then set the open state of the Occlusion Portal according to the state of that GameObject. An Occlusion Portal component does not need to be placed on the GameObject it represents.
## Setting up an Occlusion Portal in your Scene
  1. Choose a suitable GameObject in your Scene to act as an Occlusion Portal. Good candidates for Occlusion Portals are medium to large solid GameObjects, such as a door.
  2. Ensure that the GameObject is not marked as Occluder Static or Occludee Static.
  3. Add an **Occlusion Portal** component to the GameObject.
  4. Bake the occlusion data for your Scene. See [Getting started with occlusion culling](https://docs.unity3d.com/6000.0/Documentation/Manual/occlusion-culling-getting-started.html) for instructions.
  5. Ensure that the Occlusion Culling window, the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) panel and the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) are all visible.
  6. In the Scene view, move the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) to a position where it is directly in front of the Occlusion Portal.
  7. Select the GameObject with the Occlusion Portal component.
  8. In the Inspector window, toggle the Occlusion Portal component’s **Open** property on and off. In the Scene view, observe the difference in occlusion culling.


## Opening and closing an Occlusion Portal at runtime
Use a script to set the Occlusion Portal’s [open](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OcclusionPortal-open.html) property to the desired state.
```
void OpenDoor() {
     // Toggle the Occlusion Portal's open state, so that Unity renders the GameObjects behind it
    myOcclusionPortal.open = true;
    
    // Call a function that plays a door opening animation, or otherwise hides the GameObject
    …
}

```

## Occlusion Portal component reference
**_Property:_** | **_Function:_**  
---|---  
**Open** | If enabled, the Occlusion Portal is open, and does not occlude Renderers. If disabled, the Occlusion Portal is closed, and occludes Renderers.  
**Center** | Set the center of the Occlusion Portal. The default value is 0,0,0.  
**Size** | Define the size of the Occlusion Portal.  
OcclusionPortal
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-OcclusionArea.html)
Create high-precision occlusion areas
[](https://docs.unity3d.com/6000.0/Documentation/Manual/occlusion-culling-window.html)
Occlusion Culling window reference
